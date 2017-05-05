from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!, how are you? My name is Tom"
     for v in range (0,3):
            print(v)




if __name__ == "__main__":
    application.run()
    

