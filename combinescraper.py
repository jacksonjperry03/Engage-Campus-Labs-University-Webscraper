import argparse

# Import functions from clubscraper.py
from clubscraper import scrape_json_data as scrape_club_json_data
from clubscraper import main as club_main

# Import functions from eventscraper.py
from eventscraper import fetch_rss_data
from eventscraper import scrape_json_data as scrape_event_json_data
from eventscraper import main as event_main


def main(html_file_path, base_url, output_dir=None):
    try:
        # If output directory is not provided, default to 'output' folder in current directory
        if output_dir is None:
            output_dir = 'output'

        # Run club scraper
        club_main(html_file_path, base_url, output_dir)

        # Run event scraper
        event_main(base_url, output_dir)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape organization and event data from a webpage.')
    parser.add_argument('html_file', type=str, help='Path to the HTML file')
    parser.add_argument('base_url', type=str, help='Base URL of the webpage')
    parser.add_argument('--output', type=str, help='Path to the output directory to save data', default=None)
    args = parser.parse_args()

    main(args.html_file, args.base_url, args.output)
