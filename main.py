from flask import Flask, render_template, url_for

app = Flask(__name__)

data = {
    "paris": {
        "description": "Romantizmin ve sanatın şehri, Eyfel Kulesi'nin evi.",
        "image": "paris.jpg"
    },
    "tokyo": {
        "description": "Gelenek ve teknolojinin buluştuğu dinamik metropol.",
        "image": "tokyo.jpg"
    },
    "new york": {
        "description": "Hiç uyumayan şehir, özgürlük ve fırsatların merkezi.",
        "image": "nyc.jpg"
    },
    "istanbul": {
        "description": "Doğu ve Batı’nın birleştiği tarihi ve büyüleyici şehir.",
        "image": "istanbul.jpg"
    }
}

@app.route("/search")
def search():
    return render_template("search.html", cities=data)

if __name__ == "__main__":
    app.run(debug=True)
