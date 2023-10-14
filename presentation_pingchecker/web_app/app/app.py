from flask import Flask, render_template,send_from_directory,request
import subprocess
from urllib import parse

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/robots.txt",methods=["GET"])
def robot():
    return send_from_directory("static", "robots.txt")

@app.route("/rce_easy",methods=["GET","POST"])
def rce_easy():
    if (request.method == "POST"):
        ip_address = request.form["ip"]
        result= os_execution(ip_address)
        return render_template("rce.html",result=result)
    return render_template("rce.html")

@app.route("/rce_medium",methods=["GET","POST"])
def rce_medium():
    if (request.method == "POST"):
        command_operators = [";","\n","&","|","&&","||","``","$()"," "]
        raw_data = request.get_data().decode("utf-8").split("ip=")[1]
        for operators in command_operators:
            if operators in raw_data:
                caught = "Blacklisted character!"
                return render_template("rce_medium.html",result=caught)
        url_decoded = parse.unquote(raw_data)
        blacklisted_v2 = [";","\n","&","&&","``","$()"]
        for operators in blacklisted_v2:
            if operators in url_decoded:
                caught = F"{operators} not allowed"
                return render_template("rce_medium.html",result=caught)
        if "cat" in url_decoded:
            caught = "command not allowed"
            return render_template("rce_medium.html",result=caught)
        result = os_execution(url_decoded)
        return render_template("rce_medium.html",result=result)
    return render_template("rce_medium.html")    

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"),404

def os_execution(ip_address):
    result= subprocess.Popen(f"ping -i 1 -c 1 {ip_address}",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = result.communicate()
   
    if (output):
        #print(result)
        result = output.decode()
        #print("Afte decoded")
        #print(result)
    else:
        #print(result)
        result = errors.decode()
        #print(result)
    return result
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="5000")
    

