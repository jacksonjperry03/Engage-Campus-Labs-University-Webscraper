import feedparser
import json
import requests
import argparse
import os
import csv
from bs4 import BeautifulSoup

# Fetch the RSS feed data
def fetch_rss_data(rss_url):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Prepare response data
    events = []
    for item in feed.entries:
        event = {
            'link': item.link,
        }
        events.append(event)

    return events

def write_to_csv(event_info, csv_file):
    try:
        if event_info is None:
            print("Event info is None.")
            return

        # Extract relevant information from event_info
        event_details = event_info.get('preFetchedData', {}).get('event', {})
        id = event_details.get('id', '')
        name = event_details.get('name', '')

        description_html = event_info['preFetchedData']['event']['description']
        soup = BeautifulSoup(description_html, 'html.parser')
        description_text = soup.get_text(strip=True)

        start_time = event_details.get('startsOn', '')
        ends_on = event_details.get('endsOn', '')

        benefits = event_details.get('benefits', '')
        benefits_str = ', '.join(benefits) if isinstance(benefits, list) else benefits

        # Extract address information if available
        address_info = event_details.get('address', {})
        if address_info:
            address_name = address_info.get('name', '')
            address = address_info.get('address', '')

        category_list = []
        categories = event_details.get('categories', [])
        for category in categories:
            category_list.append(category.get('name', ''))
        categories_str = ', '.join(category_list)

        # Write to CSV file
        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            event_writer = csv.writer(csvfile)
            # Write header if the file is empty
            if os.stat(csv_file).st_size == 0:
                event_writer.writerow(["ID", "Name", "Description", "Start Time", "End Time", "Benefits", "Address Name", "Address", "Categories"])
            event_writer.writerow([id, name, description_text, start_time, ends_on, benefits_str, address_name, address, categories_str])

        print(f"Event data successfully written to {csv_file}.")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

def scrape_json_data(url, index, csv_file):
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
                event_info = json.loads(json_raw)
                write_to_csv(event_info, csv_file)
                break
        
        print(f"\nURL: {url}")

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

def main(base_url, output_dir=None):
    rss_url = f"{base_url}/events.rss"
    try:
        # Fetch events from the RSS feed
        events = fetch_rss_data(rss_url)

        # If output directory is not provided, default to 'output' folder in current directory
        if output_dir is None:
            output_dir = 'output'

        # Check if the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Construct the path to the CSV file
        csv_file = os.path.join(output_dir, 'events.csv')

        # Iterate over each event and scrape JSON data
        for index, event in enumerate(events):
            scrape_json_data(event['link'], index, csv_file)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape event data from an RSS feed.')
    parser.add_argument('base_url', type=str, help='Base URL of the webpage')
    parser.add_argument('--output', type=str, help='Path to the output directory to save event data', default=None)
    args = parser.parse_args()

    main(args.base_url, args.output)
