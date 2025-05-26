from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# 模拟的商品推荐数据
products = [
    {"id": 1, "name": "商品 A", "category": "电子产品"},
    {"id": 2, "name": "商品 B", "category": "书籍"},
    {"id": 3, "name": "商品 C", "category": "家居用品"},
    {"id": 4, "name": "商品 D", "category": "电子产品"},
    {"id": 5, "name": "商品 E", "category": "书籍"},
]


# 用户推荐逻辑（此处为简单示范）
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', default=None, type=int)

    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400

    # 简单的随机推荐逻辑，真实场景中可以更复杂（基于协同过滤、内容推荐等）
    recommended = random.sample(products, 3)  # 推荐3个商品
    return jsonify({"user_id": user_id, "recommended_products": recommended})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
