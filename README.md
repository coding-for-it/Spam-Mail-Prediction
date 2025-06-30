# **Spam Mail Prediction**

This project is a machine learning-based system that predicts whether an email is spam or not. It features a **Streamlit-based frontend** for user interaction and uses **pre-trained ML models** on **TF-IDF-transformed** text for prediction.

---

## **Project Structure**

- **`app.py`**: Streamlit application code for real-time spam email classification.
- **`spam_mail_prediction.ipynb`**: Jupyter notebook for data preprocessing, model training, and evaluation.
- **`models/`**: Stores trained models (`.pkl` files) for Logistic Regression, Naive Bayes, and Random Forest.
- **`data/`**: Contains the dataset `mail_data.csv`.
- **`output/`**: Contains visual outputs like `spam.png` and `not spam.png`.
- **`requirements.txt`**: Lists required Python packages.
- **`README.md`**: Overview and setup instructions for the project.

---

## **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/coding-for-it/spam-mail-prediction.git
   cd spam-mail-prediction

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
