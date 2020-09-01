from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visit mars.nasa.gov/news to get recent news title and paragraph
    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest news: title & paragraph
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text

    # Get the featured image from second url JPL Mars Space Images
    url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Retrieve page with the requests module
    browser.visit(url1)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    carousel=soup.find('article', class_='carousel_item')
    image_path = carousel["style"]
    split_text=image_path.split(" ' ")
    featured_image_url= url1 + split_text[1]

    #Get Mars Facts table from the 2nd url
    url2 = 'https://space-facts.com/mars/'
    browser.visit(url2)
    tables = pd.read_html(url2)
    df = tables[0]
    df.columns = ['Criteria', 'Measurements']
    df=df.set_index('Criteria', inplace=True)
    mars_table = df.to_html(table_id='mars_info_table')

    # Get hemisphere images, visit third url USGS website
    url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # Set up an empty dictionary and start a loop
    hem_image_url=[]
    all_hem_titles=soup.find_all('h3')
    for i in range(len(all_hem_titles)):
        hem_title=all_hem_titles[i].text
        image_url=soup.find('img', class_='thumb')['src']
        image_path=url3+image_url

    # Store data in a dictionary
    hem_dict = {
        "title": hem_title,
        "image_url": image_path
    }
    hem_image_url.append(hem_dict)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_url": featured_image_url,
        "mars_table": mars_table,
        "hem_image_url": hem_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data