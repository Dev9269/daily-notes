import re

NMAP_STEALTH = re.compile(r'-T[0-2]\b')

def reject_reason(cmd):
    if re.search(r'(?:^|\s)(?:sudo\s+)?nmap\b', cmd) and not NMAP_STEALTH.search(cmd):
        return 'loud_nmap'
    return None
