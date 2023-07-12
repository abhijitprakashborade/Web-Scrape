# Import the necessary libraries for Scraping Data:
import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from the table and store in a CSV file
def scrape_data():
    base_url = "https://www.teaboard.gov.in/WEEKLYPRICES/"

    # Open CSV file for writing
    with open('average_location.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(['week', 'location', 'average_price'])  

        # Iterate over years from 2008 to 2023 using for loop
        for year in range(2008, 2024):
            url = f"{base_url}{year}"
            r= requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            

            # Find the table with id 'contn_GridView2'
            table = soup.find('table', id='contn_GridView2')
            # Find all rows in the table (excluding header row)
            rows = table.find_all('tr')[1:]

            # Iterate over rows and extract data 
            # text.strip for removing back
            for row in rows:
                cells = row.find_all('td')
                week = cells[0].text.strip()
                location = cells[1].text.strip()
                average_price = cells[2].text.strip()

                # Write a data to CSV file 
                writer.writerow([week, location, average_price])

    #   Call the function to start scraping
scrape_data()
