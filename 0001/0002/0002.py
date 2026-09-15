from __future__ import annotations

_VALID_SCOPE = {"same-origin", "host", "any"}
_VALID_VERBOSITY = {"quiet", "normal", "verbose", "debug"}
_VALID_FORMAT = {"terminal", "json", "jsonl", "csv"}


def _0001(_opts) -> list:
    _errs: list = []
    if _opts.scope not in _VALID_SCOPE:
        _errs.append(
            f'Invalid scope: "{_opts.scope}". '
            f'Expected one of: {", ".join(sorted(_VALID_SCOPE))}.'
        )
    if _opts.verbosity not in _VALID_VERBOSITY:
        _errs.append(
            f'Invalid verbosity: "{_opts.verbosity}". '
            f'Expected one of: {", ".join(sorted(_VALID_VERBOSITY))}.'
        )
    if _opts.output_format not in _VALID_FORMAT:
        _errs.append(
            f'Invalid output format: "{_opts.output_format}". '
            f'Expected one of: {", ".join(sorted(_VALID_FORMAT))}.'
        )
    if _opts.timeout <= 0:
        _errs.append(
            f'Invalid timeout: "{_opts.timeout}". '
            'Expected a positive integer of seconds.'
        )
    if _opts.depth < 0:
        _errs.append(f'Invalid depth: "{_opts.depth}". Expected a non-negative integer.')
    if _opts.concurrency <= 0:
        _errs.append(
            f'Invalid concurrency: "{_opts.concurrency}". Expected a positive integer.'
        )
    if _opts.rate_limit < 0:
        _errs.append(
            f'Invalid rate limit: "{_opts.rate_limit}". Expected a non-negative number.'
        )
    if _opts.max_bytes <= 0:
        _errs.append(
            f'Invalid max bytes: "{_opts.max_bytes}". Expected a positive integer.'
        )
    if _opts.max_redirects < 0:
        _errs.append(
            f'Invalid max redirects: "{_opts.max_redirects}". '
            'Expected a non-negative integer.'
        )
    return _errs