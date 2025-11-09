from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Number Info API is running on Vercel!"})

@app.route('/number-info', methods=['GET'])
def number_info():
    number = request.args.get('number')
    if not number:
        return jsonify({"error": "Please provide ?number= parameter"}), 400

    info = {
        "number": number,
        "operator": "Jio",
        "circle": "Delhi NCR",
        "status": "Active"
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)
