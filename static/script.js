document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const voiceSelect = document.getElementById('voice-select');
    const generateBtn = document.getElementById('generate-btn');
    const loader = document.getElementById('loader');
    const btnText = document.querySelector('.btn-text');
    const statusMessage = document.getElementById('status-message');
    const savedFilename = document.getElementById('saved-filename');

    // Fetch available voices
    async function fetchVoices() {
        try {
            const response = await fetch('/api/voices');
            const voices = await response.json();

            voices.forEach(voice => {
                const option = document.createElement('option');
                option.value = voice.name;
                option.textContent = `${voice.name} (${voice.gender})`;
                voiceSelect.appendChild(option);
            });

            // Set default voice
            if (voices.some(v => v.name === 'Jasper')) {
                voiceSelect.value = 'Jasper';
            }
        } catch (error) {
            console.error('Error fetching voices:', error);
        }
    }

    // Generate Audio
    async function generateAudio() {
        const text = textInput.value.trim();
        const voice = voiceSelect.value;

        if (!text) {
            alert('Please enter some text!');
            return;
        }

        // UI State: Loading
        generateBtn.disabled = true;
        loader.style.display = 'block';
        btnText.style.display = 'none';
        statusMessage.classList.remove('status-visible');

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text, voice }),
            });

            const result = await response.json();

            if (result.status === 'success') {
                // UI State: Success
                savedFilename.textContent = result.filename;
                statusMessage.classList.add('status-visible');

                // Hide status after 5 seconds
                setTimeout(() => {
                    statusMessage.classList.remove('status-visible');
                }, 5000);
            } else {
                alert('Generation failed: ' + result.detail);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during generation.');
        } finally {
            // UI State: Reset
            generateBtn.disabled = false;
            loader.style.display = 'none';
            btnText.style.display = 'block';
        }
    }

    generateBtn.addEventListener('click', generateAudio);

    // Initial fetch
    fetchVoices();
});
