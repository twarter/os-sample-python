from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return " is Tom- how r u"
    print("hi")
#     for v in range (0,3):
 #           print(v)




if __name__ == "__main__":
    application.run()
    

