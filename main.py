# Importing necessary modules and classes
from banner import print_banner
from scanner.scanner import scan_url_for_open_redirect
from scanner.url import data
import argparse
import os
import re

# Define the main function
def main():
    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description='Open Redirect Vulnerability Scanner')
    parser.add_argument('-u', '--url', type=str, help='URL to scan')
    parser.add_argument('-i', '--input', type=str, help='Read input URLs from file')
    parser.add_argument('-o', '--output', type=str, help='Write output to file')
    parser.add_argument('-b', '--blog', action='store_true', help='Read about the bug')
    args = parser.parse_args()

    # Printing the banner
    print_banner()

    # If no arguments are provided, show the help menu
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Displaying URLs from the data class if specified
    if args.blog:
        print("Blog URL:", data.blog)
        print("Website URL:", data.website)
        print("To read more about open redirect vulnerabilities, visit: https://owasp.org/www-community/attacks/Unvalidated_Redirects_and_Forwards_Cheat_Sheet")
        return  # Terminate the script after displaying the URLs

    # Creating a list to store URLs
    urls_to_scan = []

    # Adding URL from command line argument if provided
    if args.url:
        urls_to_scan.append(args.url)

    # Adding URLs from a file if provided
    if args.input:
        input_path = os.path.abspath(args.input)
        if not os.path.exists(input_path):
            print(f"Error: The file {input_path} does not exist.")
            return
        try:
            with open(input_path, 'r') as file:
                urls_to_scan.extend([line.strip() for line in file.readlines()])
        except Exception as e:
            print(f"Error reading input file: {e}")
            return

    # Validating URLs
    def is_valid_url(url):
        return re.match(r'^(http|https)://', url) is not None

    urls_to_scan = [url for url in urls_to_scan if is_valid_url(url)]

    # List to store scan results
    results = []

    # Scanning each URL for open redirects
    for url in urls_to_scan:
        result = scan_url_for_open_redirect(url)
        if result:
            print(result)
            results.append(result)

    # Writing results to a file if specified
    if args.output:
        try:
            output_path = os.path.abspath(args.output)
            with open(output_path, 'w') as file:
                for result in results:
                    file.write(result + '\n')
            print(f"Results written to {args.output}")
        except Exception as e:
            print(f"Error writing output file: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()

