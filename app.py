from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True)
    