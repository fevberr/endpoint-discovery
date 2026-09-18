
# endpoint-discovery

<img src="https://p16-tiktok-dm-sticker-sign-sg.ibyteimg.com/tos-alisg-i-dhq7zx4c1p-sg/d179a29e560642bba3707aa2ec9babd8~tplv-dhq7zx4c1p-full.awebp?rk3s=00edd399&x-expires=1792029789&x-signature=qrJJe26DGlzonOoaKdczYDcF0BE%3D" alt="RAHHHH">

Static endpoint and web reconnaissance framework. Walks a page, parses the markup, scans the bundles, and reconstructs candidate API endpoints. Passive and static only.

---

**Stack**

<p>
  <img src="https://cdn.simpleicons.org/python" alt="Python" width="20">
  <img src="https://cdn.simpleicons.org/rust" alt="Rust" width="20">
  <img src="https://cdn.simpleicons.org/typescript" alt="TypeScript" width="20">
  <img src="https://cdn.simpleicons.org/javascript" alt="JavaScript" width="20">
  <img src="https://cdn.simpleicons.org/sqlite" alt="SQLite" width="20">
</p>

---

**Author** — [fevberr](https://github.com/fevberr) *(super coolz guy btw)*

---

## Install

```powershell
git clone https://github.com/fevberr/endpoint-discovery.git
cd endpoint-discovery
python -m pip install -e .
```

Optional accelerators:

```powershell
cd 0002; cargo build --release; cd ..
cd 0004; npm install; npm run build; cd ..
```

---

## Use

```powershell
python -m _launcher --help

python -m _launcher --file 0013\0001.html
python -m _launcher --file 0013\0003.js

python -m _launcher https://example.com
python -m _launcher https://example.com --depth 2 --source-maps
python -m _launcher https://example.com --json
python -m _launcher https://example.com --jsonl
python -m _launcher https://example.com --csv results.csv
python -m _launcher https://example.com --sarif results.sarif
python -m _launcher https://example.com --sqlite scan.db
python -m _launcher https://example.com --graph graph.json
python -m _launcher https://example.com --confidence high
```

---

## What it finds

- HTML references: `script`, `link`, `a`, `iframe`, `form`, `preload`, `modulepreload`, `data-*` hints, inline JSON
- JavaScript request sites: `fetch`, `XMLHttpRequest.open`, `axios.<verb>`, `new WebSocket`
- Static reconstruction of string literals and empty template literals
- Classifications: absolute, relative, api, graphql, websocket, authentication, static
- Confidence scoring with visible evidence per finding

## What it never does

- No probing of discovered endpoints
- No form submission, no auth attempts, no credential collection
- No telemetry, no analytics, no hidden network requests

---
## Tests

```powershell
python -m pytest 0009 -q
```


## License

MIT © 2026 fevberr
```
MIT License

Copyright (c) 2026 fevberr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
