from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print "request.form: ", request.form
        for x in request.form.getlist('animals[]'):
            print x
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
