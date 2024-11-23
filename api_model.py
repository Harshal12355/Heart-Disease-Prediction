from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load your trained model
with open('heart_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

print(type(model))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        data = request.form.to_dict()
        features = np.array([float(data[key]) for key in data.keys()]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return the result
        result = 'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease'
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
