from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello world!</h1>

    <iframe src="https://www.youtube.com/embed/_-4pkJl3UwA" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(debug=True, use_reloader=True)
