import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import torch
from voice_gender_classifier.model import ECAPA_gender

# Load the pretrained model from Hugging Face
model = ECAPA_gender.from_pretrained("JaesungHuh/voice-gender-classifier")
model.eval()

# Move model to appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_gender(audio_path):
    """
    Predicts the gender from the given audio file.

    Parameters:
    - audio_path (str): Path to the audio file.

    Returns:
    - str: Predicted gender ('Male' or 'Female').
    """
    with torch.no_grad():
        output = model.predict(audio_path, device=device)
    return output
