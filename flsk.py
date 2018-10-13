from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])  # yani kök dizinde ise index() fonksiyonunu çalıştır
def index():
    return ("asd") #index.html 'yi açar
    


if __name__ == "__main__": #main'de çalıştırılıyorsa 
    app.run(debug = True, host="0.0.0.0") #debug modunda programı çalıştırır (python app.py nin çalışmasını ve çalışır kalmasını sağlar)
