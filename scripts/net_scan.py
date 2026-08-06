import ip_tool

for host in ['192.168.1.1', '10.0.0.1']:
    print(host, ip_tool.resolve(host))
