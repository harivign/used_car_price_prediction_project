🚗 Used Car Price Prediction - CarDekho Dataset

📌 Overview
This project predicts the resale price of used cars based on various features such as manufacturing year, fuel type, transmission, and kilometers driven.
The model is built using machine learning algorithms and deployed via Streamlit for user interaction.

🔹 Technologies Used: Python, Pandas, Scikit-Learn, Streamlit, Web Scraping
🔹 Key Skills Demonstrated: Data Cleaning, Feature Engineering, Model Training, Deployment

📂 Dataset Details
The dataset contains car details collected from multiple cities in India. The main features include:

Feature	Description
Car Name	Name of the car
Year	Manufacturing year
Kilometers Driven	Distance traveled
Fuel Type	Petrol, Diesel, CNG, etc.
Transmission	Manual or Automatic
Location	City where the car is listed
Selling Price	Target variable (Price of the car)
📁 Data Source: The data was collected from multiple online sources using web scraping techniques.

🛠 Project Workflow
✔ Data Collection – Scraped data from car-selling websites
✔ Data Cleaning – Handled missing values, outliers, and categorical encoding
✔ Exploratory Data Analysis (EDA) – Visualized patterns in car pricing
✔ Feature Engineering – Created new features to improve model accuracy
✔ Model Training – Applied Random Forest, XGBoost, and other algorithms
✔ Model Deployment – Built an interactive Streamlit web app

🔧 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/harivign/used_car_price_prediction_project.git
cd used_car_price_prediction_project
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run used_car_project.py
💡 Now, open your browser at http://localhost:8501 to use the app!

🖥 Streamlit Web App Interface
🚗 User Inputs: Enter car details (Year, Fuel Type, Transmission, etc.)
📊 Model Prediction: The app predicts the estimated resale price of the car


📈 Model Performance
The model was evaluated using: ✔ R² Score
✔ Mean Absolute Error (MAE)
✔ Root Mean Squared Error (RMSE)

📊 Best Model Achieved R² Score: 0.85 (Example)

🌍 Deployment
The project can be deployed on:

Streamlit Cloud
Heroku
AWS/GCP for real-world production use
📝 Future Improvements
🔹 Add more data for better generalization
🔹 Improve hyperparameter tuning for better model accuracy
🔹 Deploy on a cloud platform for public access

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


