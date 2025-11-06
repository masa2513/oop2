# Report Builder MD
- マークダウン記法でレポートを作成するGUIアプリ
- オブジェクト指向プログラミング及び演習２の講義資料の一部

## 作成者
- 内種岳詞(takeshi.uchitane@aitech.ac.jp)

## 要件
- 以下の環境で動作確認済み
    - Python 3.11.5
    - PySide6 6.6.0

## 使い方
0. 初回利用時のみ`status_orig.json`を参考に`status.json`を作成する
1. status.jsonの存在しているディレクトリでmain.pyを実行(`python main.py`)
2. 画面左の編集ボタンから内容を更新
3. `Save`ボタンもしくは`Save without history`ボタンでマークダウン記法のレポートを書き出し
    - 次回起動時に更新後の内容から編集を始めたいときはSaveボタンを利用する
    - 次回起動時に変更内容を反映したくないときはSave without historyボタンを利用する

## プログラム利用の注意
- 学外への公開を認めない．
- 本プログラムを利用して生じた不利益への責は，プログラム作成者には無い．
