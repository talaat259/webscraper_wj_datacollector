
# WSJ Article Archive Scraper

A Python-based web scraper for extracting historical articles from the Wall Street Journal (WSJ) archive using Selenium and BeautifulSoup.  
**Purpose:** Automate archive browsing and data collection for research.

---

## Features

- **Automated URL Generation:** Builds and navigates WSJ archive URLs from a configurable list (`dates_list.csv`)
- **Article Extraction:** Collects headline, article link, timestamp, and article content
- **Pagination Support:** Handles multi-page archive days
- **Content Fetching:** Uses `content_creator` to retrieve and print full article body text
- **Configurable Input:** Easily specify scraping dates via CSV
- **Designed For:** Automation and research in data collection

---

## Project Structure

```
├── dates_list.csv            # Input: List of dates (YYYY-MM-DD)
├── dates_dataset.csv         # Output: Final dataset (optional, in development)
├── functions_in_scraper.py   # Main scraper code
```

---

## Technologies Used

- **Python**
- **Selenium** (with Microsoft Edge WebDriver)
- **BeautifulSoup4** (HTML parsing)
- **CSV** (structured date input)

---

## How It Works

1. **Read Date List:** Loads dates from `dates_list.csv`
2. **URL Generation:** Converts each date to a WSJ archive URL
3. **Scraping Flow:**
   - Opens the URL in Edge
   - Scrolls and paginates through results
   - Extracts headline, link, and timestamp for each article
   - Passes article link to `content_creator` for full text extraction
4. **Output:** Prints or stores article data for each date

---

## Example Output

```yaml
Headline: Nasdaq Drops 2%
Link: https://www.wsj.com/articles/...
Timestamp: Jan 03, 2000
Date: 2000/01/03
```

---

## Disclaimer

This scraper is intended for educational and personal research purposes.  
Please respect WSJ’s Terms of Service and avoid any scraping practices that may violate access policies or copyright rules.

---

## Author

**Talaat Sallam**  
GitHub: [https://github.com/talaat259](https://github.com/talaat259)

---
