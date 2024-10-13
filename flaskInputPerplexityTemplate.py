from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

PERPLEXITY_API_KEY = os.environ.get('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')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.json['query']
        
        client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")
        
        messages = [
            {
                "role": "system",
                "content": "You are an artificial intelligence assistant and you need to engage in a helpful, detailed, polite conversation with a user."
            },
            {
                "role": "user",
                "content": query
            }
        ]
        
        try:
            response = client.chat.completions.create(
                model="mistral-7b-instruct",
                messages=messages,
            )
            return jsonify({'result': response.choices[0].message.content})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)