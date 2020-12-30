# Mission_to_Mars
Web Scraping and Documentation Databases


In this project, we will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

## Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. 


### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image 


### Mars Weather

* Visited the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page

### Mars Facts

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.



## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that will import your `scrape_mars.py` script and call the `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

- - - - 

## Notes

* Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Used Pymongo for CRUD applications for your database.

* Used Bootstrap to structure your HTML template.

Final Webpage Looks Like this:
![Images 1](Images/fig1.png)
![Images 2](Images/Fig2.png)
![Images 3](Images/Fig3.png)
![Images 4](Images/Fig4.png)

