import csv

def read_rows(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def write_rows(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
