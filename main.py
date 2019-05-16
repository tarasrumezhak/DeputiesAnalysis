from flask import Flask, render_template, request, send_file
from visual import stats
# import webbrowser

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("mainpage.html")
    # line_chart.render_in_browser()

@app.route("/stats", methods=["GET", "POST"])
def build():
    chart = stats()
    return chart.render_response()

@app.route("/download")
def download():
    return send_file("info.txt", attachment_filename="data.txt", as_attachment=True)

@app.route("/deputy", methods=["GET", "POST"])
def data():
    if not request.form.get("input"):
        return render_template("failure.html")
    try:
        name = request.form.get("input")
        with open("info.txt", encoding="utf-8") as f:
            data = f.readlines()
        with open("photos.txt", encoding="utf-8") as f:
            photos = f.readlines()
        for i in data:
            if name.strip() in i:
                info = i.split(", ")
                # print(info)
                text = "Депутат {}, отримав з бюджету {} грн., бере участь у {} " \
                       "комітетах та організаціях, на засіданнях був присутнім {} " \
                       "раз та відсутнім {} раз, законопроектів - {} (схвалених {}), КОЕФІЦІЄНТ = {}".format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
        wiki = info[0].split()
        wiki_url = "_".join(wiki)
        for ph in photos:
            # print(name.strip(), ph)
            if name.strip() in ph:
                # print("hello")
                photo = "https://data.rada.gov.ua/ogd/mps/skl8/foto/{}.jpg".format(ph.split()[0])

        # webbrowser.open_new_tab(photo)
        return render_template("deputy.html", name=info[0], salary=info[1], coef=info[7], image=photo,
                               orgs=info[2], pres=info[3], absent=info[4], laws=info[5], accepted=info[6],
                               wiki=wiki_url)
    except:
        return render_template("failure.html")


if __name__ == "__main__":
    app.run(debug=True)
