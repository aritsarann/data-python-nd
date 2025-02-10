# Real-Time Bitcoin Price Prediction using Machine Learning

### Project Overview

This project implements a real-time Bitcoin price prediction system using Machine Learning techniques. Automated workflows are set up using Apache Airflow to continuously predict the price of Bitcoin every 5 minutes, based on historical data. The model uses **Random Forest Regression** to forecast the prices, and the prediction accuracy is evaluated using the **Mean Absolute Percentage Error (MAPE)**.

Additionally, real-time Bitcoin price data is collected and stored in **MongoDB**. The system continuously fetches the latest price data from MongoDB to train the **Random Forest Regression** model, which then predicts future Bitcoin prices. The predicted values are compared with the actual real-time prices stored in MongoDB to assess the model's **accuracy**.

### Key Features:
- **Automated Workflows**: Utilizing Apache Airflow DAGs for scheduling and execution.
- **Data Collection**: Real-time Bitcoin price data is stored in **MongoDB**.
- **Machine Learning Model**: Random Forest Regression to predict Bitcoin prices.
- **Real-Time Comparison**: Predicted Bitcoin prices are compared with actual real-time prices from MongoDB.
- **Accuracy**: Achieved an average MAPE of **0.3299**.
