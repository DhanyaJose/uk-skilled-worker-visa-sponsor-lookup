import os
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load CSV into memory on startup
CSV_PATH = os.path.join(
    os.path.dirname(__file__),
    "sponsors.csv",
)
df = pd.read_csv(CSV_PATH)
df["Organisation Name"] = df["Organisation Name"].str.strip()
df["Town/City"] = df["Town/City"].fillna("").str.strip()
df["Type & Rating"] = df["Type & Rating"].fillna("").str.strip()
df["Route"] = df["Route"].fillna("").str.strip()

# Pre-compute lowercase names for fast searching
df["_name_lower"] = df["Organisation Name"].str.lower()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/search")
def search():
    query = request.args.get("q", "").strip()
    if len(query) < 3:
        return jsonify({"results": [], "total": 0})

    mask = df["_name_lower"].str.contains(query.lower(), na=False)
    matches = df.loc[mask, ["Organisation Name", "Town/City", "Type & Rating", "Route"]]
    total = len(matches)
    results = matches.head(50).to_dict(orient="records")

    return jsonify({"results": results, "total": total})


if __name__ == "__main__":
    app.run(debug=True)
