# 🤖 Aria - Persian Voice AI Assistant

Aria is a Persian-speaking voice assistant built with Python. It can listen to your voice, convert speech to text, send the conversation to an AI model, and reply with a natural Persian voice.

---

## ✨ Features

* 🎤 Voice recording from microphone
* 📝 Speech-to-Text (Persian)
* 🧠 AI conversation using OpenAI-compatible API
* 🔊 Natural Persian Text-to-Speech
* 💬 Conversation memory during runtime
* 🚪 Voice command to exit

---

## 📂 Project Structure

```
aria_bot/
│
├── main.py
├── config.py
│
├── core/
│   ├── ai.py
│   ├── voice.py
│   ├── memory.py
│   ├── emotion.py
│   └── character.py
│
└── data/
    └── memory.json
```

---

## 🛠 Requirements

Python 3.10+

Install dependencies:

```bash
pip install openai
pip install sounddevice
pip install soundfile
pip install SpeechRecognition
pip install edge-tts
pip install playsound3
```

Or install everything at once:

```bash
pip install openai sounddevice soundfile SpeechRecognition edge-tts playsound3
```

---

## 🔑 API Configuration

Edit the API key inside the project:

```python
client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key="YOUR_API_KEY"
)
```

Replace `YOUR_API_KEY` with your own key.

---

## ▶️ Run

```bash
python main.py
```

When the assistant starts, simply speak into your microphone.

To exit, say:

* خداحافظ
* بسه
* exit
* bye

---

## ⚙️ Technologies

* Python
* OpenAI API
* SpeechRecognition
* sounddevice
* soundfile
* edge-tts
* playsound3

---

## 🔄 Workflow

```
Microphone
      │
      ▼
Record Audio
      │
      ▼
Speech to Text
      │
      ▼
OpenAI API
      │
      ▼
AI Response
      │
      ▼
Text to Speech
      │
      ▼
Speaker
```

---

## 💡 Current Capabilities

* Persian voice conversation
* Runtime conversation memory
* AI-generated responses
* Natural Persian speech synthesis

---

## 🚀 Future Improvements

* Long-term memory using JSON
* Emotion detection
* Animated avatar
* Graphical desktop interface (PyQt6)
* Wake word detection ("Hey Aria")
* Streaming speech recognition
* Local LLM support
* Multi-language support

---

## 📄 License

This project is released under the MIT License.

---

## 👨‍💻 Author

Developed by **Heli** as a personal AI assistant project.
