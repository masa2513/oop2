from record import Record
from transcription import Transcription
from characterStorage import CharacterStorage

def main():
    # 設定
    duration = 10  # 録音時間（秒）
    audio_file = "python-audio-output.wav"
    text_file = "transcription_output.txt"
    
    # 音声録音
    recorder = Record(duration, audio_file)
    record_success = recorder.record()
    
    # 音声文字起こし
    transcription = Transcription(audio_file)
    result = transcription.transcribe()
    
    # 文字保存
    storage = CharacterStorage(result, text_file)
    save_success = storage.save()

if __name__ == "__main__":
    main()

