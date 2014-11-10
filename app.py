from flask import Flask, render_template, request

import hello

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print "request.form: ", request.form
        for x in request.form.getlist('animals[]'):
            print x
    return render_template("index.html")


app.route('/hello')(hello.hello)
hello.logger.handlers = app.logger.handlers


# The following demonstrates how ``add_url_rule`` (and ``route``) can be
# bypassed; the following are (essentially) equivalent.

app.route("/a", endpoint="a", methods=['GET'])(lambda: "a")

app.add_url_rule("/b", endpoint="b", methods=['GET'])
app.endpoint("b")(lambda: "b")

app.url_map.add(app.url_rule_class("/c", endpoint="c", methods=['GET']))
app.view_functions["c"] = lambda: "c"


if __name__ == "__main__":
    app.run(debug=True, port=4000)
