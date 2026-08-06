import ip_tool
import sys

def main(argv):
    for host in argv[1:]:
        try:
            print(host, '->', ip_tool.resolve(host))
        except Exception as exc:
            print(host, 'ERR', exc)

if __name__ == '__main__':
    main(sys.argv)
