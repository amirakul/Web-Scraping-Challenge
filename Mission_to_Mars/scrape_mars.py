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
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest news: title & paragraph
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").get_text()

    # Get the featured image from second url JPL Mars Space Images
    url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Retrieve page with the requests module
    browser.visit(url1)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    carousel=soup.find('article', class_='carousel_item')
    image_path = carousel["style"]
    split_text=image_path.split("'")
    featured_image_url= "https://www.jpl.nasa.gov/" + split_text[1]

    #Get Mars Facts table from the 2nd url
    url2 = 'https://space-facts.com/mars/'
    browser.visit(url2)
    tables = pd.read_html(url2)
    df = tables[0]
    df.columns = ['Criteria', 'Measurements']
    df.set_index('Criteria', inplace=True)
    html_table = df.to_html(table_id='scrape_table')


    # Get hemisphere images, visit third url USGS website
    url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the titles of the hemispheres
    # hem_titles=soup.find_all('h3')

    # Initialize hemisphere data list
    hem_url = []
    links = browser.find_by_css('a.product-item h3')
    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css('a.product-item h3')[i].click()
        element = browser.links.find_by_text('Sample').first
        hemisphere["image_url"] = element["href"]
        hemisphere["title"] = browser.find_by_css("h2.title").text
        hem_url.append(hemisphere)
        browser.back()



    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hem_url": hem_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data