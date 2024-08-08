from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
import dotenv  
# Load environment variables  
dotenv.load_dotenv()  # Put the keys and variables here (never put your real keys in the code)
prediction_key = os.getenv("CUSTOMVISIONAI_PREDICTION_KEY")  

# Replace with project id and published model name
#ENDPOINT = "https://bspm2023.cognitiveservices.azure.com/"
PRED_ENDPOINT = "https://bspm2023-prediction.cognitiveservices.azure.com/"
projectid = "208badc1-a218-4ba2-98ea-c5188c337fdf"
model_name = "Iteration1"


# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(PRED_ENDPOINT, prediction_credentials)

test_image_url = "https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3051392.png"
results = predictor.classify_image_url(projectid, model_name, url=test_image_url)
print("📌Results from a URL:")
# Display the results.
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))

# Now let's try with a local image
print("📌Results from a local image:")
with open("test/image.png", "rb") as image_contents:
    results = predictor.classify_image(projectid, "Iteration1", image_contents.read())
    #results = predictor.classify_image_url(projectid, "Iteration1", url="https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3051392.png")
    #print(results)

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))