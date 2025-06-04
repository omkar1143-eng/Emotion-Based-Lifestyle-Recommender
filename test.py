import cv2
import streamlit as st

def take_input():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("❌ Cannot open camera")
        return

    ret, frame = cap.read()
    if not ret:
        st.error("❌ Failed to grab frame")
        return

    st.image(frame, channels="BGR")  # Streamlit-friendly display

    # ✅ Save the captured image so app.py can use it
    cv2.imwrite("photo.jpg", frame)

    cap.release()