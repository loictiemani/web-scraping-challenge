from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
db = mongo.db
collection = db['mars_data']

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_info = list(collection.find())
    #print (mars_info)
    return render_template("index.html", mars_info=mars_info)




@app.route("/scrape")
def scrape():
     # Run the scrape function  
    # Update the Mongo database using update and upsert=True
    collection.insert_many(scrape_mars.mars_news())
    collection.insert_many(
            [
                {'featured_img_full':
                scrape_mars.JPL_image()}
            ]
            )
    collection.insert_many(scrape_mars.Mars_Facts())
    #collection.insert_many(scrape_mars.Mars_Hemispheres())
    # Redirect back to home page"""
    return redirect("/")

@app.route("/clear_data")
def clear_data():  
    collection.delete_many({})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)