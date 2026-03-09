# KittenTTS GUI

A sleek, web-based interface for the **KittenTTS** text-to-speech engine. This application allows you to generate high-quality audio from text using various voices and automatically saves the output as unique WAV files.

## Features

- **Web GUI**: Easy-to-use interface built with FastAPI.
- **High Quality**: Uses the `KittenML/kitten-tts-mini-0.8` model for superior voice quality.
- **Multiple Voices**: Choose from a variety of male and female voices (Bella, Kiki, Luna, Rosie, Bruno, Hugo, Jasper, Leo).
- **Auto-Saving**: Audio files are automatically saved to an `output/` directory with unique timestamps.
- **CPU Efficient**: Works seamlessly without requiring a GPU.

## Prerequisites

- Python 3.12+ (don't not use Pythong3.13)
- [FFmpeg](https://ffmpeg.org/) (required by `soundfile` for certain operations, though basic WAV export usually works with just the library).

## Installation

### 1. Set up with Conda (Recommended)

Conda is the recommended way to manage environments for this project.

```bash
# Create a new environment
conda create -n kittentts python=3.12

# Activate the environment
conda activate kittentts
```

### 2. Install dependencies

Once the Conda environment is activated, install the necessary libraries:

```bash
pip install kittentts fastapi uvicorn soundfile pydantic torch transformers
```

## How to Run

1. Clone or download this repository.
2. Navigate to the project directory:
   ```bash
   cd KittenTTS-WEBUI
   ```
3. Start the application:
   ```bash
   python KittenTTS-WEBUI.py
   ```
4. Open your web browser and go to:
   ```
   http://localhost:7689
   ```

## Usage

1. **Enter Text**: Type the text you want to convert to speech in the input field.
2. **Select Voice**: Choose a voice from the dropdown menu (includes Gender tags).
3. **Generate**: Click the "Generate" button.
4. **Download/Review**: The generated file will be saved in the `output/` directory. The UI will confirm the filename once generation is complete.

## Project Structure

- `KittenTTS-WEBUI.py`: The main FastAPI server.
- `static/`: Contains the frontend assets (HTML, CSS, JS).
- `output/`: Where generated audio files are stored.
- `sample.py`: A simple CLI example script.

## Troubleshooting

If you encounter the error `Generation failed: TTS Model not initialized`, it usually means the Hugging Face model could not be downloaded or initialized.

### Common Issues on PC/Windows:

1.  **Missing `espeak-ng` (CRITICAL)**: If you see `espeak not installed on your system`, you must install the `espeak-ng` system library:
    -   Download the installer from [espeak-ng GitHub Releases](https://github.com/espeak-ng/espeak-ng/releases) (look for `espeak-ng-X.XX-x64.msi`).
    -   Run the installer and follow the prompts.
    -   **Important**: You may need to restart your terminal or PC after installation for the changes to take effect.
    -   To verify, open a new Command Prompt and type `espeak-ng "test"`. If you hear a voice, it's working.
2.  **Internet Connection**: The first time you run the app, it needs to download about 150MB of model data from Hugging Face. Ensure you have a stable internet connection.
2.  **Missing Dependencies**: Ensure all required libraries are installed:
    ```bash
    pip install kittentts fastapi uvicorn soundfile pydantic torch transformers
    ```
3.  **Microsoft Visual C++ Redistributable**: Some dependencies (like `soundfile` or `torch`) may require the [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) to be installed on Windows.
4.  **Python Version**: Ensure you are using Python 3.8 or higher.
5.  **Check Console Logs**: The command window where you ran `python KittenTTS-GUI.py` will show the specific error message during startup.

## Acknowledgments

- [KittenML](https://github.com/KittenML) for the underlying TTS model.
