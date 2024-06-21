from rouge_score import rouge_scorer
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import config
from collections import namedtuple

from flask import Flask, request, jsonify
from collections import namedtuple
from rouge_score import rouge_scorer

app = Flask(__name__)
CORS(app) 
# Named tuple for Score
Score = namedtuple('Score', ['precision', 'recall', 'fmeasure'])

def score_to_dict(score):
    return {
        'precision': score.precision,
        'recall': score.recall,
        'fmeasure': score.fmeasure
    }

@app.route('/rouge', methods=['POST'])
def get_prompts():
    data = request.get_json()
    print(f"Received data: {data}")  # Log received data
    reference = data.get('reference', '')
    prediction = data.get('prediction', '')

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)
    scores = scorer.score(reference, prediction)
    print(f"Calculated scores: {scores}")  # Log calculated scores

    rouge_scores_dict = {key: score_to_dict(value) for key, value in scores.items()}
    print(f"ROUGE scores dict: {rouge_scores_dict}")  # Log the scores dictionary
    return jsonify(rouge_scores_dict)

if __name__ == '__main__':
    app.run(debug=True)
