from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample waste collection data
waste_records = [
    {
        "id": 1,
        "type": "Dry Waste",
        "location": "Sector 1",
        "status": "Collected"
    },
    {
        "id": 2,
        "type": "Wet Waste",
        "location": "Sector 2",
        "status": "Pending"
    },
    {
        "id": 3,
        "type": "Plastic Waste",
        "location": "Sector 3",
        "status": "Collected"
    }
]


@app.route("/")
def home():
    return jsonify({
        "service": "Waste Management Service",
        "status": "running"
    })


@app.route("/waste", methods=["GET"])
def get_waste():
    return jsonify({
        "waste": waste_records
    })


@app.route("/waste", methods=["POST"])
def add_waste():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No waste data provided"
        }), 400

    new_record = {
        "id": len(waste_records) + 1,
        "type": data.get("type"),
        "location": data.get("location"),
        "status": data.get("status", "Pending")
    }

    waste_records.append(new_record)

    return jsonify({
        "message": "Waste record added successfully",
        "record": new_record
    }), 201


@app.route("/schedule")
def schedule():
    return jsonify({
        "schedule": [
            {
                "day": "Monday",
                "waste_type": "Wet Waste",
                "time": "08:00 AM"
            },
            {
                "day": "Wednesday",
                "waste_type": "Dry Waste",
                "time": "09:00 AM"
            },
            {
                "day": "Friday",
                "waste_type": "Plastic Waste",
                "time": "10:00 AM"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)