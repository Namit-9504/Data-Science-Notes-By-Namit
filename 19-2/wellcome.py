from flask import Flask
app = Flask(__name__)
@app.route("/wellcome")
def wellcome():
    return "Wellcome to ABC Corporation"
@app.route("/")
def details():
    return "Company Name = ABC Corporation /n Location = India /n Contact Deatils = 999-999-999"
if __name__ == "__main__":
    app.run(host="0.0.0.0")