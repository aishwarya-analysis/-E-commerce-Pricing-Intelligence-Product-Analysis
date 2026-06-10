import pandas as pd
import random
from datetime import datetime, timedelta


# Read csv
books_df = pd.read_csv("/Users/aishutheanalyst/Downloads/books_full_data.csv")

#keep only needed columns
df =df[["Title","Price"]]

#create empty list to store historical records
price_history=[]

#number of historical days
days=7

#loop through each book
for _,row in df.iterrows():

    
    # Get book title
    title = row["Title"]


    #get current price
    base_price= float(row["Price"])

    # Set starting price
    current_price = base_price

    #create 7 days of history
    for i in range(days):

    #Generate date
    #today minus i days
        date=(datetime.today()-timedelta(days=i)).date()
        
    #create random price variation
   # Small gradual daily change
        price_change = random.uniform(
            -1.5,
            1.5
        )


    # Update previous day's price
        current_price = (
            current_price
            + price_change
        )


    # Round price
        new_price = round(
            current_price,
            2
        )


    # Prevent negative price
        new_price = max(
            new_price,
            5
        )


    # Save record
        price_history.append(
            [
                date,
                title,
                new_price
            ]
        )

    # Convert list to dataframe
history_df = pd.DataFrame(price_history,
    columns=[
        "Date",
        "Title",
        "Price"
       ]
 )

    # Save as CSV
history_df.to_csv("price_history.csv",index=False)


       
    # Print success message
print("Price history created!") 

          


