"""
detector.py
-----------
Phase 2 lives here: given a raw payload, decide whether it looks like
it's carrying cleartext credentials, and say why.

TODO(you): fill in the pieces marked below.
"""

# TODO(you): think about what byte-string keywords indicate credentials.
# Some starting categories to research and add to:
#   - URL-encoded form fields (password=, passwd=, pwd=, user=, login=)
#   - HTTP Basic Auth header (Authorization: Basic ...)
#   - FTP commands (USER, PASS)
# Question to answer for yourself: should these be bytes (b"password=")
# or should you decode the payload to a string first? What's the
# tradeoff? (We talked about this in Phase 2 -- revisit your answer.)

KEYWORDS = [
    # TODO(you): fill this in
]


def looks_like_credentials(payload: bytes) -> list[str]:
    """
    Inspect a raw payload and return a list of reasons it might contain
    cleartext credentials (empty list if it doesn't look suspicious).

    Example return value: ["contains 'password=' in body"]

    TODO(you):
      - Decide how you'll search: bytes-in-bytes, or decode first?
        Handle the case where decoding might fail (not all payloads
        are valid UTF-8/ASCII text -- some are binary data).
      - Loop through KEYWORDS and check for each one.
      - For HTTP Basic Auth specifically: if you find "Authorization: Basic",
        the actual credentials are base64-encoded right after it. Do you
        want to just flag it, or actually decode it? (Try decoding it by
        hand first with Python's `base64` module to see what it looks like
        before writing that logic.)
      - Return a list describing what you found (this makes your alerts
        much more useful than just "found something suspicious").
    """
    raise NotImplementedError


def is_post_request(payload: bytes) -> bool:
    """
    Quick check: does this payload look like the start of an HTTP POST
    request? (POST requests are far more likely to carry credentials
    than GET requests.)

    TODO(you):
      - What does the very start of an HTTP request line look like?
        (Try `curl -v` against a test server and look at the raw
        request line it prints.)
    """
    raise NotImplementedError
