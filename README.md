# Heart Disease Prediction Web Application

Welcome to the **Heart Disease Prediction** web application. This project provides a machine learning-powered tool to predict the likelihood of heart disease based on user inputs such as age, sex, cholesterol levels, and other health parameters.

## Project Overview

This application leverages a machine learning model trained on a heart disease dataset to predict whether an individual is at risk of heart disease. The user-friendly interface allows users to input key health data, and the system returns a prediction of either **Heart Disease Present** or **No Heart Disease**.

### Key Features:
- **Form-based input**: Collects user data including age, sex, cholesterol, chest pain type, and other medical details.
- **Real-time prediction**: Submits the data to a backend model which predicts the likelihood of heart disease.
- **Responsive design**: Optimized for all devices (desktop, tablet, and mobile).

## Technologies Used

- **Backend**: Flask (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Python, scikit-learn (for model training and prediction)
- **Deployment**: Local/Cloud server

## Installation

To run the project locally, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies

Ensure you have Python 3.x installed. Then, install the necessary dependencies:

```
pip install -r requirements.txt
```

### 3. Run the Application

Start the Flask application by running the following command:

```
python app.py
```

## Web Interface

### Home Page

The user is presented with a clean, professional form where they can input the following details:

- Age: Age of the individual
- Sex: Gender of the individual (Male or Female)
- Chest Pain Type: Categorized into 4 types
- Blood Pressure, Cholesterol, and other medical details: Various health-related inputs

Once the user fills out the form, they can click the Predict button to submit the data.

## Prediction Result

After submitting the form, the application will display one of the following predictions:

- Heart Disease Present: Indicates that the model predicts the individual is at risk for heart disease.
- No Heart Disease: Indicates that the model predicts the individual is not at risk

## How It Works

- Data Collection: The user enters personal and medical details via a form on the frontend.
- Data Processing: The collected data is sent to the Flask backend via a POST request.
- Prediction: The Flask backend processes the data and uses the trained model to make a prediction.
- Result: The prediction is displayed on the frontend, informing the user of their risk.

## Model Details

The heart disease prediction model is trained using the Heart Disease UCI dataset. The model uses various health features to predict whether an individual is at risk of heart disease or not. It leverages machine learning algorithms such as Logistic Regression, Random Forests, or Support Vector Machines for classification.

## Contributing

We welcome contributions! If you'd like to improve this project, you can:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

The model is based on the Heart Disease UCI dataset, which is publicly available and widely used for medical prediction tasks. Special thanks to scikit-learn for providing the machine learning tools used in this project.