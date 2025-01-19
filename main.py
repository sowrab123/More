from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_html_source(url):
    """Fetch HTML source code from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch page. Status code: {response.status_code}")

def extract_book_data(html):
    """Extract book details (name, writer, and price) from the HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    book_data = []
    
    # Locate book items in the HTML (specific to http://books.toscrape.com)
    books = soup.select('.product_pod')  # Adjust selector for other websites
    
    for book in books:
        try:
            name = book.select_one('h3 a').get('title')
            price = book.select_one('.price_color').text.strip()
            # Since this site doesn’t include writer info, add a placeholder
            writer = "Unknown"  # Replace with appropriate selector for other sites
            
            book_data.append({
                'Book Name': name,
                'Writer Name': writer,
                'Price': price,
            })
        except AttributeError:
            continue
    
    return book_data

def save_to_csv(data, filename):
    """Save extracted data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Example site URL
    url = "http://books.toscrape.com"
    
    try:
        print("Fetching HTML...")
        html = get_html_source(url)
        
        print("Extracting data...")
        data = extract_book_data(html)
        
        if data:
            print(f"Extracted {len(data)} items. Saving to CSV...")
            save_to_csv(data, "books_data.csv")
        else:
            print("No data extracted. Check the website structure or selectors.")
    except Exception as e:
        print(f"An error occurred: {e}")
