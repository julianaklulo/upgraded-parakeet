from flask import Flask, render_template, request

import sys
sys.path.append('back')

from catalog import list_marketplaces, list_categories, list_categories_of_marketplace, list_subcategories, add_marketplace


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marketplaces')
def marketplaces():
    marketplaces = list_marketplaces()
    return render_template('marketplaces.html', marketplaces=marketplaces)


@app.route('/create_marketplace')
def create_marketplace():
    categories = list_categories()
    return render_template('create_marketplace.html', categories=categories)


@app.route('/marketplace')
def marketplace():
    marketplace_name = request.args.get('marketplace_name')
    categories = [
        category for category in request.args.keys() if category != 'marketplace_name'
    ]
    add_marketplace(marketplace_name, categories)
    return render_template(
        'success_message.html',
        message="Marketplace created successfully!"
    )


@app.route('/<marketplace>/categories')
def categories(marketplace):
    categories = list_categories_of_marketplace(marketplace)
    return render_template(
        'categories.html',
        marketplace=marketplace,
        categories=categories
    )


@app.route('/<marketplace>/<category>/subcategories')
def subcategories(marketplace, category):
    subcategories = list_subcategories(category)
    return render_template(
        'subcategories.html',
        marketplace=marketplace,
        category=category,
        subcategories=subcategories
    )


app.run(debug=True)
