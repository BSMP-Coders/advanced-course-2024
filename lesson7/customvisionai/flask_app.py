from flask import Flask, render_template, request
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()  # Ensure you have a .env file with your keys
prediction_key = os.getenv("CUSTOMVISIONAI_PREDICTION_KEY")
PRED_ENDPOINT = "https://bspm2023-prediction.cognitiveservices.azure.com/"
DEFAULT_PROJECT_ID = "208badc1-a218-4ba2-98ea-c5188c337fdf"
DEFAULT_MODEL_NAME = "Iteration1"

# Initialize the prediction client
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(PRED_ENDPOINT, prediction_credentials)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def classify_image():
    image_url = ""
    project_id = DEFAULT_PROJECT_ID
    model_name = DEFAULT_MODEL_NAME
    predictions_data = []

    if request.method == 'POST':
        image_url = request.form.get('image_url')
        project_id = request.form.get('project_id', DEFAULT_PROJECT_ID)
        model_name = request.form.get('model_name', DEFAULT_MODEL_NAME)

        if image_url:
            try:
                results = predictor.classify_image_url(project_id, model_name, url=image_url)
                predictions_data = [{"Tag": pred.tag_name, "Probability (%)": f"{pred.probability * 100:.2f}"} for pred in results.predictions]
            except Exception as e:
                predictions_data = [{"Error": str(e)}]

    return render_template('index.html', image_url=image_url, predictions_data=predictions_data, project_id=project_id, model_name=model_name)

if __name__ == '__main__':
    app.run(debug=True)
