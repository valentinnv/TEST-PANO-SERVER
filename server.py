from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/discover-assets')
def discover_assets():
    assets_dir = os.path.join(os.getcwd(), 'assets')
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp')
    images = []
    if os.path.exists(assets_dir):
        images = [f for f in os.listdir(assets_dir) if f.lower().endswith(valid_exts)]
    return jsonify(images)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)