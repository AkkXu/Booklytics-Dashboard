book_data = []

for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]

        book_data.append({
            'title': title,
            'price': price,
            'availability': availability,
            'rating': rating
        })

df = pd.DataFrame(book_data)
df.to_csv("books_all_pages.csv", index=False)
print(f"Scraped {len(df)} books and saved to books_all_pages.csv")