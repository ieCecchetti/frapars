import re
from frapars.functions import clean_str
import frapars.constants.regex as rx
import ptvsd
import pandas as pd
import csv
from tqdm import tqdm
from frapars.constants import in_file_path, out_file_path


def score_percentage(text):
    # Calculate the percentage score based on the length of the string
    if len(text) <= 50:
        # If the length is less than or equal to 50, calculate the percentage
        percentage_score = ((50 - len(text)) / 50)
    else:
        # If the length is more than 50, percentage score is 0%
        percentage_score = 1.0
    return percentage_score


def format_details(address_info):
    address_str = "{} {} {} {} {} {} {} {} {}".format(
        (' ').join(address_info.get('addres_num', '')),
        (' ').join(address_info.get('urba_names', '')),
        (' ').join(address_info.get('prepositions', '')),
        (' ').join(address_info.get('street_name', '')),
        (' ').join(address_info.get('city', '')),
        (' ').join(address_info.get('postcode', '')),
        (' ').join(address_info.get('insee', '')),
        (' ').join(address_info.get('codes', '')),
        (' ').join(address_info.get('department', '')),
    )
    # Replace multiple spaces with a single space
    address_str = re.sub(r'\s+', ' ', address_str)
    # Capitalize the first letter of each word
    return address_str.title()


def parse(addresses_str, verbose=False):
    parsed_addresses = []
    # there can be multiple str
    addresses = re.split(r';|et', addresses_str)
    for address_str in addresses:
        address_str = address_str.strip()
        parsed_addresses.append(parse_single_address(address_str, verbose))
    return ' et '.join(parsed_addresses)


def parse_single_address(address_str, verbose=False):
    if verbose:
        print(f"Initial address is: {address_str}")
    addr_details = {}
    norm_address = clean_str.normalize_text(address_str)

    # Find all matches for urban names using the compiled pattern
    addr_details['urba_names'], norm_address = rx.exec(
        rx.urban_names_pattern, norm_address)

    # Find all matches for preposition using the compiled pattern
    addr_details['prepositions'], norm_address = rx.exec(
        rx.prepositions_pattern, norm_address)
    norm_address = norm_address.replace('()', '')

    # Find all matches for city using the compiled pattern
    date_streets, norm_address = rx.exec(
        rx.date_pattern, norm_address)

    # Find all matches for city using the compiled pattern
    addr_details['city'], norm_address = rx.exec(
        rx.city_pattern, norm_address)

    # Find all matches for postcode using the compiled pattern
    codes, norm_address = rx.exec(
        rx.postal_insee_code_pattern, norm_address)
    # find the category of the insee
    if len(codes):
        addr_details['insee'], addr_details['postcode'], addr_details['codes'] = rx.parse_codes(
            codes)

    # Find all matches for address number using the compiled pattern
    addr_details['addres_num'], norm_address = rx.exec(
        rx.address_num_pattern, norm_address)

    # Find all matches for address_num using the compiled pattern
    addr_details['department'], norm_address = rx.exec(
        rx.department_pattern, norm_address)

    # Handle the rest
    addr_details['street_name'], norm_address = rx.exec(
        rx.street_name_pattern, norm_address)
    addr_details['street_name'].extend(date_streets)

    parsed_address = format_details(addr_details)
    if verbose:
        print(f"Result is: {parsed_address}")
        print(f"Details: {addr_details}")
        print(f"Unparsed string remained is: {norm_address}")
        print(f"Parse quality scored: {score_percentage(norm_address)}")
    return parsed_address.strip()


if __name__ == "__main__":
    print("Welcome to Fra-pars")
    df = pd.read_csv(in_file_path, dtype='str', encoding='latin-1')
    df = df.dropna()
    # TODO: remove the limit
    csv_addr_list = list(df['address'])[:1000]
    print(f"Found {len(csv_addr_list)} addresses to parse")
    results = []
    i = 0
    for address in tqdm(csv_addr_list, desc="Processing", unit="item"):
        parsed_address = parse(address, verbose=False)
        results.append({
            'original':  address,
            'parsed':  parsed_address,
        })
        i += 1
    print(f"Storing into file the results")
    # Write the list of dictionaries to a CSV file
    with open(out_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"Process has finished!")
