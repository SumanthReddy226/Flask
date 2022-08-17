from flask import Flask,render_template,request,redirect

app = Flask(__name__)


Dict = {}
@app.route("/",methods=["GET","POST"])
def login():
    user = request.form.get("uname")
    passw = request.form.get("passw")
    if request.method == "POST":
        Dict.update({user:passw})
        return render_template("success.html",user=user,passw=passw,Dict=Dict)
    else:
        return render_template("login.html",user=user,passw=passw)


@app.route("/search",methods=["GET","POST"])
def search():
    user = request.form.get("uname")
    passw = request.form.get("passw")
    search = request.form.get("s1")
    return render_template("result.html",user=user,Dict=Dict,passw=passw,search=search)

@app.route("/back")
def back():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True,port="5001")