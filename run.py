from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST']) 
def main():
    return render_template('home.html', icon="images/logo.jpg", html_sqr_logo='sqr_logo.html', html_article='article.html')
    
@app.route("/sqr_logo.html")
def sqr_logo():
    return render_template('sqr_logo.html', image_file="images/SQR_logo.jpg")

@app.route("/article.html")
def article():
    return render_template('article.html')

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8080)

