# endpoint-discovery

Static endpoint and web reconnaissance framework.

Extracts candidate API endpoints from HTML, JavaScript bundles, TypeScript sources, source maps, and configuration objects. Passive and static only.

## Install

    python -m pip install -e .

## Quick start

    endpoint-discovery --help
    endpoint-discovery --file 0013\0001.html --json
    endpoint-discovery --file 0013\0003.js --confidence high
    endpoint-discovery https://example.com --depth 2 --source-maps

## Output formats

- terminal
- --json
- --jsonl
- --csv results.csv
- --sarif results.sarif
- --sqlite scan.db
- --graph graph.json

## License

MIT.
