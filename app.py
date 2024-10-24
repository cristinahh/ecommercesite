from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/myaccount')  #when this path is accessed, show whatever is after return
def myaccount():
  return render_template('myaccount.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #starts the app on hose 0.0.0.0