import sys
import socket 
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Riad \n Port Scanner")
print(ascii_banner)


ip = sys.argv[1]
max_port = sys.argv[2]
open_ports = []

ports = range(1, int(max_port))

def port_scan(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result


for port in ports:
    print(port, end="\r")
    sys.stdout.flush()
    response = port_scan(ip, port)
    if response == 0:
        open_ports.append(port)


if open_ports:
    print('Open ports are: ')
    print(sorted(open_ports))
else:
    print('No ports are open on the host: ', ip)

