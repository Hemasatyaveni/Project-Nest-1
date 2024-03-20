from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html') 

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/Categories')
def categories():
    return render_template('categories.html')

@app.route('/Fashion')
def fashion():
    return render_template('fashion.html')

@app.route('/Electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/Cosmetics')
def cosmetics():
    return render_template('cosmetics.html')

@app.route('/Footwear')
def footwear():
    return render_template('footwear.html')

@app.route('/Furniture')
def furniture():
    return render_template('furniture.html')

@app.route('/Grocery')
def grocery():
    return render_template('grocery.html')

@app.route('/Jewellary')
def jewellary():
    return render_template('jewellary.html')

if __name__ == '__main__' :
    app.run(debug=True)