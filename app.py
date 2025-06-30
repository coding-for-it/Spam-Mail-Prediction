import streamlit as st
import joblib

# Load vectorizer and model from files
vectorizer = joblib.load('models/vectorizer.pkl')
model = joblib.load('models/naive_model.pkl')  # Or rf_model.pkl / logistic_model.pkl

# Streamlit UI
st.title("Spam Mail Classifier")
st.markdown("Enter an email below to check whether it's **Spam** or **Not Spam**.")

user_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vect = vectorizer.transform([user_input])  #Use saved vectorizer
        prediction = model.predict(input_vect)[0]

        if prediction == 1:
            st.success("Not Spam:-)")
        else:
            st.error("Spam")
