WSJ Article Archive Scraper:
This project is a Python-based web scraper for extracting historical articles from the Wall Street Journal (WSJ) archive using Selenium and BeautifulSoup. The tool automates browsing through date-specific pages, collects headlines, links, and timestamps, and optionally extracts full article content for each entry.

Features:
  Automatically builds and navigates WSJ archive URLs from a list of dates (dates_list.csv)

Extracts:
  Headline
  Article link
  Timestamp
  Supports pagination for multi-page archive days
  Fetches and prints article content (via content_creator)
  Configurable via CSV input
Designed for scraping automation and data collection research

Project Structure:
├── dates_list.csv            # Input CSV file with date list (YYYY-MM-DD)
├── dates_dataset.csv         # (Optional) Final dataset or output file (in development)
├── functions_in_scraper.py   # Main scraper code

Technologies Used:
  Python

Selenium==> (with Microsoft Edge WebDriver)

BeautifulSoup4 ==>(HTML parsing)

CSV (for structured date input)

How It Works:
  dates_list.csv is read to generate a list of dates.
  Each date is converted into a URL for the WSJ archive.
  The scraper opens the URL in Edge, scrolls, paginates through results, and extracts article data.
  For each article, headline, link, and timestamp are logged and passed to content_creator.
  content_creator() opens the article link in a separate browser session and extracts article body text (currently printed).
  
Example Output:
  yaml:
  Headline: Nasdaq Drops 2%
  Link: https://www.wsj.com/articles/...
  Timestamp: Jan 03, 2000
  Date: 2000/01/03


Disclaimer:
This scraper is built for educational and personal research purposes. Be mindful of WSJ’s Terms of Service and avoid aggressive scraping that may violate access policies or copyright rules.

Author
Talaat Sallam
GitHub: https://github.com/talaat259

