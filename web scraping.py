import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Lists to store data
Names = []
Prices = []
Descs = []
Reviews = []


# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Loop through multiple pages
for i in range(1, 50):
    url = f"https://www.flipkart.com/search?q=Head+phones+under+50000&page={i}"
    r = requests.get(url, headers=headers)
    print(f"Status Code for Page {i}:", r.status_code)

    soup = BeautifulSoup(r.text, 'lxml')

    # Find the box containing all products
    Box = soup.find('div', class_="DOjaWF gdgoEp")
    if not Box:
        print("Box not found on page", i)
        continue

    # Find individual product containers
    products = Box.find_all('div', class_="_75nlfW")

    for product in products:
        # Name
        name_tag = product.find('a', class_="wjcEIp")
        name = name_tag.text.strip() if name_tag else ""
        Names.append(name)

        # Price
        price_tag = product.find('div', class_="Nx9bqj")
        price = price_tag.text.strip() if price_tag else ""
        Prices.append(price)

        # Description
        desc_tag = product.find('span', class_="Wphh3N")
        desc = desc_tag.text.strip() if desc_tag else ""
        Descs.append(desc)

        # Reviews
        review_tag = product.find('div', class_="XQDdHH")
        review = review_tag.text.strip() if review_tag else ""
        Reviews.append(review)

      
  


    # Delay between requests to avoid being blocked
    time.sleep(2)

# Create DataFrame
df = pd.DataFrame({
    "Product Name": Names,
    "Product Price": Prices,
    "Product Description": Descs,
    "Product Reviews": Reviews,
    
})

# Display the DataFrame
df.to_csv(r'C:\Users\MERLIN\OneDrive\Documents\pro.csv', index=False)


