from flask import Flask, render_template
from datetime import datetime

books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


app = Flask(__name__)


@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h, w):
    bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
    return f"<h1>身高:{h}cm 體重:{w}kg<br> BMI:{bmi}</h1>"


@app.route("/books")
@app.route("/books/id=<int:id>")
def get_books(id=None):
    try:
        if id == None:
            return render_template("books.html", books=books)

        return books[id]
        # return books[1]
        # return books
    except Exception as e:
        return f"書籍編號錯誤:{e}"


@app.route("/nowtime")
def now_time():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(time)
    return time


@app.route("/")
def index():
    time = now_time()
    return render_template("index.html", timeX=time, name="Muz")


app.run(debug=True)
