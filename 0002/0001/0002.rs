pub fn _0001(s: &str) -> Vec<String> {
    let mut out: Vec<String> = Vec::new();
    let b = s.as_bytes();
    let n = b.len();
    let mut i = 0usize;
    while i < n {
        let c = b[i];
        if c == b'"' || c == b'\'' || c == b'`' {
            let q = c;
            let mut j = i + 1;
            let mut esc = false;
            while j < n {
                let d = b[j];
                if esc { esc = false; j += 1; continue; }
                if d == b'\\' { esc = true; j += 1; continue; }
                if d == q { break; }
                j += 1;
            }
            if j < n {
                let raw = &s[i + 1..j];
                if raw.len() <= 4096 {
                    out.push(raw.to_string());
                }
            }
            i = j + 1;
        } else {
            i += 1;
        }
    }
    out
}