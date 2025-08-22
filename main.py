from flask import Flask
from datetime import datetime

app=Flask(__name__)

@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h,w):
    bmi=round(eval(w)/(eval(h)/100)**2,2)
    return f"<h1>身高:{h}cm 體重:{w}kg<br> BMI:{bmi}</h1>"

@app.route("/books")
@app.route("/books/id=<int:id>")
def get_books(id=None):
    try:
        books={1:"Python book",2:"Java book",3:"Flask book"}

        if id==None:
            return books
    
        return books[id]
        #return books[1]
        #return books
    except Exception as e :
        return f"書籍編號錯誤:{e}"

@app.route("/nowtime")
def now_time():
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(time)
    return time


@app.route("/")
def index():
    return "<h1>Hello MuzQ !<h1>"

app.run(debug=True)