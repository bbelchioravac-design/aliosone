# -*- coding: utf-8 -*-
"""
gerar.py — fábrica de artigos da ALIOS ONE.

Lê artigos/*.md (markdown com cabeçalho YAML), gera <slug>.html na raiz
com o template do site, e actualiza a lista de artigos no index.html
(entre os marcadores ARTIGOS:INICIO / ARTIGOS:FIM).

Corre no GitHub Actions a cada push em artigos/ — ou localmente:
    python build/gerar.py
"""
import html
import re
import sys
from pathlib import Path

import markdown
import yaml

RAIZ = Path(__file__).resolve().parent.parent
PASTA_ARTIGOS = RAIZ / "artigos"
TEMPLATE = RAIZ / "templates" / "artigo.html"
INDEX = RAIZ / "index.html"

MARCA_GERADO = "<!-- gerado automaticamente por build/gerar.py — NÃO editar à mão -->"

CORES_TAG = {
    "Conforto & Energia": "var(--orange)",
    "Regulamentação": "var(--blue)",
    "IA no terreno": "var(--magenta)",
    "Bastidores": "var(--green)",
}
COR_DEFEITO = "var(--blue)"

MESES_PT = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
MESES_EN = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]

BIO_PT_DEFEITO = ("Beatriz Belchior é engenheira mecânica, investigadora "
                  "independente em comportamento de LLMs, e fundadora da ALIOS ONE.")
BIO_EN_DEFEITO = ("Beatriz Belchior is a mechanical engineer, independent "
                  "researcher in LLM behaviour, and founder of ALIOS ONE.")

TOGGLE_HTML = """    <div class="lang-toggle">
      <button class="lang-btn active" onclick="switchLang('pt')">PT</button>
      <button class="lang-btn" onclick="switchLang('en')">EN</button>
    </div>"""

SECCAO_EN_HTML = """    <!-- ═══ ENGLISH ═══ -->
    <div class="lang-content" id="lang-en">
      <div class="article-meta">{tag_en} · {data_en}</div>
      <h1 class="article-title">{titulo_en}</h1>
      <p class="article-subtitle">ALIOS ONE · {autor}</p>

      <div class="article-body">
{body_en}
        <p class="article-author">{bio_en}</p>
      </div>
    </div>
"""


def md_para_html(texto_md: str) -> str:
    """Markdown → HTML no estilo do site (hr vira separador visual)."""
    corpo = markdown.markdown(texto_md, extensions=["extra", "sane_lists"])
    corpo = re.sub(r"<hr\s*/?>", '<div class="article-separator"></div>', corpo)
    # indentação para o HTML final ficar legível
    return "\n".join("        " + linha for linha in corpo.splitlines())


def ler_artigo(caminho: Path) -> dict:
    texto = caminho.read_text(encoding="utf-8")
    partes = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", texto, re.DOTALL)
    if not partes:
        raise ValueError(f"{caminho.name}: falta o cabeçalho YAML (--- ... ---)")
    meta = yaml.safe_load(partes.group(1)) or {}
    meta["corpo"] = partes.group(2).strip()

    # versão inglesa: ou no campo corpo_en (painel), ou após <!-- EN --> no corpo
    if "<!-- EN -->" in meta["corpo"] and not meta.get("corpo_en"):
        pt, en = meta["corpo"].split("<!-- EN -->", 1)
        meta["corpo"], meta["corpo_en"] = pt.strip(), en.strip()

    for obrigatorio in ("titulo", "data", "tag", "resumo"):
        if not meta.get(obrigatorio):
            raise ValueError(f"{caminho.name}: falta o campo '{obrigatorio}'")

    meta["data"] = str(meta["data"])[:10]  # YYYY-MM-DD
    if not re.match(r"\d{4}-\d{2}-\d{2}$", meta["data"]):
        raise ValueError(f"{caminho.name}: data '{meta['data']}' não é YYYY-MM-DD")

    meta.setdefault("slug", re.sub(r"^\d{4}-\d{2}-\d{2}-", "", caminho.stem))
    meta.setdefault("autor", "Beatriz Belchior")
    meta.setdefault("bio", BIO_PT_DEFEITO)
    meta.setdefault("bio_en", BIO_EN_DEFEITO)
    meta.setdefault("publicado", True)
    return meta


def data_bonita(data: str, meses: list) -> str:
    ano, mes, _ = data.split("-")
    return f"{meses[int(mes) - 1]} {ano}"


