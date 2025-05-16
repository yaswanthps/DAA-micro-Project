from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

def crack_password_logic(password):
    start = time.time()
    attempts = 0
    cracked = False

    # Try all 4-digit numeric passwords from 0000 to 9999
    for i in range(10000):
        attempt = f"{i:04d}"
        attempts += 1
        # Artificial delay to make time measurable (optional)
        time.sleep(0.0001)
        if attempt == password:
            cracked = True
            break

    elapsed = round(time.time() - start, 4)  # More precision

    return {
        "cracked": cracked,
        "attempts": attempts,
        "time": elapsed
    }

@app.route('/crack', methods=['POST'])
def crack_password():
    data = request.get_json()
    password = data.get("password", "")

    result = crack_password_logic(password)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)