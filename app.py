import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import random
import test

# Layout containers
header = st.container()
inp = st.container()
pred = st.container()

# Header section
with header:
    st.title('🎵Lifestyle Recommendation based on Emotion')
    st.image('emo.png')
    st.markdown('**Aim : To detect the emotion of the person and predict a song, food, activity, and more**')

# Define song sets
song_sets = {
    'happy': ['https://open.spotify.com/track/02Ck2nLoW3TpgGV6uwvK5Z', 'https://open.spotify.com/track/3bTnREOf1CyY4Gz5jfHUiI?si=62d6ac1186044c01', 'https://open.spotify.com/track/6reHcXJekQ2csk0UazSBV1'],
    'sad': ['https://open.spotify.com/track/57zEYntUat0ofbFpoicN26', 'https://open.spotify.com/track/6zdikHQs2PBFgGIZBxqOeV', 'https://open.spotify.com/track/4Q2ulAxP62EOIXmdAVUh1w?si=bdddd4247b6b413d'],
    'angry': ['https://open.spotify.com/track/75IywzsrO67PjCrFHnA9tb?si=6e9aac33b61a4229', 'https://open.spotify.com/track/1YKPRycM3GzKbZUYDgLrmn?si=7c7e0aa843f14add', 'https://open.spotify.com/track/538V6gFAnhcLZrg6I8lIMI'],
    'neutral': ['https://open.spotify.com/track/1418IuVKQPTYqt7QNJ9RXN', 'https://open.spotify.com/track/5OMUXgfXsSukZ0zxelpC3b', 'https://open.spotify.com/track/7JGgKHHDgJCJkQCQxyHHdl'],
    'fear': ['https://open.spotify.com/track/6SfEAt8HbFLrC8XiiBEU7s?si=18fd3f74e33c49b2', 'https://open.spotify.com/track/7LBnxqvqIdeDazVYhtMMpg?si=834d7361c0e84ba1', 'https://open.spotify.com/track/3Hz8bwNyZPOzlz74dhuysC?si=221926b3fc114f75'],
    'disgust': ['https://open.spotify.com/track/7KXjTSCq5nL1LoYtL7XAwS', 'https://open.spotify.com/track/1rgnBhdG2JDFTbYkYRZAku', 'https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m'],
    'surprise': ['https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK', 'https://open.spotify.com/track/7e89621JPkKaeDSTQ3avtg', 'https://open.spotify.com/track/5CtI0qwDJkDQGwXD1H1cLb']
}

# Activities
activities = {
    'happy': ['Go for a walk 🎒', 'Dance to music 💃', 'Hang out with friends 👯‍♂️'],
    'sad': ['Journal your thoughts 📝', 'Watch your comfort movie 🎥', 'Sip hot chocolate ☕'],
    'angry': ['Go for a jog 🏃‍♂️', 'Do a boxing workout 🥊', 'Listen to calming tunes 🎧'],
    'neutral': ['Do a crossword 🧩', 'Clean your workspace 🧹', 'Try drawing something ✏️'],
    'fear': ['Talk to a friend 📞', 'Do guided breathing 🌬️', 'Hug your pet 🐶'],
    'disgust': ['Watch a funny video 😂', 'Try baking a dessert 🍰', 'Go outside for fresh air 🌳'],
    'surprise': ['Celebrate something! 🎉', 'Call someone special 📲', 'Take a spontaneous selfie 🤳']
}

# Travel ideas with destination links per emotion
travel_destinations = {
    'happy': [('Beach holiday in Goa 🏖️', 'https://www.tripadvisor.in/Tourism-g297604-Goa-Vacations.html')],
    'sad': [('Hill retreat in Munnar 🌄', 'https://www.keralatourism.org/destination/munnar/202')],
    'angry': [('Peaceful stay in Rishikesh 🧘', 'https://uttarakhandtourism.gov.in/destination/rishikesh')],
    'fear': [('Nature escape to Coorg 🌲', 'https://karnatakatourism.org/tour-item/coorg/')],
    'disgust': [('Wellness trip to Auroville 🌿', 'https://auroville.org/'),],
    'neutral': [('City break in Bangalore 🏙️', 'https://www.bangaloretourism.in/')],
    'surprise': [('Adventure trip to Manali 🏔️', 'https://himachaltourism.gov.in/destination/manali/')]
}

# Therapy tips
therapy_tips = [
    "You're stronger than you feel 💪",
    "Take it one breath at a time 🌬️",
    "Rest is productive too 🛌",
    "Talk to someone you trust 💬"
]

