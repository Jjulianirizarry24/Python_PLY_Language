from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    # process user_input
    return ''

if __name__ == '__main__':
    app.run(debug=True)
