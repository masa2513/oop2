from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ
from datetime import datetime

app = Flask(__name__)

URANAI_RESULT_MESSAGES = {
    1: "今日は物理実験が失敗して、再実験になるかも？",
    2: "今日はオブ演が難しすぎて、早退するかも？",
    3: "今日は普通の日すぎて、特に何も起こらないかも？",
    4: "今日はプロジェクト演習がうまくいって、成績Sがもらえるかも？",
    5: "今日は授業を全て欠席して、遊んでるかも？(おめでとう)",
}

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():

    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"
    
    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)

    # 接待モードのチェックボックス
    settai_mode = request.form.get("settai_mode") == "on"

    # CPUの手を決定
    if settai_mode and hand:
        # 接待モードの場合、CPUは必ず負けるようにする
        if hand == "rock":
            cpu = "scissor"  # プレイヤーがグーなら、CPUはチョキ（プレイヤーの勝ち）
        elif hand == "scissor":
            cpu = "paper"  # プレイヤーがチョキなら、CPUはパー（プレイヤーの勝ち）
        elif hand == "paper":
            cpu = "rock"  # プレイヤーがパーなら、CPUはグー（プレイヤーの勝ち）
        else:
            cpu = random.choice(["rock", "scissor", "paper"])
    else:
        # 通常モード：リストの中からランダムに選ぶ
        cpu = random.choice(["rock", "scissor", "paper"])

    # じゃんけん処理
    if hand == cpu:
        result_message = "あいこ"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                           result_message=result_message,
                           name=name,
                           hand=hand,
                           cpu=cpu)


# 4. 占いアプリ
@app.route('/uranai')
def uranai():
    return render_template('uranai_form.html')


@app.route('/uranai/play', methods=["POST"])
def uranai_play():
    name = request.form.get("name", "").strip()
    birthday_raw = request.form.get("birthday", "").strip()

    is_valid = True
    birthday_value = None

    if not name:
        is_valid = False

    try:
        birthday_value = datetime.strptime(birthday_raw, "%Y-%m-%d")
    except ValueError:
        is_valid = False

    if not is_valid:
        result_score = 1
        fortune_message = "入力不備で占えませんでした"
    else:
        today_value = int(datetime.now().strftime("%Y%m%d"))
        birth_value = int(birthday_value.strftime("%Y%m%d"))
        diff = abs(today_value - birth_value)
        product = diff * len(name)
        result_map = [5, 1, 3, 2, 4]
        result_score = result_map[product % len(result_map)]
        fortune_message = URANAI_RESULT_MESSAGES[result_score]

    return render_template(
        'uranai_result.html',
        name=name or "名無しさん",
        birthday=birthday_raw,
        result_score=result_score,
        fortune_message=fortune_message,
        is_error=not is_valid
    )


if __name__ == '__main__':
    # portは適宜書き換えてください
    app.run(host="0.0.0.0", port=8888, debug=True)