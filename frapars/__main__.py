import pandas as pd
import csv
from frapars.functions.addresses import parse_all_parallel, parse
from frapars.constants import out_file_path as out_csv
import importlib.metadata
import argparse
# import ptvsd

version = importlib.metadata.version('frapars')


def print_banner():
    # Read the contents of the banner.txt file
    with open('banner.txt', 'r') as file:
        banner_text = file.read()
    # Replace ${application.version} with the desired version
    banner_text = banner_text.replace('${application.version}', version)
    # Print the modified banner
    print(banner_text)


def csv_from_dict(file_path, data):
    print(f"Storing into file the results")
    # Write the list of dictionaries to a CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    print("Result printed at: ", file_path)


def parse_from_file(in_file_path, out_file_path, limit=None):
    df = pd.read_csv(in_file_path, dtype='str', encoding='latin-1')
    df = df.dropna()
    if limit:
        csv_addr_list = list(df['address'])[:limit]
    else:
        csv_addr_list = list(df['address'])

    print(f"Found {len(csv_addr_list)} addresses to parse")
    results = parse_all_parallel(csv_addr_list)
    i = 0
    for address, parsed_address in zip(results, csv_addr_list):
        results.append({
            'original':  address,
            'parsed':  parsed_address,
        })
        i += 1
    #  store in the file the data collected
    csv_from_dict(out_file_path, results)


def parse_from_list(list_of_addresses):
    #  split the addresses
    addresses = list_of_addresses.split(';')

    # Print each value as list
    result = parse_all(addresses)
    for ua, pa in zip(addresses, result):
        print(f"Unparsed: {ua} --> Parsed: {pa}")


def parse_from_address(address_str):
    parse(address_str, verbose=True)


def main():
    print_banner()
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Example Argument Parser')
    # Create a mutually exclusive group for input options
    input_group = parser.add_mutually_exclusive_group(required=True)

    # Add arguments
    input_group.add_argument('-i', '--input-file',
                             type=str, help='Path to the input file')
    input_group.add_argument('-l', '--list', type=str,
                             help='List of inputs. Needs to be on format "rue saint-Philippe 31; Aevenue Carlos (De) 31"')
    input_group.add_argument('-a', '--address', type=str,
                             help='Single input address. Ex: "rue saint-Philippe 31 (De)"')

    # Parse the arguments
    args = parser.parse_args()

    # Execute based on the input arg
    if args.input_file:
        parse_from_file(args.input_file, out_csv)
    if args.list:
        parse_from_list(args.list)
    if args.address:
        parse_from_address(args.address)

    print(f"Process has finished!")


if __name__ == "__main__":
    main()
