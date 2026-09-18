package main

import (
"errors"
"io"
"net/http"
"time"
)

const _maxRedirects = 5

func _0001(req request) response {
timeout := time.Duration(req.Timeout) * time.Second
if timeout <= 0 { timeout = 15 * time.Second }
maxSize := req.MaxSize
if maxSize <= 0 { maxSize = 5_000_000 }
redirects := 0
client := &http.Client{
Timeout: timeout,
CheckRedirect: func(r *http.Request, via []*http.Request) error {
redirects++
if redirects > _maxRedirects { return errors.New("too many redirects") }
return nil
},
}
resp, err := client.Get(req.URL)
if err != nil { return response{URL: req.URL, Error: err.Error()} }
defer resp.Body.Close()
body, err := io.ReadAll(io.LimitReader(resp.Body, int64(maxSize)))
if err != nil { return response{URL: req.URL, Error: err.Error()} }
return response{
URL:         req.URL,
Status:      resp.StatusCode,
ContentType: resp.Header.Get("Content-Type"),
Size:        len(body),
Body:        string(body),
}
}