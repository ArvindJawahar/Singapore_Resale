# Singapore HDB Resale Price Prediction

## Project Overview

This project aims to predict the resale prices of Housing and Development Board (HDB) flats in Singapore. The main tasks involved in this project are:

1. **Data Collection and Preprocessing**:
   - Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date.  You can find the dataset [here](https://beta.data.gov.sg/collections/189/view).
   - Preprocess the data to clean and structure it for machine learning.

2. **Feature Engineering**:
   - Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date.
   - Create any additional features that may enhance prediction accuracy.

3. **Model Selection and Training**:
   - Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests).
   - Train the model on the historical data, using a portion of the dataset for training.

4. **Model Evaluation**:
   - Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE), and R2 Score.

5. **Streamlit Web Application**:
   - Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.).
   - Utilize the trained machine learning model to predict the resale price based on user inputs.

6. **Deployment on Render**:
   - Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.

7. **Testing and Validation**:
   - Thoroughly test the deployed application to ensure it functions correctly and provides accurate predictions.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
   
2. Install the required Python packages by running the following command:

   ```bash
   pip install -r requirements.txt

3. start the streamlit web apploication

   ```bash
   streamlit run main.py
