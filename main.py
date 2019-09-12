from flask import Flask, request

app = Flask(__name__)
app.config['DEGUG'] = True

form = '''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action=/hello method="post">
        <label for="rot">Rotate by::</label>
        <input id="rot" type="text" name="rot" />
        <input id="text" type="textarea" name="text" placeholder="" />
        <input type="submit" value="Submit" />
      </form>
    </body>
</html>
view raw'''
@app.route('/')
def index():
    return form


@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'


if __name__ == '__main__':
    app.run()
