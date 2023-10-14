from flask import Flask, render_template,send_file, request, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    elif (request.method == "POST"):
        message = request.form.get("file_name","static/images.png")
        return redirect(url_for('view_image', file_name=message))

@app.route("/view_image",methods=["GET"])
def view_image():
    file_name = request.args.get('file_name')
    try:
        return send_file(file_name)
    except:
        return "File does not exist",404
if __name__ == "__main__":    
    app.run(debug=False,host='0.0.0.0',port="5000")