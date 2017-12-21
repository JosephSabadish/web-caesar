from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!doctype html>
<html>
    <head>
        <style>
           form {{
               background-color: #eee;
               padding: 20px;
               margin: 0 auto;
               width: 540px;
               font: 16px sans-serif;
               border-radius: 10px;
            }}
            textarea {{           margin: 10px 0;
                width: 540 px;
                height: 120px;
            }}
         </style>
      </head>
      <body>
        <form action="/" method= "post">
        <label for= "rot">"Rotate amount:</label>
        <input value = 0 type= "text" name = "rot">
        <textarea name = "text">{0}</textarea> 
        <input type= "submit" name= "Submit Query"/>
        </form>
        </body>
 </html> 
 """                



@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST', 'GET'])
def encrypt():
    rot=int(request.form["rot"])
    text= request.form["text"]
    rotate = rotate_string(text,rot)
    return form.format(rotate)
app.run()