def gerar_pagina(meta: dict, template: str) -> str:
    cor = CORES_TAG.get(meta["tag"], COR_DEFEITO)
    tem_en = bool(meta.get("corpo_en", "").strip())

    seccao_en = ""
    toggle = ""
    if tem_en:
        toggle = TOGGLE_HTML
        seccao_en = SECCAO_EN_HTML.format(
            tag_en=html.escape(str(meta.get("tag_en", meta["tag"]))),
            data_en=data_bonita(meta["data"], MESES_EN),
            titulo_en=html.escape(str(meta.get("titulo_en", meta["titulo"]))),
            autor=html.escape(str(meta["autor"])),
            body_en=md_para_html(meta["corpo_en"]),
            bio_en=html.escape(str(meta["bio_en"])),
        )

    pagina = template
    substituicoes = {
        "{{TITULO_PT}}": html.escape(str(meta["titulo"])),
        "{{RESUMO_PT}}": html.escape(str(meta["resumo"])),
        "{{TAG}}": html.escape(str(meta["tag"])),
        "{{COR_TAG}}": cor,
        "{{DATA_PT}}": data_bonita(meta["data"], MESES_PT),
        "{{AUTOR}}": html.escape(str(meta["autor"])),
        "{{BODY_PT}}": md_para_html(meta["corpo"]),
        "{{BIO_PT}}": html.escape(str(meta["bio"])),
        "{{LANG_TOGGLE}}": toggle,
        "{{SECCAO_EN}}": seccao_en,
    }
    for chave, valor in substituicoes.items():
        pagina = pagina.replace(chave, valor)
    return pagina.replace("<body>", f"<body>\n{MARCA_GERADO}", 1)


def item_index(meta: dict) -> str:
    cor = CORES_TAG.get(meta["tag"], COR_DEFEITO)
    return (
        '          <div class="pub-article">\n'
        f'            <div class="pub-article-tag" style="color: {cor}">{html.escape(str(meta["tag"]))}</div>\n'
        f'            <h4><a href="{meta["slug"]}.html" style="color: inherit; text-decoration: none;">'
        f'{html.escape(str(meta["titulo"]))}</a></h4>\n'
        f'            <p>{html.escape(str(meta["resumo"]))}</p>\n'
        '          </div>'
    )


def actualizar_index(artigos: list) -> None:
    conteudo = INDEX.read_text(encoding="utf-8")
    inicio, fim = "<!-- ARTIGOS:INICIO -->", "<!-- ARTIGOS:FIM -->"
    if inicio not in conteudo or fim not in conteudo:
        raise ValueError("index.html: faltam os marcadores ARTIGOS:INICIO/FIM")
    bloco = "\n".join(item_index(a) for a in artigos[:3])
    novo = re.sub(
        re.escape(inicio) + r".*?" + re.escape(fim),
        f"{inicio}\n{bloco}\n          {fim}",
        conteudo,
        flags=re.DOTALL,
    )
    INDEX.write_text(novo, encoding="utf-8")


def limpar_orfaos(slugs_actuais: set) -> None:
    """Apaga HTML gerado cujo artigo .md já não existe."""
    for ficheiro in RAIZ.glob("*.html"):
        if ficheiro.name == "index.html":
            continue
        if MARCA_GERADO in ficheiro.read_text(encoding="utf-8", errors="ignore"):
            if ficheiro.stem not in slugs_actuais:
                print(f"  órfão removido: {ficheiro.name}")
                ficheiro.unlink()


def main() -> int:
    template = TEMPLATE.read_text(encoding="utf-8")
    artigos = []
    for md_file in sorted(PASTA_ARTIGOS.glob("*.md")):
        meta = ler_artigo(md_file)
        if not meta["publicado"]:
            print(f"  rascunho (publicado: false), ignorado: {md_file.name}")
            continue
        artigos.append(meta)

    artigos.sort(key=lambda a: a["data"], reverse=True)

    for meta in artigos:
        destino = RAIZ / f"{meta['slug']}.html"
        destino.write_text(gerar_pagina(meta, template), encoding="utf-8")
        print(f"  gerado: {destino.name}  ({meta['data']} · {meta['tag']})")

    actualizar_index(artigos)
    print(f"  index.html actualizado ({min(len(artigos), 3)} artigos na montra)")
    limpar_orfaos({a["slug"] for a in artigos})
    return 0


if __name__ == "__main__":
    sys.exit(main())
