all_books = []

for page in range(1, 51):

    print(f"Scraping Page {page}...")

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    #print(f"\nPage {page}")
    for book in books:
        
        title = book.h3.a["title"]
        print(title)

        price = book.find("p",class_="price_color").text.strip()[1:]
        print(price)
        availability = book.find("p",class_="instock availability").text.strip()
        print(availability)
        rating = book.find("p",class_="star-rating")["class"][1]
        print(rating)
        book_link = ("https://books.toscrape.com/catalogue/"+ book.h3.a["href"])
        print(book_link)
        
        all_books.append([title,price,availability,rating,book_link])
        
        file_path = "/Users/analyst/Downloads/books_full_data.csv"
        
        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:
        
            writer = csv.writer(f)
        
            writer.writerow([
                "Title",
                "Price",
                "Availability",
                "Rating",
                "Book_link"
            ])
        
            writer.writerows(all_books)
        
        print("Data saved successfully!")
        print(file_path)
                


        

       

   
