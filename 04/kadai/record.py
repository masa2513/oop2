import ffmpeg
import time

class Record:
    
    def __init__(self, duration, output_file):
        """
        Args:
            duration (int): 録音時間（秒）
            output_file (str): 出力ファイル名
        """
        self.duration = duration
        self.output_file = output_file
    
    def record(self):
        try:
            print(f"{self.duration}秒間、マイクからの録音を開始します...")
            # FFmpegコマンドを実行
            # -f <デバイス入力形式>: OSに応じたデバイス入力形式を指定
            #   - Windows: 'dshow' または 'gdigrab'
            #   - macOS: 'avfoundation'
            #   - Linux: 'alsa'
            # -i <入力デバイス名>: デバイス名を指定
            (
                ffmpeg
                .input(':1', format='avfoundation', t=self.duration) # macOSの例（:0=内蔵マイク）
                .output(self.output_file, acodec='pcm_s16le', ar='44100', ac=1)
                .run(overwrite_output=True)
            )
            print(f"録音が完了しました。{self.output_file}に保存されました。")
            return True
        
        except ffmpeg.Error as e:
            error_message = e.stderr.decode() if e.stderr else str(e)
            print(f"録音エラーが発生しました: {error_message}")
            return False
        except Exception as e:
            print(f"予期せぬエラー: {e}")
            return False
