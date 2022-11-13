from flask import Flask, render_template
from app import app
@app.route('/')
def demo():  # put application's code here
    return render_template("demo.html")


@app.route('/demo1')
def demo1():  # put application's code here
    return render_template("demo1.html")


@app.route('/demo2')
def demo2():  # put application's code here
    return render_template("demo2.html")


if __name__ == '__main__':
    app.run()