import streamlit as st
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

# Streamlit app
st.title("Image Classification with Azure Custom Vision")
st.write("Provide an image URL to get classification predictions.")

# Input fields
col1, col2, col3 = st.columns(3)
image_url = col1.text_input("Image URL", "")
project_id = col2.text_input("Project ID", DEFAULT_PROJECT_ID)
model_name = col3.text_input("Model Name", DEFAULT_MODEL_NAME)
st.caption("Example image URL for soccer player: [image link](https://www.bing.com/th?id=OIP.sHCieQnQ04qXxIzZ-AfSFwHaE8&w=204&h=150&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2)")
# Function to display results
def display_results(results):
    col1, col2 = st.columns(2)
    with col1:
        st.image(image_url, caption="Input Image", use_column_width=True)
    with col2:
        st.subheader("Predictions")
        predictions_data = [{"Tag": pred.tag_name, "Probability (%)": f"{pred.probability * 100:.2f}"} for pred in results.predictions]
        st.table(predictions_data)

# Predict button
if st.button("Classify Image"):
    if image_url:
        try:
            results = predictor.classify_image_url(project_id, model_name, url=image_url)
            display_results(results)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid image URL.")

# Option to add another image
#st.write("Would you like to classify another image?")
#if st.button("Add Another Image"):
#    st.experimental_rerun()
