import os
import time
import soundfile as sf
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from kittentts import KittenTTS
import uvicorn

app = FastAPI()

# Initialize KittenTTS
init_error = None
try:
    m = KittenTTS("KittenML/kitten-tts-mini-0.8")
except Exception as e:
    init_error = str(e)
    print(f"Error initializing KittenTTS: {init_error}")
    m = None

# Ensure output directory exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class GenerateRequest(BaseModel):
    text: str
    voice: str

@app.post("/api/generate")
async def generate_audio(request: GenerateRequest):
    if not m:
        error_msg = f"TTS Model not initialized. {init_error if init_error else 'Please check console logs.'}"
        raise HTTPException(status_code=500, detail=error_msg)
    
    try:
        # Generate audio
        audio = m.generate(request.text, voice=request.voice)
        
        # Create unique filename: {voice}_{timestamp}.wav
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{request.voice}_{timestamp}.wav"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Ensure unique filename if generated in the same second
        counter = 1
        while os.path.exists(filepath):
            filename = f"{request.voice}_{timestamp}_{counter}.wav"
            filepath = os.path.join(OUTPUT_DIR, filename)
            counter += 1
            
        # Save the audio
        sf.write(filepath, audio, 24000)
        
        return {"status": "success", "filename": filename, "path": filepath}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/voices")
async def get_voices():
    # Sorted by Female first, then Male, and alphabetical within each group
    return [
        {"name": "Bella", "gender": "Female"},
        {"name": "Kiki", "gender": "Female"},
        {"name": "Luna", "gender": "Female"},
        {"name": "Rosie", "gender": "Female"},
        {"name": "Bruno", "gender": "Male"},
        {"name": "Hugo", "gender": "Male"},
        {"name": "Jasper", "gender": "Male"},
        {"name": "Leo", "gender": "Male"}
    ]

# Serve static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7689)
