from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
cluster = MongoClient("mongodb+srv://aravinth:aravinth@cluster0.riij8.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
login = db["login"]
collection = db["password"]
app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/',methods = ['GET', 'POST'])
def hello():
    if request.method=="POST":
        names = request.form["name"]
        password = request.form["password"]
       
        
        
        if names:
            
            detail = login.find({"name":names})
            for i in detail:
                a = i
                break
           
            p=bytes(a["password"],"utf-8")
                   
            print(p)
            check = bcrypt.check_password_hash(p, password)
            if not check:
                return "not match"
            return render_template("home.html",name=names)
        return "no detail"

    return render_template('index.html')
@app.route('/find',methods = ['POST'])
def add():
    if request.method=="POST":
        names = request.form["name"]
        password = request.form["password"]
        cname = request.form["name"]
        cpass = request.form["password"]
        isfind = collection.find({"name":names})
        s=""
        for i in isfind:
            s=i
            break

        if not s:
            d_cname=[]
            d_cpass=[]
            d_cname.append(cname)
            d_cpass.append(cpass)
            collection.insert_one({"name":names,"cname":d_cname,"cpass":d_cpass})
            return "inserted"
        return"ddd"




if __name__ == "__main__":
    app.run(debug=True)
