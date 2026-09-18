package main

import (
"bufio"
"encoding/json"
"os"
)

type request struct {
URL     string `json:"url"`
Timeout int    `json:"timeout"`
MaxSize int    `json:"max_bytes"`
}

type response struct {
URL         string `json:"url"`
Status      int    `json:"status"`
ContentType string `json:"content_type"`
Size        int    `json:"size"`
Body        string `json:"body,omitempty"`
Error       string `json:"error,omitempty"`
}

func main() {
sc := bufio.NewScanner(os.Stdin)
sc.Buffer(make([]byte, 1024*1024), 64*1024*1024)
enc := json.NewEncoder(os.Stdout)
for sc.Scan() {
line := sc.Bytes()
if len(line) == 0 { continue }
var req request
if err := json.Unmarshal(line, &req); err != nil {
_ = enc.Encode(response{Error: "invalid request"})
continue
}
res := _0001(req)
_ = enc.Encode(res)
}
}