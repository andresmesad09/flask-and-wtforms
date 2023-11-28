from flask import Flask, render_template
from form import MyForm
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    # which will be True if validation was successful after the user submitted the form
    # or False if it failed.
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.password.data
        if email == "admin@email.com" and pwd == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
