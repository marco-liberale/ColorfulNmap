print("Made by Marco Liberale")
import argparse

import nmap
from termcolor import colored
try:
    parser = argparse.ArgumentParser(description="A simple nmap scanning tool")
    parser.add_argument("-t", "--target", type=str, help="target host to scan", required=True)
    parser.add_argument("-n", "--nmap-help", help="show nmap's help message", action="store_true")
    parser.add_argument("-p", "--ports", type=str, help="port range to scan(e.g. '22-443')", default="1-1000")
    args, unknown = parser.parse_known_args()

    args.arguments = ' '.join(unknown)

    nm = nmap.PortScanner()
    if args.nmap_help:
        os.system("nmap -h")
        exit(0)
    print(colored(f"\n========= SCANNING {args.target.upper()} =========", 'green'))
    try:
        nm.scan(args.target, args.ports, arguments=args.arguments)
    except nmap.nmap.PortScannerError as e:
        e = str(e).replace('"', '')
        e = str(e).replace('\\n', '')

        print(colored(f"Error occurred: {str(e).strip()}", 'red'))
        exit(1)

    for host in nm.all_hosts():
        print(colored('\n-------------------------', 'yellow'))
        print(colored(f'Host : {host} ({nm[host].hostname()})', 'cyan'))
        print(colored(f'State : {nm[host].state()}', 'cyan'))

        for proto in nm[host].all_protocols():
            print(colored('\n----------', 'yellow'))
            print(colored(f'Protocol : {proto}', 'cyan'))

            lport = nm[host][proto].keys()
            for port in lport:
                print(colored(f'\nPort : {port}', 'blue'))
                print(colored(f"State : {nm[host][proto][port]['state']}", 'blue'))
                print(colored(f"Service : {nm[host][proto][port]['name']}", 'blue'))
                print(colored(f"Product : {nm[host][proto][port]['product']}", 'blue'))
                print(colored(f"Version : {nm[host][proto][port]['version']}", 'blue'))
                print(colored(f"Extra Info : {nm[host][proto][port]['extrainfo']}", 'blue'))

    print(colored("\n-------------------------", 'yellow'))
    print(colored("SCAN COMPLETE\n", 'green'))
except KeyboardInterrupt:
    print(colored("Stopping scanner", 'red'))
    exit(0)
except Exception as e:
    e = str(e).replace('"', '')
    e = str(e).replace('\\n', '')

    print(colored(f"Error occurred: {str(e).strip()}", 'red'))
    exit(1)
