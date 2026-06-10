# E-commerce Pricing Intelligence & Product Analysis

## Project Overview

This project simulates an e-commerce pricing intelligence system by collecting, monitoring, and analyzing product-level data from an online bookstore marketplace using Python.

The system scrapes product details including **title, price, rating, availability, and product URL** for **1,000+ books across 50 pages** and performs exploratory data analysis (EDA) to understand pricing patterns and product positioning.

Additionally, a price monitoring workflow was developed to compare current prices with historical data and trigger automated email alerts for significant price drops.

---

## Business Problem

In e-commerce marketplaces, sellers continuously compete on pricing, product quality, and availability to attract customers. Manually tracking competitor prices across hundreds of products is inefficient and time-consuming.

This project demonstrates how pricing intelligence can help businesses:

* Monitor competitor pricing trends
* Identify premium and budget product segments
* Analyze product quality through ratings
* Detect meaningful price drops for pricing decisions

---

## Project Objectives

* Scrape product-level data from an e-commerce marketplace
* Perform exploratory data analysis (EDA) on pricing and ratings
* Simulate historical pricing data for trend analysis
* Monitor product price fluctuations over time
* Trigger automated email alerts for significant price drops (**≥10%**)

---

## Dataset Information

The dataset contains:

* **Title** – Product name
* **Price** – Product price (£)
* **Rating** – Product rating (1–5 stars)
* **Availability** – Stock availability status
* **Book URL** – Product page link
* **Date** – Historical date for price tracking

**Total products analyzed:** 1,000+ books

---

## Technologies Used

* Python
* Pandas
* BeautifulSoup
* Requests
* Matplotlib
* SMTP (Email Automation)
* Jupyter Notebook

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

### 1. Price Distribution

Analyzed product pricing distribution to identify budget, mid-range, and premium pricing segments.

### 2. Rating Distribution

Examined rating frequency to understand product quality distribution.

### 3. Average Price by Rating

Evaluated whether highly rated products command premium pricing.

### 4. Top 10 Most Expensive Products

Identified premium-priced books for competitor benchmarking.

### 5. Price vs Rating Analysis

Explored the relationship between pricing and ratings.

### 6. Historical Price Trend Analysis

Simulated historical pricing trends to monitor competitor price changes over time.

---

## Price Monitoring & Email Alert System

A price monitoring workflow was developed to compare current product prices with historical prices.

To avoid unnecessary notifications from minor fluctuations, email alerts are triggered **only when the product price decreases by 10% or more**.

### Workflow

1. Scrape latest product prices
2. Compare with historical pricing data
3. Calculate percentage price drop
4. Trigger email alert if price drop ≥10%

Example logic:

```python
if price_drop_percent >= 10:
    send_email()
```

---

## Key Insights

* Product prices were distributed across budget, mid-range, and premium segments.
* Mean (£34.87) and median (£35.83) prices were closely aligned, indicating balanced marketplace pricing with minimal skew.
* Historical price simulation demonstrated how businesses can monitor competitor pricing behavior over time.
* A 10% threshold reduced unnecessary alerts and focused on meaningful pricing changes.

---

## Project Structure

```plaintext
ecommerce-price-intelligence/
│
├── data/
│   ├── books_full_data.csv
│   └── price_history.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── images/
│
├── scraper.py
├── email_alert.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Improvements

* Build an interactive dashboard using Tableau or Power BI
* Automate daily scraping using scheduling tools
* Track pricing trends across multiple e-commerce platforms
* Add customer review sentiment analysis

---

## Author

**Aishwarya**
