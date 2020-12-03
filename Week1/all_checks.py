#!/usr/local/bin python3
import os

def check_reboot():
    """Returns True is the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    pass

main()