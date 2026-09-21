"""
grabber.py
----------
Phase 1 lives here: capture packets and hand back their raw payload
(if they have one) so detector.py can search it for cleartext
credentials.

TODO(you): fill in the pieces marked below.
"""

from scapy.all import sniff, TCP, Raw


def extract_payload(packet) -> bytes | None:
    """
    Return the raw payload bytes from a packet, or None if it doesn't
    have one (e.g. a bare TCP ACK with no data).

    TODO(you):
      - Check whether `packet` has a Raw layer.
      - If it does, return packet[Raw].load
      - If it doesn't, return None
    """
    raise NotImplementedError


def start_capture(interface: str | None, bpf_filter: str | None, on_payload):
    """
    Start a live capture. For every packet that has a payload, call
    on_payload(payload_bytes, packet) so main.py/detector.py can react
    to it.

    Parameters:
        interface: which NIC to capture on (None = scapy's default)
        bpf_filter: a BPF filter string, e.g. "tcp port 5000"
                    (this is a CAPTURE filter -- ask yourself why that
                    matters vs. filtering in Python afterward)
        on_payload: a callback function you'll pass in from main.py

    TODO(you):
      - Write the scapy sniff() call.
      - Inside a small internal callback function, call extract_payload()
        on each packet.
      - If it returned something (not None), call on_payload(payload, packet)
      - Remember: sniff() needs `iface=`, `filter=`, and `prn=` arguments,
        similar to your last project's TrafficCapture class.
    """
    raise NotImplementedError
