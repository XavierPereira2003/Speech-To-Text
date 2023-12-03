# Speech to Text

Speech to Text is a simple web application that allows users to transcribe audio files into text using the Facebook Wav2Vec2 model. This project is built using Flask and leverages the Hugging Face Transformers library.

## Features

- Transcribe audio files in formats like .wav, .mp3, and .flac.
- Display the transcribed text on the web interface.

## Getting Started

### Prerequisites

Make sure you have Python and pip installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/speech-to-text.git
    cd speech-to-text
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Upload an audio file and click the "Transcribe" button to see the transcribed text.

### Usage

- Choose an audio file (supported formats: .wav, .mp3, .flac).
- Click the "Transcribe" button to get the transcribed text.

<!-- ### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->
