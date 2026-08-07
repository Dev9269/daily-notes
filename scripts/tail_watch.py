import time

def watch(path, n=10):
    with open(path) as f:
        lines = f.readlines()[-n:]
        print(''.join(lines))
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line, end='')
            else:
                time.sleep(0.5)
