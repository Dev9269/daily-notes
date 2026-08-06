import re

NMAP_STEALTH = re.compile(r'-T[0-2]\b')
LOUD_TOOLS = re.compile(r'(?:^|\s)(?:sudo\s+)?(nmap|masscan|hydra)\b')

def reject_reason(cmd):
    if LOUD_TOOLS.search(cmd) and not NMAP_STEALTH.search(cmd):
        return 'loud_scan'
    return None
