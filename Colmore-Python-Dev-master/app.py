from flask import Flask,render_template, request, session, redirect
from flask.templating import render_template_string
from flask_session import Session
from symbolsearch import symbol_search, ticker_search

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template("login.html")


@app.route('/log_in', methods=["POST"])
def log_in():
    session["api_key"] = request.form.get("api_key")
    if not session["api_key"]:
        return redirect("/")
    return render_template("search.html")
    # return render_template("search.html")

@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        api_key = request.form.get("api_key")
        company_name = request.form.get("company_name")
    list1 = symbol_search(company_name, api_key)
    return render_template("search_results.html", list1 = list1)

@app.route("/more_info", methods=["POST"])
def more_info():
    
    ticker = request.form.get("ticker")
    return ticker_search(ticker, session["api_key"])

if __name__ == "__main__":
    app.run(debug=True, port=8001, use_reloader = True)