import sounddevice as sd
import wavio

def record_audio(duration, filename, samplerate=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    
    # Save the recording as a WAV file
    wavio.write(filename, recording, samplerate, sampwidth=2)
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    duration = 10  # Duration of the recording in seconds
    filename = "recording.wav"  # Name of the output file

    record_audio(duration, filename)
