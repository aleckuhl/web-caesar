from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

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
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label>Rotate by:</label>
        <input type="text" name="rot" value="0"></input>
        <textarea type="text" name="text">{0}</textarea>
        <button type="submit" value="Submit">Submit</button>
      </form>
      
    </body>
</html>
"""
@app.route("/", methods = ['POST'])
def rotate():
    rot = int(request.form['rot'])
    text = request.form['text']
    rotated = encrypt(text,rot) 
    return form.format(rotated)

@app.route("/")
def index():
    return form.format("")

app.run()