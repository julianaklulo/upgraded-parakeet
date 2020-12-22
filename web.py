from flask import Flask

from catalog import list_marketplaces, list_categories, list_subcategories


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Olist Catalog</h1>
    <ol>
        <li><a href='/marketplaces'>List all marketplaces</a>
        <li><a href='/categories'>List marketplace's categories</a>
        <li><a href='/subcategories'>List category's subcategories</a>
    </ol>
    """

@app.route('/marketplaces')
def marketplaces():
    marketplaces = list_marketplaces()
    response = f"""
    <h1>Olist Catalog</h1>
    <h3>Marketplaces:</h3>
    <ol>
    """
    for marketplace in marketplaces:
        response += f"<li>{marketplace}</li>"
    response += """
    </ol>
    <a href='/'>Go Back</a> 
    """

    return response

@app.route('/categories')
def categories():
    categories = list_categories()
    response = f"""
    <h1>Olist Catalog</h1>
    <h3>Categories:</h3>
    <ol>
    """
    for category in categories:
        response += f"<li>{category}</li>"
    response += """
    </ol>
    <a href='/'>Go Back</a> 
    """

    return response

@app.route('/subcategories')
def subcategories():
    subcategories = list_subcategories()
    response = f"""
    <h1>Olist Catalog</h1>
    <h3>Subcategories:</h3>
    <ol>
    """
    for subcategory in subcategories:
        response += f"<li>{subcategory}</li>"
    response += """
    </ol>
    <a href='/'>Go Back</a> 
    """

    return response

app.run(debug=True)