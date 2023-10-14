from flask import Flask, render_template,request, render_template_string,redirect,url_for

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if (request.method == "POST"):
        message = request.form["echo"]
        return redirect(url_for('echo', result=message))
    else:
        return render_template("index.html")

@app.route("/echo",methods=["GET"])
def echo():
    result = request.args.get("result")
    template = '''
        {}
    '''.format(result)
    return render_template_string(template)
if __name__ == "__main__":    
    app.run(debug=False,host='0.0.0.0',port="5000")
    