import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# ==============================================================================
# アプリケーション設定と定数定義
# ==============================================================================

app = Flask(__name__)

# CORS (Cross-Origin Resource Sharing) の有効化
# これにより、別のドメインやポート（例: localhost:3000）のフロントエンドから
# このAPIへのアクセスが可能になります。
CORS(app)

# データを保存するJSONファイルのパス設定
# このファイルのディレクトリを基準にパスを作成（実行ディレクトリに依存させないため）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, 'contacts.json')


# ==============================================================================
# ヘルパー関数（データの読み書き担当）
# ==============================================================================

def load_data():
    """
    JSONファイルから連絡先データを読み込みます。
    
    Returns:
        list: 連絡先データのリスト。ファイルがない、または壊れている場合は空リストを返す。
    """
    # ファイルが存在しない場合は、まだデータがないので空リストを返す
    if not os.path.exists(DATA_FILE_PATH):
        return []
    
    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # ファイルの中身が空だったり、JSON形式が不正な場合も空リストを返す
        return []

def save_data(data):
    """
    連絡先データをJSONファイルに書き込みます。
    
    Args:
        data (list): 保存したい連絡先データのリスト
    """
    with open(DATA_FILE_PATH, 'w', encoding='utf-8') as f:
        # ensure_ascii=False: 日本語をUnicodeエスケープ(\uXXXX)せずそのまま保存
        # indent=4: 人間が読みやすいようにインデントをつけて整形
        json.dump(data, f, ensure_ascii=False, indent=4)


# ==============================================================================
# ルーティング定義 (APIのエンドポイント)
# ==============================================================================

# ------------------------------------------------------------------
# [GET] 一覧取得
# URL: /api/contacts
# ------------------------------------------------------------------
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """保存されているすべてのアドレス帳データを返します"""
    contacts = load_data()
    return jsonify(contacts), 200


# ------------------------------------------------------------------
# [GET] 個別取得
# URL: /api/contacts/<id>
# ------------------------------------------------------------------
@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """指定されたIDの連絡先を1件返します"""
    contacts = load_data()
    
    # リストの中からIDが一致するものを探す
    # next() は条件に合う最初の要素を返します。見つからない場合は None を返します。
    contact = next((item for item in contacts if item['id'] == contact_id), None)
    
    if contact:
        return jsonify(contact), 200
    else:
        return jsonify({'error': 'Contact not found'}), 404


# ------------------------------------------------------------------
# [POST] 新規作成
# URL: /api/contacts
# Body: { "name": "...", "phone": "...", "email": "..." }
# ------------------------------------------------------------------
@app.route('/api/contacts', methods=['POST'])
def create_contact():
    """新しい連絡先を作成し、保存します"""
    # リクエストのJSONボディを取得
    request_data = request.get_json()

    # バリデーション: 名前(name)は必須項目とする
    if not request_data or 'name' not in request_data:
        return jsonify({'error': 'Name is required'}), 400

    contacts = load_data()

    # IDの自動採番ロジック
    # データがあれば「最後のID + 1」、データが空なら「1」とする
    if contacts:
        new_id = contacts[-1]['id'] + 1
    else:
        new_id = 1

    # 新しいデータ辞書の作成
    new_contact = {
        'id': new_id,
        'name': request_data['name'],
        'phone': request_data.get('phone', ''), # キーがない場合は空文字を設定
        'email': request_data.get('email', '')
    }

    # リストに追加してファイルへ保存
    contacts.append(new_contact)
    save_data(contacts)

    # 作成成功(201 Created)として、作ったデータを返す
    return jsonify(new_contact), 201


# ------------------------------------------------------------------
# [PUT] 更新
# URL: /api/contacts/<id>
# Body: { "name": "...", ... }
# ------------------------------------------------------------------
@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """指定されたIDの連絡先情報を更新します"""
    request_data = request.get_json()
    contacts = load_data()

    # 更新対象のデータがリストの何番目にあるか(index)を探す
    target_index = None
    for i, item in enumerate(contacts):
        if item['id'] == contact_id:
            target_index = i
            break

    # 見つからなかった場合
    if target_index is None:
        return jsonify({'error': 'Contact not found'}), 404

    # データの更新処理
    # リクエストに含まれていれば新しい値に、含まれていなければ元の値を維持
    current_contact = contacts[target_index]
    current_contact['name'] = request_data.get('name', current_contact['name'])
    current_contact['phone'] = request_data.get('phone', current_contact['phone'])
    current_contact['email'] = request_data.get('email', current_contact['email'])

    # リストを更新して保存
    contacts[target_index] = current_contact
    save_data(contacts)

    return jsonify(current_contact), 200


# ------------------------------------------------------------------
# [DELETE] 削除
# URL: /api/contacts/<id>
# ------------------------------------------------------------------
@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """指定されたIDの連絡先を削除します"""
    contacts = load_data()
    
    # 指定されたID「ではない」データだけを集めた新しいリストを作成（フィルタリング）
    filtered_contacts = [item for item in contacts if item['id'] != contact_id]

    # 削除前後でリストの長さが同じ＝削除対象が見つからなかったということ
    if len(contacts) == len(filtered_contacts):
        return jsonify({'error': 'Contact not found'}), 404

    # 新しいリストで上書き保存
    save_data(filtered_contacts)
    
    return jsonify({'message': 'Contact deleted successfully'}), 200


# ==============================================================================
# 4. サーバー起動
# ==============================================================================

if __name__ == '__main__':
    # debug=True にすると、コード変更時に自動リロードされ、エラー詳細が表示されます
    app.run(host="0.0.0.0", port=8888, debug=True)