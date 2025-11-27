from flask import Flask, request    # Flaskは必須、requestはリクエストパラメータを処理する場合に使用します。
app = Flask(__name__)


@app.route('/income/')
@app.route('/income/<name>')
def income(name=None):
    if name is None:
        message = "誰も来ていません"
    else:
        message = "{}さんが来ています".format(name)
    
    return "<html><body><h1>K24044</h1><h2>{}</h2></body></html>".format(message)


if __name__ == "__main__":
    # port=8080にて、アプリケーションの動作ポート番号を指定しています。省略すると5000から使用可能な番号で起動します。
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="0.0.0.0", port=8080, debug=True)