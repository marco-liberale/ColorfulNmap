# ColorfulNmap
This Python script is a simple, user-friendly command-line interface for the nmap network scanning tool. It enhances the output of nmap scans with color-coding and formatting for better readability.

## Features

- : Specify the target host to scan using the `-t` or `--target` option. This is a required argument.
    

- : Display nmap's help message using the `-n` or `--nmap-help` option.
    

- : Specify the range of ports to scan using the `-p` or `--ports` option. By default, all ports (1-65535) are scanned.
    

- : Pass any additional arguments for nmap directly to the script. These arguments are forwarded to nmap as-is.
    

- : The output of the scan is color-coded for better readability. Information about each host is displayed in a structured format, with separate sections for each protocol and port.
    

## Installation

To install this tool, you need to clone the repository from GitHub and install the required Python libraries.

1. Clone the repository:

```bash
git clone https://github.com/marco-liberale/ColorfulNmap
```



2. Navigate to the cloned repository:

```bash
cd ColorfulNmap
```



3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

To use the script, run it from the command line with the desired options. For example:

```bash
python main.py -t 192.168.1.1 -p 22-443 -A
```

This will scan the host at 192.168.1.1 for open ports in the range 22-443 using the Nmap agressive mode.

## Error Handling

The script handles errors and exceptions gracefully. If an error occurs during the scan, the error message is displayed in red color and the script exits with a non-zero status code. If the script is interrupted with a keyboard interrupt (Ctrl+C), it displays a message and exits cleanly.

## Dependencies

This script depends on the following Python libraries:

- `argparse` for parsing command-line arguments.
- `python-nmap` for performing the network scans.
- `os` for interacting with the operating system.
- `termcolor` for color-coding the output.

## Legal Disclamer
By using the repository, you acknowledge that you have read this [Disclaimer](https://github.com/marco-liberale/ColorfulNmap/blob/main/legal_disclamer.md) and agree to be bound by the terms hereof.
If you do not agree to abide by the above, please do not use the repository.



Enjoy :)
