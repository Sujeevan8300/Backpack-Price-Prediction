# Software Overview: Backpack Price Prediction Challenge  

## Overview  
This project is a **machine learning-based web application** developed for the **Kaggle Backpack Price Prediction Challenge**. It predicts backpack prices based on features like brand, material, capacity, and design using a **hyperparameter-tuned LightGBM model**. The solution is deployed as an interactive Flask web app with a user-friendly interface.  

## Key Features  
✅ **Price Prediction Model**  
- LightGBM regressor optimized with hyperparameter tuning (GridSearchCV/RandomizedSearchCV).  
- Preprocessing pipeline for handling categorical/numerical features.  
- Evaluation metrics: RMSE, R² score.  

✅ **Web Application**  
- Input form for users to specify backpack attributes (brand, size, material, etc.).  
- Real-time price prediction displayed with clear output.  
- Responsive UI built with Bootstrap, HTML, CSS, and JavaScript.  

✅ **Technical Stack**  
- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python (Flask)  
- **Machine Learning**: LightGBM, Scikit-learn, Pandas  
- **Tools**: Git, Jupyter Notebook (for model development)  

## How It Works  
1. **User Input**: Enter backpack details (e.g., brand, dimensions, material).  
2. **Model Prediction**: The trained LightGBM model processes features and predicts the price.  
3. **Result Display**: Predicted price is shown with optional confidence intervals.  

## Setup & Installation  
1. Clone the repository:  
   ```bash  
   git clone [GitHub_Repo_URL]  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the Flask app:  
   ```bash  
   python app.py  
   ```  

## Dataset  
- **Source**: Kaggle competition dataset (https://www.kaggle.com/competitions/playground-series-s5e2/data).  
- **Preprocessing**: Handled missing values, encoded categorical variables, scaled numerical features.  

## Performance  
- **Model Accuracy**: Achieved an RMSE of ~$38.92827 on the test set.  
- **Comparison**: Outperformed baseline models (Linear Regression, Random Forest and etc).  


## Future Enhancements  
- Include visualizations (e.g., feature importance plots).  

## GitHub Repository  
🔗 [GitHub Link](#) *(https://github.com/Sujeevan8300/Backpack-Price-Prediction)*  
