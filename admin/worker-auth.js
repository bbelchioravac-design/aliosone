// alios-admin-auth — intermediário de login GitHub para o painel /admin
// Vive num Cloudflare Worker. Precisa de 2 variáveis de ambiente:
//   GITHUB_CLIENT_ID e GITHUB_CLIENT_SECRET (da OAuth App do GitHub)
// Endpoints: /auth (início do login) e /callback (retorno do GitHub)

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/auth") {
      const state = crypto.randomUUID();
      const destino =
        "https://github.com/login/oauth/authorize" +
        `?client_id=${env.GITHUB_CLIENT_ID}` +
        "&scope=repo" +
        `&state=${state}`;
      return Response.redirect(destino, 302);
    }

    if (url.pathname === "/callback") {
      const code = url.searchParams.get("code");
      const resposta = await fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "User-Agent": "alios-admin-auth",
        },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });
      const dados = await resposta.json();
      const token = dados.access_token;
      const estado = token ? "success" : "error";
      const conteudo = token
        ? { token, provider: "github" }
        : { error: dados.error || "sem token" };

      // handshake que o Decap CMS espera na janela de login
      const html = `<!doctype html><html><body><script>
        (function () {
          function responder(e) {
            window.opener.postMessage(
              'authorization:github:${estado}:${JSON.stringify(conteudo)}',
              e.origin
            );
          }
          window.addEventListener('message', responder, false);
          window.opener.postMessage('authorizing:github', '*');
        })();
      </script></body></html>`;
      return new Response(html, { headers: { "Content-Type": "text/html" } });
    }

    return new Response("alios-admin-auth: operacional", { status: 200 });
  },
};
