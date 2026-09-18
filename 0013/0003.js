const base = "/api/v1";
async function list() {
  return fetch(`${base}/users`);
}
function create(payload) {
  return fetch("/api/v1/users", { method: "POST", body: JSON.stringify(payload) });
}
new WebSocket("wss://example.com/ws");