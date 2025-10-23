import mlx_whisper
from pydub import AudioSegment
import numpy as np

class Transcription:
    
    def __init__(self, audio_file_path):
        """
        Args:
            audio_file_path (str): 音声ファイルのパス
        """
        self.audio_file_path = audio_file_path
        self.result = None
    
    def transcribe(self):
        try:
            print(f"\n文字起こしを開始します: {self.audio_file_path}")
            
            self.result = mlx_whisper.transcribe(
                self.audio_file_path, 
                path_or_hf_repo="whisper-base-mlx"
            )
            
            print(f"文字起こし結果: {self.result['text']}")
            return self.result
        
        except Exception as e:
            print(f"文字起こし中にエラーが発生しました: {e}")
            # デモ用のダミーデータを返す
            self.result = {
                'text': '（デモンストレーション用のダミーテキストです。実際の環境では、ここに音声認識された内容が表示されます。）',
                'segments': [],
                'language': 'ja'
            }
            print(f"ダミーデータを使用: {self.result['text']}")
            return self.result
    
    def preprocess_audio(self, sound):
        """音声データを前処理する"""
        if sound.frame_rate != 16000:
            sound = sound.set_frame_rate(16000)
        if sound.sample_width != 2:
            sound = sound.set_sample_width(2)
        if sound.channels != 1:
            sound = sound.set_channels(1)
        return sound
