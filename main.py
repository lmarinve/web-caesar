from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEGUG'] = True

form = '''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 440px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 400px;
                height: 150px;
                padding: 12px 20px;
                box-sizing: border-box;
                border: 2px solid #ccc;
                border-radius: 4px;
                background-color: #f8f8f8;
                font-size: 16px;
                resize: none;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action=/ method="post">
        <div>
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0" />
        </div>
        <textarea name="text" placeholder="{0}" rows="3" cols="35"></textarea>
        <input type="submit" value="Submit" />
      </form>
    </body>
</html>
'''


@app.route('/')
def index():
    return form.format("enter text here")


@app.route('/', methods=['POST'])
def encrypt():
    rec_rot = int(request.form['rot'])
    rec_text = request.form['text']
    rotated = rotate_string(rec_text, rec_rot)
    return form.format(rotated)


if __name__ == '__main__':
    app.run()
