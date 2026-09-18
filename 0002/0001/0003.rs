use std::collections::HashSet;

static PREFIXES: &[&str] = &[
    "http://", "https://", "ws://", "wss://", "/api/", "/v1/", "/v2/",
    "/v3/", "/graphql", "/rest/", "/rpc/", "/auth/", "/oauth/",
];

pub fn _0002(xs: &[String]) -> Vec<String> {
    let mut out: Vec<String> = Vec::new();
    let mut seen: HashSet<String> = HashSet::new();
    for x in xs {
        if x.len() > 2048 { continue; }
        if !plausible(x) { continue; }
        if seen.insert(x.clone()) {
            out.push(x.clone());
        }
    }
    out
}

fn plausible(s: &str) -> bool {
    if s.is_empty() { return false; }
    for p in PREFIXES {
        if s.starts_with(p) { return true; }
    }
    false
}