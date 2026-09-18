import * as walk from "acorn-walk";
import type { Finding } from "./0002.js";

export function _0003(ast: any, source: string): Finding[] {
  const out: Finding[] = [];
  walk.simple(ast, {
    CallExpression(node: any) {
      const callee = node.callee;
      if (!callee) return;
      if (callee.type === "Identifier" && callee.name === "fetch") {
        const url = _str(node.arguments?.[0]);
        if (url) out.push(_mk(url, "GET", "fetch", node));
      } else if (callee.type === "MemberExpression") {
        const name = _member(callee);
        if (name === "axios" || name?.startsWith("axios.")) {
          const url = _str(node.arguments?.[0]);
          const method = name.includes(".") ? name.split(".")[1].toUpperCase() : "GET";
          if (url) out.push(_mk(url, method, "axios", node));
        } else if (name === "xhr.open" || name === "XMLHttpRequest.open") {
          const m = _str(node.arguments?.[0]);
          const u = _str(node.arguments?.[1]);
          if (u) out.push(_mk(u, (m ?? "GET").toUpperCase(), "xhr", node));
        }
      }
    },
    NewExpression(node: any) {
      const c = node.callee;
      if (c?.type === "Identifier" && c.name === "WebSocket") {
        const u = _str(node.arguments?.[0]);
        if (u) out.push(_mk(u, "WS", "websocket", node));
      }
    },
  });
  return out;
}

function _mk(url: string, method: string, detector: string, node: any): Finding {
  return {
    url,
    method,
    detector,
    line: node.loc?.start?.line ?? 0,
    column: node.loc?.start?.column ?? 0,
    expression: "call",
  };
}

function _str(n: any): string | null {
  if (!n) return null;
  if (n.type === "Literal" && typeof n.value === "string") return n.value;
  if (n.type === "TemplateLiteral" && n.expressions?.length === 0) {
    return n.quasis.map((q: any) => q.value.cooked).join("");
  }
  return null;
}

function _member(n: any): string | null {
  if (n.type !== "MemberExpression") return null;
  const o = n.object?.type === "Identifier" ? n.object.name : null;
  const p = n.property?.type === "Identifier" ? n.property.name : null;
  if (!o || !p) return null;
  return `${o}.${p}`;
}