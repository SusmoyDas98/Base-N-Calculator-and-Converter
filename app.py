from flask import Flask, redirect, request, url_for, render_template
import json

app = Flask(__name__)

with open("config.json","r") as c:
    params = json.load(c)['params']

@app.route("/")

def home():


    return render_template('index.html', params = params)

@app.route("/calculator")

def calculator():
    bases = list(range(2,37))
    operations = {"add":"+", "sub":"-", "mul":"×", "div":"÷"}

    return render_template('calculator.html',  bases = bases, operations = operations ,  params = params)

@app.route("/converter")

def converter():
    bases = list(range(2,37))    
    return render_template('converter.html',  bases = bases , params = params)



if __name__ == '__main__':
    app.run(debug = True)