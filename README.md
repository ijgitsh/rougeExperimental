
# ROUGE Scoring API

This project is a Flask-based API that calculates ROUGE scores for evaluating the quality of text summaries.

## Requirements

Before running the application, ensure you have the required Python packages installed. You can install the necessary packages using `pip` and the provided `requirements.txt` file.

```text
flask
flask-cors
requests
rouge-score
```

## Installation

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/rouge-scoring-api.git
    cd rouge-scoring-api
    ```

2. Create a virtual environment and activate it (optional but recommended).

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application.

    ```bash
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### `POST /rouge`

Calculate the ROUGE scores for given reference and prediction texts.

#### Request

- **URL:** `/rouge`
- **Method:** `POST`
- **Headers:** `Content-Type: application/json`
- **Body:** JSON object containing `reference` and `prediction` strings.

    ```json
    {
      "reference": "The reference text",
      "prediction": "The predicted text"
    }
    ```

#### Response

Returns a JSON object containing the ROUGE scores.

    ```json
    {
      "rouge1": {
        "precision": 0.5,
        "recall": 0.5,
        "fmeasure": 0.5
      },
      "rouge2": {
        "precision": 0.4,
        "recall": 0.4,
        "fmeasure": 0.4
      },
      "rougeL": {
        "precision": 0.45,
        "recall": 0.45,
        "fmeasure": 0.45
      },
      "rougeLsum": {
        "precision": 0.45,
        "recall": 0.45,
        "fmeasure": 0.45
      }
    }
    ```

## Example

You can use `curl` to test the API.

```bash
curl -X POST http://127.0.0.1:5000/rouge -H "Content-Type: application/json" -d '{"reference": "The reference text", "prediction": "The predicted text"}'
```

## License

This project is licensed under the MIT License.
