class CharacterStorage:
    
    def __init__(self, transcription_result, output_file="transcription_output.txt"):
        """
        Args:
            transcription_result (dict): 文字起こし結果
            output_file (str): 出力ファイル名
        """
        self.transcription_result = transcription_result
        self.output_file = output_file
    
    def save(self):
        try:
            print(f"\n文字起こし結果をファイルに保存します: {self.output_file}")
            
            with open(self.output_file, 'w', encoding='utf-8') as f:
                if isinstance(self.transcription_result, dict):
                    # 辞書形式の場合、テキスト部分を抽出
                    text = self.transcription_result.get('text', str(self.transcription_result))
                else:
                    text = str(self.transcription_result)
                
                f.write(text)
            
            print(f"保存が完了しました: {self.output_file}")
            return True
        
        except Exception as e:
            print(f"保存中にエラーが発生しました: {e}")
            return False
