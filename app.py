from flask import Flask, render_template, request, jsonify
from AI_pm import generate_reponse_ia

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '')
    response = generate_reponse_ia(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)