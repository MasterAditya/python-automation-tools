import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Example: scrape table rows
rows = soup.find_all("tr")
data = []
for row in rows:
    cols = [col.text.strip() for col in row.find_all("td")]
    if cols:
        data.append(cols)

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Scraped data saved to output.csv")
