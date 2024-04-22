from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/sense', methods=['POST'])
def get_sensor_data():
    # Parse incoming JSON data
    data = request.json
    try:
        # Extracting 'pulse', 'spo2', and 'temperature' from the incoming JSON
        pulse = data.get('pulse', 0)
        spo2 = data.get('spo2', 0)
        temperature = data.get('temperature', 0.0)  # Assuming temperature can be a float

        # Convert the values to a numpy array
        # Including temperature along with pulse and spo2 for consistency
        values = np.array([pulse, spo2, temperature], dtype=np.float64)
        
        # Check if pulse and spo2 are greater than 0, and temperature is a valid number
        if values[0] > 0 and values[1] > 0 and not np.isnan(values[2]):
            return jsonify({
                'status': 'success', 
                'data': {
                    'pulse': values[0], 
                    'spo2': values[1], 
                    'temperature': values[2]
                }
            })
        else:
            return jsonify({'error': 'Invalid data received'})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
