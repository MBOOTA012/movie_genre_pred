import streamlit as st
import pickle

# Load the trained model
with open("svm_genre_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit app interface
st.set_page_config(page_title="🎬 Movie Genre Predictor", layout="centered")

st.title("🎬 Movie Genre Predictor")
st.markdown("Enter a movie description below, and the app will predict its most likely **genre** using a trained SVM model.")

# Input box
user_input = st.text_area("📝 Enter Movie Description", height=200, placeholder="Example: A team of heroes fights to save the galaxy from an alien warlord...")

# Predict button
if st.button("🔍 Predict Genre"):
    if user_input.strip() == "":
        st.warning("Please enter a movie description.")
    else:
        predicted_genre = model.predict([user_input])[0]
        st.success(f"🎯 **Predicted Genre:** {predicted_genre}")
