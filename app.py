from flask import Flask, render_template, redirect, url_for

app = Flask(name)

@app.route('/')
def asosiy_menyu():
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    return "Tovar muvaffaqiyatli aformit qilindi!"

if name == 'main':
    app.run(debug=True)