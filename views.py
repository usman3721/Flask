from app import app
from flask import render_template
from datetime import datetime


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%m/%d/%Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    my_name= "Usman Hassan Osuoale Abu zayd " #creating an objects to be passed
    age=23
    skills=["Python","sklearn","ml algorithms","NLP"]
    friends={
        "me":22,
        "mubarok":34,
        "abdillahi":20,
        "hubeidat":18,
    }
    colors=("blue","yellow")
 
    
    class GitExperince:
        def __init__(self,name,description,url):
            self.name=name
            self.description=description
            self.url=url
        def pull(self):
            return f"Pulling repo {self.name}"
        def clone(self):
            return f"cloning the repo of {self.url}"
        
    def repeat(x,qty):
        return x*qty
    my_remotes=GitExperince(
    name="Usamn hassan Osuolale Abu zaydin",
    description="Falsk tutorila by jovian nash",
    url="http://github.com/usman/flask.git"
    
   
)
    date=datetime.utcnow()
    my_html="<h1> This is my html <h1/>"
    
    suspicious="<script> You got hacked </script>"
    return render_template("public/jinja.html", my_name=my_name,
                           age=age,
                           skills=skills,
                           friends=friends,
                           colors=colors,
                           GitExperince=GitExperince,
                           repeat=repeat,
                           my_remotes=my_remotes,
                           date=date,
                           my_html=my_html,
                           suspicious=suspicious)

@app.route("/about")
def about():
    return render_template("about/about.html")

