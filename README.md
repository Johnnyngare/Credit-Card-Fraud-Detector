# Credit Card Fraud Detection System Using Machine Learning and Flask
This project is a real-time credit card fraud detection system built using Flask, Google OAuth for authentication, and Machine Learning models to detect suspicious transactions. It allows users to securely log in using their Google accounts, view transaction data, and detect potential fraudulent activities.

# Features:
User Authentication: Secure login and authentication using Google OAuth 2.0.
Machine Learning Model: Utilizes advanced machine learning algorithms such as XGBoost to identify potentially fraudulent transactions.
Real-time Fraud Detection: Detects fraud in real-time by analyzing incoming transaction data.
Interactive Dashboard: Visualizes transactions and highlights potential fraud using Plotly or Chart.js.
User-Friendly Interface: The system provides an intuitive, responsive, and easy-to-use front end for users.
# Technologies Used:
Flask: Python web framework for building the server-side logic.
Google OAuth 2.0: For user authentication and authorization.
XGBoost: Machine learning model for fraud detection.
HTML/CSS/JavaScript: Front-end interface.
Plotly/Chart.js: Data visualization for transaction data and fraud alerts.
AWS SageMaker: For hosting the machine learning models (optional, if using AWS).
SQLite/PostgreSQL: For storing user and transaction data.
# Installation Instructions:
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection
Set Up the Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up OAuth 2.0 Credentials:

Create a new project on Google Cloud Console and enable Google OAuth 2.0.
Download the credentials and place them in the project folder.
Configure your client_id and client_secret in the Flask app.
Run the Application:

bash
Copy code
flask run
Access the App:

Open http://127.0.0.1:5000/ in your web browser to start using the system.
# How It Works:
Users log in with their Google accounts via OAuth 2.0.
Transactions are loaded into the system, where a machine learning model (e.g., XGBoost) processes them to detect potential fraud.
An interactive dashboard allows users to view transaction details and highlights flagged fraudulent activities.
Contributing:
Feel free to fork this repository, open issues, and submit pull requests to improve the system.

# License:
This project is licensed under the MIT License.
