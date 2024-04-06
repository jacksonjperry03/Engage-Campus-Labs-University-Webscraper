# Engage-Campus-Labs-University-Webscraper
Campus Labs is a web-based platform used by over 1,400 public and private colleges and universities to display information relating to collegiate organizations and events.

These Python programs are designed to scrape relevant organization and event details from Campus Labs University sites and store them in a CSV file.

After wrestling with the intricacies of scraping dynamic websites and sifting through outdated webscraping tools and repositories, I found myself at a dead end in my quest for info on university clubs and events. Luckily, after some time I stumbled upon an insightful [article](https://danielbeadle.net/post/2018-04-14-scraping-react-with-python/) that shed light on the annoying task of scraping React with Python. I expanded on the concept by implementing my own webscraping solution and ended up learning many new things along the way.

## Usage

### Prerequisites

Before using this program, make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/jacksonjperry03/Engage-Campus-Labs-University-Webscraper.git

2. Open a command line interface (CLI) or terminal on your system.

3. Navigate to the project directory:

   ```bash
   cd Engage-Campus-Labs-University-Webscraper

4. Install the required Python packages using pip:
   
   ```bash
   pip install -r requirements.txt

### clubscraper.py

1. **Load All Organizations:**

   - Open a web browser and navigate to the Campus Labs University site.
   - On the Organizations page, locate the "Load More" button, and click it repeatedly until all organizations are loaded.
   - Once all organizations are loaded, right-click on the page and select "Save Page As" to save the HTML file. Choose a location on your system to save the file, and remember the path for later use.

2. **Run the Club Scraper:**

     ```bash
     python clubscraper.py <path_to_html_file> <base_url> [--output <output_csv_file>]
     ```

     - Replace `<path_to_html_file>` with the path to the saved HTML file containing organization information.
     - Go back to the homepage of the Campus Labs University site and copy the base URL. Replace `<base_url>` with this URL.
     - Optionally, specify `--output` followed by the desired path to save the CSV file. If not specified, it will be saved in the "output" folder within the project directory.

### Selection of Fields

The fields chosen for extraction were selected based on their relevance to my specific use case and the information available on the Campus Labs University site. Here's a brief overview of each included field:

- **Profile Image URL**: Provides a visual representation of each organization.
- **ID**: Unique identifier for accurate differentiation between organizations.
- **Name**: Fundamental information for identifying each organization.
- **Email**: Allows for easy communication with organizations.
- **Description**: Offers a brief overview of each organization's purpose and activities.
- **City, State, Street1, Street2, Zip Code**: Enables geographical categorization of organizations.
- **External Website**: Allows users to explore additional information about organizations.
- **Instagram URL**: Facilitates social media engagement with organizations.

These fields collectively provide comprehensive information about each organization, enhancing the usability and utility of our dataset.

### eventscraper.py

Before running eventscraper.py, you need to retrieve the RSS URL for the function argument. This URL can be found at the bottom right corner of the Campus Engage site's event page.

1. **Navigate to the Engage Site's Event Page**: Open a web browser and navigate to the event page of your university's Engage site.

2. **Locate the RSS Feed Link**: Scroll down to the bottom right corner of the event page. You should find a link labeled "RSS" or "RSS Feed". Right-click on this link and select "Copy Link Address" or similar option depending on your browser.

To run the `eventscraper.py` program, use the following command:

```bash
python eventscraper.py <rss_url> [--output <output_file>]
```
Replace `<rss_url>` with the RSS URL for the Engage site's event page, and `<output_file>` with the optional path to save the CSV file. If the `--output` argument is not provided, the CSV file will be saved in the "output" folder within the project directory by default.

The fields chosen for eventscraper.py were selected based on my subjective relevance ranking of event details that are commonly available on the Engage site's event pages. These fields provide essential information about each event, including:

- **ID**: Unique identifier for the event.
- **Name**: Name or title of the event.
- **Description**: Description or details about the event.
- **Start Time**: Date and time when the event starts.
- **End Time**: Date and time when the event ends.
- **Benefits**: Any benefits associated with attending the event.
- **Address Name**: Name of the location where the event is held.
- **Address**: Address details of the event location.
- **Categories**: Categories or tags associated with the event.

These fields were chosen to capture key information about each event 😎

If you encounter any issues or have suggestions for improvement, feel free to open an issue on GitHub. Contributions are also welcome through pull requests.

Thank you for using Engage-Campus-Labs-University-Webscraper!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is intended for educational and informational purposes only. While web scraping itself is not necessarily illegal, the legality and ethical considerations surrounding it can vary by jurisdiction and context. It is essential to use this software responsibly and to ensure that your web scraping activities comply with applicable laws, terms of service, and ethical guidelines. The developers of this software do not endorse or condone any unethical or illegal use of web scraping tools. Users are encouraged to exercise caution and discretion when using this software and to seek legal advice if necessary.

---
*This README document was partially generated with the assistance of AI.*
