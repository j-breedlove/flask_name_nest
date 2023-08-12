import datetime as dt
import json
import random

import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Route for the home page.
    Displays a random number between 1 and 10, and the current year.
    """
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year

    # Handling the form submission
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(f'/guess/{name}')

    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    """
    Route to guess the gender and age based on a name.
    Uses external APIs to fetch the gender and age estimates.
    """
    # Using genderize.io API to predict gender based on name
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender = gender_response.json()

    # Using agify.io API to predict age based on name
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age = age_response.json()

    return render_template('guess.html', name=name.title(), gender=gender['gender'], age=age['age'])


@app.route('/blog')
def get_blog():
    """
    Route for displaying blog posts.
    Reads data from the project root directory's JSON file.
    """
    # Reading blog data from root JSON file
    with open('blog_posts.json', 'r') as file:
        all_posts = json.load(file)

    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run()
