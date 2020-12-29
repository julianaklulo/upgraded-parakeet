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

@app.route('/<marketplace>/categories')
def categories(marketplace):
    categories = list_categories(marketplace)
    return render_template('categories.html', marketplace=marketplace, categories=categories)

@app.route('/<category>/subcategories')
def subcategories(category):
    subcategories = list_subcategories(category)
    return render_template('subcategories.html', category=category, subcategories=subcategories)

app.run(debug=True)