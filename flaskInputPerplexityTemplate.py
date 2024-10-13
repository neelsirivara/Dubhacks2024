from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

PERPLEXITY_API_KEY = os.environ.get('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')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.json['query']
        api_key = PERPLEXITY_API_KEY
        return jsonify({'query': query, 'api_key': api_key})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)