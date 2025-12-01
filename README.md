Web Scraping Practice — Python Project

This project is a practical exercise in web scraping using Python, focusing on extracting article titles from the website OpenCodez.
The project demonstrates essential scraping techniques using Requests and BeautifulSoup, and saves the collected data for further analysis.

🔍 Project Goals
Learn and practice web scraping in Python
Extract textual content (article titles) from a real website
Clean and process scraped data
Display structured results
Build a foundation for more advanced scraping and data projects

🛠 Technologies Used
Python 3
Requests – for sending HTTP requests
BeautifulSoup4 – for parsing HTML
re (Regular Expressions) – for text cleaning

📦 Project Structure
web_scrap_practice/
│
├── web_scrapping_practice.py   # main scraper file
├── README.md                   # project documentation
└── output/                     # optional (you can add CSV/JSON output later)

▶️ How to Run the Script
1) Install dependencies:
pip install requests beautifulsoup4

2) Run the script:
python web_scrapping_practice.py

📌 What the Script Does
Sends a GET request to:
https://www.opencodez.com

Parses the homepage HTML
Finds all article blocks matching class:
div.td-block-span6

Extracts:
Title of each article
Cleans text (removes extra whitespace, newlines)
Prints results with numbering

