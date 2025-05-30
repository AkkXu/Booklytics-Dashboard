**Booklytics Dashboard**

This project demonstrates a complete end-to-end data workflow, from scraping and preprocessing synthetic book data to building an interactive dashboard using Plotly Dash.

The dataset is sourced from books.toscrape.com, a website designed for practicing web scraping. While the data itself is artificial, the skills applied in this project are highly relevant for real-world analytics and dashboard development.

<br><br>
<br><br>
Project Structure

1.books_all_pages.csv: Final dataset after web scraping and preprocessing

2.books_scraper.py: Python script using BeautifulSoup to scrape book data from all 50 pages

3.eda_analysis.ipynb: Jupyter Notebook performing EDA using Pandas, Seaborn, and Matplotlib

4.books_dash.py: Main interactive dashboard built with Dash and Plotly

<br><br>

Tools & Technologies

- Python (Pandas, NumPy, BeautifulSoup)

- Data Visualization: Seaborn, Matplotlib, Plotly

- Dashboarding: Dash (with dropdowns, sliders, and interactive graphs)

<br><br>

Key Features

- Web Scraping: Scraped book title, price, rating, availability, and whether the book is part of a series.

- Feature Engineering: Cleaned and transformed data, created new binary and categorical features.

- EDA: Explored distribution and relationships between price, rating, availability, and other features.

<br><br>

Interactive Dashboard:

- Selectable visualizations (boxplots by rating, availability, etc.)

- Price slider to filter books and view scatter plot between price & rating

<br><br>

Insights

1. No strong correlation between book price and rating

2. High-rated books appear across various price points

3. Series books do not consistently yield higher prices or ratings

**Note:** The dataset is synthetic. Insights derived here should not be used for actual business decisions.

<br><br>
**How to Start**
1. Clone this repo:
2. Install required packages:
3. Start the dashboard
4. Open your browser and go to: http://127.0.0.1:8050
