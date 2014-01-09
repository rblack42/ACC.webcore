import json
from flask import render_template
from app import app

# Home page 

data = u"""{
    "nav": [
        {"name":"Fall 2013 Classes","link":"/classes"},
        {"name":"Quick Links","link":"/links"},
        {"name":"Office Location","link":"/office"},
        {"name":"About Me","link":"/about"},
        {"name":"How-To Notes","link":"/howto"},
        {"name":"Lecture Notes","link":"/lectures"}
    ]
}"""

nav = json.loads(data)['nav']
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
            title = "Roie Black's ACC Website",
            nav = nav
           )

@app.route('/classes')
def classes():
    return render_template("classes.html",
            title = "Fall 2013 Classes",
            nav = nav
           )

@app.route('/office')
def office():
    return render_template("classes.html",
            title = "Office Location",
            nav = nav
           )

@app.route('/about')
def about():
    return render_template("about.html",
            title = "About me",
            nav = nav
           )

