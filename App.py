from flask import Flask, render_template, request ,redirect ,url_for
from flask_pymongo import PyMongo



app = Flask(__name__)

#database config
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/',methods = ['POST', 'GET'])
def view():
  
   if request.method == 'POST':
      name=request.form["name"]
      lastname=request.form["lastname"]
      email=request.form["email"]
      jobtitle=request.form["jobtitle"]
      phone=request.form["phone"]
      company=request.form["company"]
      noofemply=request.form["noofemply"]
      country=request.form["country"]
      
      result = request.form
      if name and email and phone and request.method == "POST":
         res=mongo.db.user3.insert({'name':name,'email':email,'lastname':lastname,'jobtitle':jobtitle,'phone':phone,'company':company,'noofemployee':noofemply,'country':country})
         print(res)

      print(result)
     
      return redirect(url_for("getUser3"))

   else:
      
      return render_template('app.html')


@app.route('/get1')
def getUser3():
   arr=[]
   for doc in mongo.db.user3.find():
      print(doc)
      arr.append(doc)
   
   print("------------------------------")
   print(arr)

   return render_template('index3.html',arr=arr)
@app.route('/get')
def getUsers():
   arr=[]
   for doc in mongo.db.userss.find():
    print(doc)
    arr.append(doc)
   
   print("------------------------------")
   print(arr)
  
   return render_template('base.html')


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