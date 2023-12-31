import argparse
import os

def process_urls(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            unique_endpoints = {('/'.join(line.strip().split('/')[:i])) for line in infile for i in range(3, len(line.split('/')) + 1)}
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(sorted(unique_endpoints)) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process URLs from input file and generate output file with endpoints.")
    parser.add_argument("--input", dest="input_file", help="Input file containing URLs", required=True)
    parser.add_argument("-o", dest="output_file", help="Output file to store processed URLs", required=True)
    args = parser.parse_args()

    process_urls(args.input_file, args.output_file)
