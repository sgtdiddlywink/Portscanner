import socket
import termcolor
import argparse
from concurrent.futures import ThreadPoolExecutor


def scan(target, ports):
    with ThreadPoolExecutor() as executor:
        for port in range(1, ports + 1):
            executor.submit(scan_port, target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] Port ({port}) open at address {ipaddress}", color="green"))
        sock.close()  # Close the socket object once a connection has been established
    except TimeoutError:
        print(termcolor.colored(
            text=f"Timeout Error: Unable to connect to specified address {ipaddress} due to timeout",
            color="red"
        ))
    except OSError:
        print(termcolor.colored(
            text=f"OSError: Unable to connect to specified address {ipaddress} and port {port} due to permissions",
            color="red"
        ))
    except ConnectionRefusedError:
        # # Uncomment if you would like to know what ports are closed
        # print(termcolor.colored(text=f"[-] Port ({port}) closed at address {ipaddress}", color="orange"))
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan open ports")
    parser.add_argument("target", help="IP address to scan")
    parser.add_argument("ports", type=int, help="Number of ports to scan")
    args = parser.parse_args()
    scan(args.target, args.ports)
    print(termcolor.colored(text="[+] Scan Complete", color="green"))
