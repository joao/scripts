import feedparser
from bs4 import BeautifulSoup

def clean_html(raw_html):
    return BeautifulSoup(raw_html, "html.parser").get_text(strip=True)

def print_latest_entries(rss_url, count=10):
    feed = feedparser.parse(rss_url)
    entries = feed.entries[:count]
    
    for i, entry in enumerate(entries, 1):
        title = clean_html(entry.title)
        link = entry.link.strip()
        published = entry.get("published", "No date available")
        summary = clean_html(entry.get("summary", "No summary available"))
        
        print(f"\nEntry #{i}:")
        print("Title:", title)
        print("Link:", link)
        print("Published:", published)
        print("Summary:", summary)


rss_url = "https://www.cmjornal.pt/rss"
print_latest_entries(rss_url, count=10)
