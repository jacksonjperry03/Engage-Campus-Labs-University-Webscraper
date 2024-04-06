from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import requests
import json
import csv
import argparse

# Get the directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

def write_to_csv(club_info, url, output_file):
    try:
        # Extract image server base URL and profile image path
        image_server_base_url = club_info.get('imageServerBaseUrl', '')
        profile_image_path = club_info['preFetchedData']['organization'].get('profilePicture', '')
        profile_image_url = f"{image_server_base_url}/{profile_image_path}"

        # Extract relevant fields
        organization_info = club_info.get('preFetchedData', {}).get('organization', {})
        id = organization_info.get('id', '')
        name = organization_info.get('name', '')
        email = organization_info.get('email', '')
        
        # Extract and clean description using BeautifulSoup
        description_text = ''
        description_html = organization_info.get('description', '')
        if description_html == None:
            if (organization_info.get('summary', '') != None and organization_info.get('summary', '').lower() != 'to be created'):
                description_text = organization_info.get('summary', '')
        else:
            soup = BeautifulSoup(description_html, 'html.parser')
            description_text = soup.get_text(strip=True)

         # Extract relevant fields
        contact_info = organization_info.get('contactInfo', [])
        if contact_info:
            contact_info = contact_info[0]
            city = contact_info.get('city', '')
            state = contact_info.get('state', '')
            street1 = contact_info.get('street1', '')
            street2 = contact_info.get('street2', '')
            zip_code = contact_info.get('zip', '')
        else:
            city = state = street1 = street2 = zip_code = ''

        social_media = organization_info.get('socialMedia', {})
        external_website = social_media.get('externalWebsite', '')
        instagram_url = social_media.get('instagramUrl', '')

        # Extracted fields from JSON data
        header = ["Profile Image URL","ID", "Name", "Email", "Description", "City", "State", "Street1", "Street2", "Zip Code", "External Website", "Instagram URL"]
        
        # Write to CSV file
        with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
            club_writer = csv.writer(csvfile)
            
            # Write the header row if the file is empty
            if os.stat(output_file).st_size == 0:
                club_writer.writerow(header)
            
            club_writer.writerow([profile_image_url, id, name, email, description_text, city, state, street1, street2, zip_code, external_website, instagram_url])
        
        print(f"\nURL: {url}\nData successfully written to {output_file}.")

    except Exception as e:
        print(f"An error occurred while writing to a csv file: {e}")

def scrape_json_data(url, output_file):
    try:
        # Make an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid responses

        # Parse HTML content
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        # Find script tags containing JSON data
        script_tags = soup.find_all('script')

        # Iterate through script tags to find JSON data
        for script in script_tags:
            if 'initialAppState' in script.text:
                # Extract JSON data
                json_raw = script.text[25:-1]  # Remove unnecessary characters
                club_info = json.loads(json_raw)
                write_to_csv(club_info, url, output_file)
                break

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

def main(html_file_path, base_url, output_dir=None):
    
    # If output directory is not provided, default to 'output' folder in current directory
    if output_dir is None:
        output_dir = 'output'

    # Check if the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the path to the CSV file
    output_file = os.path.join(output_dir, 'clubs.csv')
    
    # Read the HTML content from the file
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all 'a' tags with 'href' attribute
    links = soup.find_all('a', href=True)

    # Extract and normalize URLs from 'href' attributes
    all_urls = [urljoin(base_url, link['href']) for link in links]

    organization_urls = [url for url in all_urls if '/organization/' in url]

    for url in organization_urls:
        scrape_json_data(url, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape organization data from a webpage.')
    parser.add_argument('html_file', type=str, help='Path to the HTML file')
    parser.add_argument('base_url', type=str, help='Base URL of the webpage')
    parser.add_argument('--output', '-o', type=str, help='Path to output CSV file (default: clubs.csv in the project directory)')
    args = parser.parse_args()

    main(args.html_file, args.base_url, args.output)