# Food suggestions with Swiggy links
food_links = {
    'happy': [('Chocolate Lava Cake 🍫', 'https://www.swiggy.com/search?query=chocolate%20lava%20cake'), ('Ice Cream Sundae 🍨', 'https://www.swiggy.com/search?query=ice%20cream')],
    'sad': [('Mac and Cheese 🧀', 'https://www.swiggy.com/search?query=mac%20and%20cheese'), ('Hot Soup 🍲', 'https://www.swiggy.com/search?query=soup')],
    'angry': [('Spicy Noodles 🌶️', 'https://www.swiggy.com/search?query=spicy%20noodles'), ('Sushi 🍣', 'https://www.swiggy.com/search?query=sushi')],
    'neutral': [('Classic Burger 🍔', 'https://www.swiggy.com/search?query=burger'), ('Pasta 🍝', 'https://www.swiggy.com/search?query=pasta')],
    'fear': [('Comforting Biryani 🍛', 'https://www.swiggy.com/search?query=biryani'), ('Milkshake 🥤', 'https://www.swiggy.com/search?query=milkshake')],
    'disgust': [('Cheesy Pizza 🍕', 'https://www.swiggy.com/search?query=pizza'), ('Nachos & Dip 🧀', 'https://www.swiggy.com/search?query=nachos')],
    'surprise': [('Waffles with Syrup 🧇', 'https://www.swiggy.com/search?query=waffles'), ('Momos 🥟', 'https://www.swiggy.com/search?query=momos')]
}

# Helper: extract track ID
def extract_track_id(url_or_id):
    if 'open.spotify.com' in url_or_id:
        return url_or_id.split('/')[-1].split('?')[0]
    return url_or_id

# Image input section
with inp:
    st.title("📷 Image Capture")
    st.markdown("**Capture an image of your face using your webcam**")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if st.button("📸 Capture Image"):
        test.take_input()  # Saves photo.jpg

# Prediction & Recommendation
with pred:
    st.title("🎶 Let's see what songs, food, and activities fit your mood!")

    img = cv2.imread('photo.jpg')

    if img is None:
        st.error("❌ Couldn't load image. Please try capturing again.")
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        st.pyplot(plt)

        with st.spinner('Analyzing your emotion...'):
            predictions = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

        if not predictions or 'dominant_emotion' not in predictions[0]:
            st.error("🙈 No face detected or emotion not found. Please try again.")
        else:
            emotion = predictions[0]['dominant_emotion'].lower()
            st.markdown(f"**Detected Emotion:** `{emotion}`")

            # 🎵 Music
            selected_song = random.choice(song_sets.get(emotion, song_sets['neutral']))
            track_id = extract_track_id(selected_song)
            st.subheader("🎧 Mood-Based Music")
            st.markdown(f'''
                <iframe src="https://open.spotify.com/embed/track/{track_id}" 
                        width="300" height="100" frameborder="0" 
                        allowtransparency="true" allow="encrypted-media"></iframe>
            ''', unsafe_allow_html=True)

            # 💡 Activity
            st.subheader("💡 Suggested Activity")
            st.markdown(f"`{random.choice(activities.get(emotion, activities['neutral']))}`")

            # 🍽️ Food
            st.subheader("🍴 Food Recommendation")
            food_name, food_url = random.choice(food_links.get(emotion, food_links['neutral']))
            st.markdown(f"**{food_name}** - [Order Now]({food_url})")

            # ✈️ Travel Suggestion
            st.subheader("✈️ Travel Suggestion")
            travel_name, travel_url = random.choice(travel_destinations.get(emotion, travel_destinations['neutral']))
            st.markdown(f"**{travel_name}** - [Explore]({travel_url})")

            # 🧠 Therapy if negative
            if emotion in ['sad', 'angry', 'fear', 'disgust']:
                st.subheader("🧠 Mental Wellness Tip")
                st.info(random.choice(therapy_tips))

                # 🧘 Extra Care Section
                st.markdown("---")
                st.subheader("🧘 Relaxation Tip")
                st.markdown("**Try a quick meditation:** [Headspace Guide](https://www.youtube.com/watch?v=c1Ndym-IsQg)")
                st.subheader("📚 Read a Quote")
                st.markdown(random.choice([
                    "*Keep going. Everything you need will come to you.*",
                    "*Be proud of how far you’ve come.*",
                    "*Your only limit is your mind.*",
                    "*You are more than your thoughts.*"
                ]))
