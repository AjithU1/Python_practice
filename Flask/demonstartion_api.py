from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
items = {}


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404


@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.get_json()
    item_id = item_data.get('id')
    if not item_id or item_id in items:
        return jsonify({"error": "Item ID is required and must be unique"}), 400

    items[item_id] = item_data
    return jsonify(item_data), 201


@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404

    item_data = request.get_json()
    items[item_id] = item_data
    return jsonify(item_data), 200


@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return '', 204
    else:
        return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
