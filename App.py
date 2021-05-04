from flask import Flask, render_template, request ,redirect ,url_for
from flask_pymongo import PyMongo



app = Flask(__name__)

#database config
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def getUsers():
   arr=[]
   for doc in mongo.db.userss.find():
    print(doc)
    arr.append(doc)
   
   print("------------------------------")
   print(arr)
  
   return render_template('index.html',arr=arr)


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      Username=request.form["Username"]
      email=request.form["email"]
      password=request.form["password"]
      result = request.form
      if Username and email and password and request.method == "POST":
         res=mongo.db.userss.insert({'name':Username,'email':email,'password':password})
         print(res)

      print(result)
      print(Username)
      return redirect(url_for("getUsers"))
   if request.method == 'GET':
       return render_template("index1.html")

if __name__ == '__main__':
   app.run(debug = True)