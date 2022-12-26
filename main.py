"""Script to scan ports to see if they are open or closed with the Sockets Library"""

import socket
import termcolor


def scan(target, ports):
	for port in range(1, ports + 1):
		scan_port(target, port)  # Iterate through each of the specified ports to scan


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(termcolor.colored(text="[+] Port ({port}) open at address {ipaddress}", color="green"))
		sock.close()  # Close the socket object once a connection has been established
	except TimeoutError:
		print(termcolor.colored(
			text=f"Timeout Error: Unable to connect to specified address {ipaddress} due to timeout",
			color="red"
		))
		pass
	except OSError:
		print(termcolor.colored(
			text=f"OSError: Unable to connect to specified address {ipaddress} and port {port} due to permissions",
			color="red"
		))
		pass
	except ConnectionRefusedError:
		# # Uncomment if you would like to know what ports are closed
		# print(termcolor.colored(text=f"[-] Port ({port}) closed at address {ipaddress}", color="orange"))
		pass


while True:
	targets = input("[*] Enter target IP Addresses to Scan (Separate targets by a ',' only): ")
	if " " in targets:
		print(termcolor.colored(text="Invalid Address(es). Try Again.", color="red"))
	else:
		targets_list = targets.split(sep=",")
		port_range = int(input("[*] Enter how many ports do you want to scan: "))
		for address in targets_list:
			scan(target=address, ports=port_range)
	print(termcolor.colored(text="[+] Scan Complete", color="green"))
