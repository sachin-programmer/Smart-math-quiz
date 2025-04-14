from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Load questions
with open("questions.json") as f:
    questions = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    question = random.choice(questions)
    return render_template('quiz.html', question=question)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    correct = data['selected'] == data['correct']
    return jsonify({"result": correct})

if __name__ == '_main_':
    print("App is starting...")  # Debug print
    app.run(debug=True)