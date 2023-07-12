# Tea Scraper

 I have Written this Python script that scrapes data from the "WEEKLY AVERAGE PRICES OF TOTAL TEA SOLD AT INDIAN AUCTION" table on the Tea Board of India website.

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
3. Open a file name `Scrape.py` in this directory.
4. write the Python script to scrape the data.    

### Dependencies

   1. beautifulsoup4==4.9.3
   2. pandas==1.3.0
   3. requests==2.26.0
   4. csv

#### Running process
1. Run the `Scrape.py` file.
2. The script will scrape the data from the website and save it as a CSV file named `avarege_location.csv` in the same directory.

##### OUTPUT
The scraped data will be saved in a CSV file named `avarege_location.csv` in the root directory of the project. Each row in the CSV file will contain the following columns:

   1. week: The week of the tea price data formatted as DD-MM-YYYY.
   2. location: The location where the tea was sold.
   3. average_price: The average price of tea as reported on the website.