from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to my first deployed web server based on python, mysql, php. This is just the beginning of somthing reallllllllyyyyy BIG. :-) --> Created by Shurik<--"
if __name__ == "__main__":
    app.run()
