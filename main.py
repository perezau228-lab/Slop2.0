#!/usr/bin/env python3
"""
main.py
-------
CLI entry point. Wires grabber.py (capture) and detector.py (pattern
matching) together, same "orchestration only" role Main.py played in
your last project.

IMPORTANT: only run this against your own test server (see
test_server.py) or networks/devices you own.

TODO(you): fill in the pieces marked below.
"""

import argparse

from grabber import start_capture
from detector import looks_like_credentials, is_post_request


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sniff HTTP traffic for cleartext credentials (learning tool)."
    )
    parser.add_argument("-i", "--interface", default=None)
    parser.add_argument(
        "-f", "--filter", dest="bpf_filter", default="tcp port 5000",
        help='BPF filter (default targets your local test server on port 5000)'
    )
    # TODO(you): any other CLI options you think would be useful?
    # (e.g. an --output flag to log findings to a file, like your last project)
    return parser.parse_args()


def handle_payload(payload: bytes, packet):
    """
    Called by grabber.py every time a packet with a payload is captured.

    TODO(you):
      - Call is_post_request() -- if it's not a POST, you probably want
        to skip it (or at least handle GET differently).
      - Call looks_like_credentials() on the payload.
      - If it found anything, print a clear alert -- include the source
        IP/port if you can get them from `packet` (same way you pulled
        src/dst out of packets in your last project).
    """
    raise NotImplementedError


def main():
    args = parse_args()
    print(f"Starting capture (filter: {args.bpf_filter}) -- Ctrl+C to stop.")
    print("Reminder: only run this against your own test server.\n")

    # TODO(you): call start_capture() with the right arguments,
    # passing handle_payload as the callback.
    # TODO(you): wrap this in a try/except KeyboardInterrupt like before,
    # so Ctrl+C exits cleanly instead of crashing.
    raise NotImplementedError


if __name__ == "__main__":
    main()
