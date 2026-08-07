def classify(mac):
    oui = mac[:8].upper()
    return {'rt3572': 'Ralink', 'rtl88': 'Realtek'}.get(oui[:4], 'unknown')
