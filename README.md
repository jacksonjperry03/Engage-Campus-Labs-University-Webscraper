# Engage-Campus-Labs-University-Webscraper
Campus Labs is a web-based platform used by over 1,400 public and private [colleges and universities](https://changingthepresent.org/pages/list-of-campuslabs-page) to display information relating to collegiate organizations and events. 

These Python programs are designed to scrape relevant organization and event details from Campus Labs University sites and store them in a CSV file.

After wrestling with the intricacies of scraping dynamic websites and sifting through outdated webscraping tools and repositories, I found myself at a dead end in my quest for info on university clubs and events. Luckily, after some time I stumbled upon an insightful [article](https://danielbeadle.net/post/2018-04-14-scraping-react-with-python/) that shed light on the annoying task of scraping React with Python. I expanded on the concept by implementing my own webscraping solution and ended up learning many new things along the way.

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

     - Replace `<path_to_html_file>` with the path to the saved HTML file containing organization information. **(Remember to enclose the path in quotes)**
     - Go back to the homepage of the Campus Labs University site and copy the base URL. Replace `<base_url>` with this URL. **(Remember to enclose the URL in quotes)**
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

To run the `eventscraper.py` program, use the following command:

```bash
python eventscraper.py <base_url> [--output <output_file>]
```
Go back to the homepage of the Campus Labs University site and copy the base URL. Replace `<base_url>` with this URL. **(Remember to enclose the URL in quotes)**, and `<output_file>` with the optional path to save the CSV file. If the `--output` argument is not provided, the CSV file will be saved in the "output" folder within the project directory by default.

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

### combinescraper.py

The `combinescraper.py` script provides a convenient way to scrape both organization and event data from the Campus Labs University sites. It generates two separate CSV files, one for organizations (clubs) and another for events.

To use the combined scraper, follow these steps:

1. **Prepare HTML File (if you have not already done so):** 
   - Open a web browser and navigate to the Campus Labs University site.
   - Load the Organizations page and click the "Load More" button repeatedly until all organizations are loaded.
   - Save the HTML file of the loaded page to your local system.

2. **Run the Combined Scraper:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `combinescraper.py` script.
   - Execute the following command:

     ```bash
     python combinescraper.py <html_file_path> <base_url> [--output <output_dir>]
     ```

     - Replace `<html_file_path>` with the file path to the saved HTML file containing organization information.
     - Replace `<base_url>` with the base URL of the Campus Labs University site.
     - Optionally, specify `--output` followed by the desired directory path to save the CSV files. If not specified, the CSV files will be saved in the "output" folder within the project directory by default.

#### Output Files

Upon successful execution, the combined scraper generates two CSV files:

- `clubs.csv`: Contains information about organizations (clubs) including profile image URL, ID, name, email, description, contact details, and social media links.

- `events.csv`: Contains details about events including ID, name, description, start time, end time, benefits, address, and categories.

#### Patience During Scraping
During the scraping process, the program retrieves information from each page, processes it, and saves it to a CSV file. Please be patient while the program is running, as it may take a few minutes or even longer to scrape all the necessary data. Additionally, ensure that your internet connection is stable to avoid interruptions during the scraping process.

If you encounter any issues or have suggestions for improvement, feel free to open an issue on GitHub. Contributions are also welcome through pull requests.

Thank you for using Engage-Campus-Labs-University-Webscraper!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is intended for educational and informational purposes only. While web scraping itself is not necessarily illegal, the legality and ethical considerations surrounding it can vary by jurisdiction and context. It is essential to use this software responsibly and to ensure that your web scraping activities comply with applicable laws, terms of service, and ethical guidelines. The developers of this software do not endorse or condone any unethical or illegal use of web scraping tools. Users are encouraged to exercise caution and discretion when using this software and to seek legal advice if necessary.

---
*This README document was partially generated with the assistance of AI.*
