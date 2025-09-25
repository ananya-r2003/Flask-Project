from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('netflix_exploded.csv')
    top_directors = df['director'].value_counts().head(10)
    top_countries = df['country'].value_counts().head(10)
    directors = list(top_directors.items())
    countries = list(top_countries.items())
    return render_template('index.html', directors=directors, countries=countries)

if __name__ == "__main__":
    app.run(debug=True)