#Open Redirect Vulnerability Scanner

This tool helps identify open redirect vulnerabilities in URLs. It can scan individual URLs or read a list of URLs from a file and check for potential open redirects. Additionally, it provides options to write the scan results to an output file and display URLs from predefined sources.

## Usage

1. **Installation**: Before using the tool, make sure you have Python 3.x installed. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

2. **Running the Tool**: Execute the `main.py` script to run the scanner. Here's how you can use it:

    ```
    python main.py [options]
    ```

    Options:
    - `-u, --url <url>`: Specify a single URL to scan.
    - `-i, --input <filename>`: Read URLs from a file for scanning.
    - `-o, --output <filename>`: Write scan results to a file.
    - `-b, --blog`: Display predefined blog and website URLs.
    - `-h, --help`: Show help menu.




