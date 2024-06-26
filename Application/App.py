import nltk
import torch
import librosa
import evaluate
import soundfile as sf
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from flask import Flask, render_template, request, flash, redirect

nltk.download('punkt')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def Correction(input_text: str):
    """
    Returns the input text with correction

    Args:
        input_text (str): Original text generated by the model
    """
    sentence = nltk.sent_tokenize(input_text)
    return " ".join([s.replace(s[0], s[0].capitalize(), 1) for s in sentence])

def transcribe(input_file):
    """
    Returns the transcribed text of the audio

    Args:
        input_file (_type_): _description_
    """
    tokenizer = Wav2Vec2Tokenizer.from_pretrained('facebook/wav2vec2-base-960h')
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    speech, sample_rate = sf.read(input_file)

    if len(speech.shape) > 1:
        speech = speech[:, 0] + speech[:, 1]

    if sample_rate != 16000:
        speech = librosa.resample(speech, orig_sr=sample_rate, target_sr=16000)

    input_values = tokenizer(speech, return_tensors="pt").input_values
    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)

    transcription = tokenizer.decode(predicted_ids[0])

    transcription = Correction(transcription.lower())
    return transcription

@app.route('/', methods=['GET', 'POST'])
def index():
    durl = '#'
    transcription = None

    if request.method == 'POST':
        if 'audioFile' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['audioFile']

        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        if file:
            transcription = transcribe(file)

    return render_template('index.html', durl=durl, transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True)
