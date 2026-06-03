from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    percentage = None

    if request.method == 'POST':
        total = int(request.form['total'])
        attended = int(request.form['attended'])
        percentage = (attended / total) * 100

    return render_template('index.html', percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)