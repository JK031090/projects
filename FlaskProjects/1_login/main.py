from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup" , methods=['GET','POST'])
def users():
    if request.method == 'POST':
        req = request.form
        print(req)

        return redirect(request.url)


    return render_template('users.html')
if __name__ == '__main__':
    app.run(debug = True)