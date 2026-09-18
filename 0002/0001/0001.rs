mod _0002;
mod _0003;

use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for line in stdin.lock().lines() {
        let line = match line { Ok(v) => v, Err(_) => break };
        if line.is_empty() { continue; }
        let strings = _0002::_0001(&line);
        let matched = _0003::_0002(&strings);
        for u in &matched {
            let _ = writeln!(out, "{{\"url\":{:?}}}", u);
        }
    }
    let _ = out.flush();
}