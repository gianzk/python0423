from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    print(name=request.args.get("name"))
    return render_template("greet.html")

@app.route("/demo")
def demo():
    return render_template("demo.html",name="hello word")


if __name__=="__main__":
    app.run()