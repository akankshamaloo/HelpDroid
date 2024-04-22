# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sensor Data Receiver'

@app.route('/sensing', methods=['POST'])
def receive_data():
    # Parse incoming JSON data
    data = request.json
    print("Received data: ", data)

    # Log the sensor data to the console
    temperature = data.get('temperature')
    heartRate = data.get('heartRate')
    spo2 = data.get('spo2')
    
    print(f"Temperature: {temperature} C")
    print(f"Heart Rate: {heartRate} BPM")
    print(f"SpO2: {spo2}%")

    # Respond to the Arduino with a success message
    response = {"status": "success", "message": "Data received"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
