import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import asyncio
import edge_tts
from playsound3 import playsound
from openai import OpenAI

# -----------------------------
# AI CLIENT
# -----------------------------
client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key="sk-jSNbbChbjgJVZ1VrJAQii6f9IS0IoDxfw2kTzHAk70qf9D8P"
)

# -----------------------------
# MEMORY
# -----------------------------
conversation_history = []

# -----------------------------
# RECORD AUDIO
# -----------------------------
def record_audio(filename="recording.wav", duration=4, fs=16000):
    print("\n🎤 صحبت کنید...")

    audio = sd.rec(int(duration * fs),
                   samplerate=fs,
                   channels=1,
                   dtype="float32")

    sd.wait()
    sf.write(filename, audio, fs)

    return filename

# -----------------------------
# SPEECH TO TEXT
# -----------------------------
def speech_to_text(file):
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language="fa-IR")
        print("You:", text)
        return text
    except:
        print("❌ متوجه نشدم")
        return ""

# -----------------------------
# TEXT TO SPEECH
# -----------------------------
async def speak(text):
    tts = edge_tts.Communicate(
        text=text,
        voice="fa-IR-DilaraNeural"
    )
    await tts.save("voice.mp3")
    playsound("voice.mp3")

# -----------------------------
# SYSTEM PROMPT
# -----------------------------
SYSTEM_PROMPT = """
You are Aria, a Persian-speaking AI companion.
Be short, friendly, and helpful.
"""

# -----------------------------
# MAIN LOOP
# -----------------------------
print("🤖 آریا آماده است... (خداحافظ / بسه / exit برای خروج)")

while True:

    # 1. record
    file = record_audio()

    # 2. speech to text
    user_text = speech_to_text(file)

    user_text = user_text.strip()

    if user_text == "":
        print("⚠️ چیزی شنیده نشد...")
        continue

    # 3. exit condition
    if user_text.lower() in ["خداحافظ", "بسه", "exit", "bye"]:
        print("👋 خداحافظ")
        asyncio.run(speak("خداحافظ"))
        break

    print("🤖 در حال فکر کردن...")

    # 4. add memory
    conversation_history.append({
        "role": "user",
        "content": user_text
    })

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ] + conversation_history

    # 5. GPT CALL (SAFE)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        answer = response.choices[0].message.content

    except Exception as e:
        print("❌ خطای GPT:", e)
        continue

    # 6. save memory
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })

    # 7. output
    print("Aria:", answer)

    # 8. speak
    asyncio.run(speak(answer))