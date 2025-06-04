
# 🎭 Emotion-Based Lifestyle Recommender


## 🧠 Project Overview

**Emotion-Based Lifestyle Recommender** is a Streamlit-based smart assistant that uses real-time facial emotion detection to recommend **music**, **food**, **activities**, **travel destinations**, and **mental wellness tips**.

Whether you're feeling happy, sad, angry, or just neutral, this app suggests personalized ways to match or improve your mood.

---

## 🎯 Key Features

- 🧠 **Real-Time Emotion Detection** using DeepFace and OpenCV  
- 🎧 **Spotify Song Recommendations** by detected mood  
- 🍽️ **Food Suggestions** with Swiggy links  
- 🧘 **Mental Health Tips & Quotes** for emotional support  
- 🧳 **Travel Destination Ideas** per emotion  
- 💡 **Fun Activities** to uplift the user  

---

## 🛠️ Technologies Used

- `Streamlit`: Front-end web framework
- `OpenCV`: Webcam and image processing
- `DeepFace`: Facial emotion recognition
- `Spotify API & Spotipy`: Music search and embedding
- `Matplotlib`: Image display
- `Python`: Core logic

---

## 🚀 How to Run the Application

### 📦 Prerequisites

Install all required packages with:

```bash
pip install -r requirements.txt
```

### ▶️ Running the App

```bash
streamlit run app.py
```

Make sure your webcam is enabled and functional.

---

## 🧪 Demo Workflow

1. Launch the Streamlit app.
2. Click **📸 Capture Image** to take a picture using your webcam.
3. The app detects your **dominant emotion** using DeepFace.
4. Get customized recommendations:
   - 🎵 Spotify song embed
   - 🍲 Food to order
   - 💡 Mood-boosting activity
   - ✈️ Travel destination with links
   - 🧘‍♀️ Mental health suggestions if needed

---

## 🧠 Example Emotions & Responses

| Emotion  | Music Suggestion | Activity Idea | Food | Travel |
|----------|------------------|----------------|------|--------|
| Happy    | Upbeat song      | Go for a walk | Ice cream | Goa |
| Sad      | Comfort tune     | Journal your thoughts | Soup | Munnar |
| Angry    | Chill beats      | Jog or box | Spicy noodles | Rishikesh |
| Fear     | Calming melody   | Talk to a friend | Biryani | Coorg |
| Surprise | Celebration vibe | Call someone | Waffles | Manali |

---


## 🔐 Notes

- The `embed.py` script includes Spotify Client credentials. Avoid sharing this file publicly without hiding sensitive keys.
- Webcam permission is required to run the app.

---

## ✅ Future Enhancements

- [ ] Store user preferences
- [ ] Add voice-based sentiment analysis
- [ ] Optimize DeepFace model switching (e.g., ArcFace, FaceNet)
- [ ] Mobile responsiveness improvements
- [ ] Deploy online using Streamlit Cloud or similar

---

## 👨‍💻 Author

**Kandukuri Omkar**  
📧 [omkark5125@gmail.com](mailto:omkark5125@gmail.com)

---
