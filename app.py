from flask import Flask, jsonify, render_template
from fetch_twitter_trends import fetch_trending_topics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    result = fetch_trending_topics()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
