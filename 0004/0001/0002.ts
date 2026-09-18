import { parse } from "acorn";
import { _0003 } from "./0003.js";

export interface Finding {
  url: string;
  method: string;
  detector: string;
  line: number;
  column: number;
  expression: string;
}

export function analyze(source: string, url: string): Finding[] {
  let ast: any;
  try {
    ast = parse(source, {
      ecmaVersion: "latest",
      sourceType: "module",
      locations: true,
      allowHashBang: true,
      allowReturnOutsideFunction: true,
    });
  } catch {
    return [];
  }
  return _0003(ast, url);
}