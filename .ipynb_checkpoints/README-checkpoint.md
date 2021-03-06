# Web Scraping Challenge

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I needed to do:

### Step 1 - Scraping
Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of the scraping and analysis tasks. The following outlines what I need to scrape.
NASA Mars News
Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that I could reference later.

### JPL Mars Space Images - Featured Image
Visit the url for JPL Featured Space Image here.

Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

Make sure to find the image url to the full size .jpg image.

Make sure to save a complete url string for this image.

### Mars Facts
Visit the Mars Facts webpage here and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, Orbit Distance, Surface Temperature and Orbit Period.

Use Pandas to convert the data to a HTML table string.
Here's a snapshot of how the NASA Mars News, Featured Space Image and the Facts table look like:
![page](Images/landing_page.png)


### Mars Hemispheres
Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

I had to click each of the links to the hemispheres in order to find the image url to the full resolution image.

Then, I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Also, I used a Python dictionary to store the data using the keys img_url and title.

Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

These are screenshots of how Mars hemisperes images look like:
![page2](Images/mars_hemispheres.png)

## Step 2 - MongoDB and Flask Application
I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

I started by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

Next, I created a route called /scrape that will import your scrape_mars.py script and call your scrape function.

Stored the return value in Mongo as a Python dictionary.
Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

