import speech_recognition as sr

def evaluate_tool(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Transcribe into Hindi
        hindi_transcription = recognizer.recognize_google(audio_data, language="hi-IN")
        print("Hindi Transcription:", hindi_transcription)

        # Transcribe into English
        english_transcription = recognizer.recognize_google(audio_data, language="en-IN")
        print("English Transcription:", english_transcription)

        # Transcribe into Hinglish
        hinglish_transcription = recognizer.recognize_google(audio_data, language="hi-IN")
        print("Hinglish Transcription:", hinglish_transcription)

        return hindi_transcription, english_transcription, hinglish_transcription

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return "", "", ""
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
        return "", "", ""

if __name__ == "__main__":
    audio_file = "C:\\Users\\shri\\Desktop\\project\\wavfiles\\record1.wav"  # Replace with the actual path to your audio file

    # Step 1: Tool Evaluation
    hindi_transcription, english_transcription, hinglish_transcription = evaluate_tool(audio_file)
