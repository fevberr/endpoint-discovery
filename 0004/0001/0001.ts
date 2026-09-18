import { createInterface } from "node:readline";
import { analyze } from "./0002.js";

const rl = createInterface({ input: process.stdin });
rl.on("line", (line) => {
  if (!line) return;
  try {
    const msg = JSON.parse(line);
    const out = analyze(msg.source, msg.url ?? "");
    process.stdout.write(JSON.stringify({ url: msg.url ?? "", findings: out }) + "\n");
  } catch (e) {
    process.stdout.write(JSON.stringify({ error: String(e) }) + "\n");
  }
});