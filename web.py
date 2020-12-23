from flask import Flask, render_template

from catalog import list_marketplaces, list_categories, list_subcategories


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplaces')
def marketplaces():
    marketplaces = list_marketplaces()
    return render_template('marketplaces.html', marketplaces=marketplaces)

@app.route('/categories')
def categories():
    categories = list_categories()
    return render_template('categories.html', categories=categories)

@app.route('/subcategories')
def subcategories():
    subcategories = list_subcategories()
    return render_template('subcategories.html', subcategories=subcategories)

app.run(debug=True)