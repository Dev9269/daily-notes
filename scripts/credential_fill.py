def extract_password(lines):
    for line in lines:
        if line.startswith('password='):
            return line[9:]
    return None
