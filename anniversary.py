import streamlit as st
from datetime import datetime, timedelta
import time

# Page config
st.set_page_config(
    page_title="Our 6 Months Together ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'show_message' not in st.session_state:
    st.session_state.show_message = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0
if 'show_jumpscare' not in st.session_state:
    st.session_state.show_jumpscare = False
if 'jumpscare_time' not in st.session_state:
    st.session_state.jumpscare_time = None

# Custom CSS with book animation
st.markdown("""
    <style>
    /* Love-themed background */
    .main {
        background: 
            linear-gradient(135deg, rgba(255, 105, 180, 0.3) 0%, rgba(255, 20, 147, 0.3) 100%),
            repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(255, 192, 203, 0.1) 35px, rgba(255, 192, 203, 0.1) 70px);
        background-color: #ff69b4;
        padding: 10px !important;
        position: relative;
    }
    .stApp {
        background: 
            linear-gradient(135deg, rgba(255, 105, 180, 0.8) 0%, rgba(255, 20, 147, 0.8) 100%),
            repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(255, 192, 203, 0.2) 35px, rgba(255, 192, 203, 0.2) 70px);
        background-color: #ff69b4;
    }
    .stApp::before {
        content: '💕';
        position: fixed;
        top: 10%;
        left: 5%;
        font-size: 3em;
        opacity: 0.15;
        animation: float 6s ease-in-out infinite;
    }
    .stApp::after {
        content: '❤️';
        position: fixed;
        bottom: 10%;
        right: 5%;
        font-size: 3em;
        opacity: 0.15;
        animation: float 8s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    .block-container {
        padding: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Book styling */
    .book-container {
        perspective: 1500px;
        margin: 20px auto;
        max-width: 100%;
    }
    
    .book-page {
        background: linear-gradient(to right, #ffffff 0%, #fff5f7 100%);
        padding: 30px 25px;
        border-radius: 15px;
        box-shadow: 
            0 10px 40px rgba(233, 30, 99, 0.2),
            inset 0 0 0 1px rgba(255, 182, 193, 0.3);
        margin: 15px 0;
        position: relative;
        animation: pageFlip 0.6s ease-in-out;
        min-height: 400px;
    }
    
    @keyframes pageFlip {
        0% {
            transform: rotateY(-90deg);
            opacity: 0;
        }
        100% {
            transform: rotateY(0deg);
            opacity: 1;
        }
    }
    
    .book-page::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 3px;
        height: 100%;
        background: linear-gradient(to bottom, 
            rgba(233, 30, 99, 0.2) 0%, 
            rgba(255, 105, 180, 0.1) 50%, 
            rgba(233, 30, 99, 0.2) 100%);
        border-radius: 15px 0 0 15px;
    }
    
    .page-number {
        position: absolute;
        bottom: 15px;
        right: 25px;
        color: #ff69b4;
        font-style: italic;
        font-size: 0.9em;
    }
    
    .title-text {
        color: white;
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
        line-height: 1.3;
    }
    
    .subtitle-text {
        color: white;
        text-align: center;
        font-size: 1.1em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    
    .month-title {
        color: #ff1493;
        font-size: 1.8em;
        font-weight: bold;
        margin-bottom: 15px;
        text-align: center;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.3);
    }
    
    .page-title {
        color: #ff69b4;
        font-size: 1.3em;
        font-weight: 600;
        margin-bottom: 15px;
        text-align: center;
    }
    
    /* Image container for consistent sizing */
    .stImage {
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.3);
        overflow: hidden;
    }
    .stImage img {
        width: 100% !important;
        height: 350px !important;
        object-fit: cover !important;
        object-position: center !important;
        border-radius: 15px;
    }
    
    .page-text {
        color: #333;
        font-size: 1.05em;
        line-height: 1.8;
        text-align: justify;
        font-family: 'Georgia', serif;
    }
    
    .nav-button {
        background: white;
        border: none;
        padding: 15px 25px;
        border-radius: 25px;
        font-size: 1.1em;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .secret-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.8em;
        font-weight: bold;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    
    .stat-box {
        background: white;
        padding: 15px 10px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 5px;
    }
    
    .stat-number {
        font-size: 2em;
        font-weight: bold;
        color: #ff1493;
    }
    
    .stat-label {
        font-size: 0.9em;
        color: #666;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .title-text { font-size: 1.8em; }
        .subtitle-text { font-size: 1em; }
        .month-title { font-size: 1.5em; }
        .page-title { font-size: 1.1em; }
        .page-text { font-size: 1em; }
        .book-page { padding: 20px 15px; min-height: 350px; }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title-text">❤️ Our 6 Months<br>Together ❤️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">A Love Story in 6 Chapters</p>', unsafe_allow_html=True)

# Email Icon Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("✉️", key="email_btn", help="Click me!", use_container_width=True):
        if not st.session_state.show_jumpscare:
            # First click - show jumpscare
            st.session_state.show_jumpscare = True
            st.session_state.jumpscare_time = time.time()
            st.session_state.show_message = False
            st.rerun()
        else:
            # Toggle message after jumpscare
            st.session_state.show_message = not st.session_state.show_message

# Show FULLSCREEN JUMPSCARE!
if st.session_state.show_jumpscare:
    # Check if 3 seconds have passed
    if st.session_state.jumpscare_time and (time.time() - st.session_state.jumpscare_time) >= 3:
        # Hide jumpscare and show message
        st.session_state.show_jumpscare = False
        st.session_state.show_message = True
        st.rerun()
    else:
        # Show the jumpscare
        import base64
        try:
            with open("picture1.jpg", "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            
            st.markdown(f"""
                <div class="jumpscare-overlay">
                    <img src="data:image/jpeg;base64,{img_data}" alt="BOO!">
                </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
                <div class="jumpscare-overlay">
                    <h1 style="color: red; font-size: 5em;">👻 BOO! 👻</h1>
                </div>
            """, unsafe_allow_html=True)
        
        # Wait and rerun
        time.sleep(3)
        st.rerun()

# Show secret message if clicked (after jumpscare)
elif st.session_state.show_message:
    st.markdown("""
        <div class="secret-message">
            💕 Happy 6 Months Bhe! 💕
        </div>
    """, unsafe_allow_html=True)
    st.balloons()

# Calculate days together
start_date = datetime(2025, 4, 11)  # Our special day - April 11, 2025
today = datetime.now()
days_together = (today - start_date).days

# Stats section
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">6</div>
            <div class="stat-label">Months</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">∞</div>
            <div class="stat-label">Memories</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{days_together}</div>
            <div class="stat-label">Days</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">1</div>
            <div class="stat-label">Love</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Book pages content
pages = [
    {
        "month": "Chapter 1",
        "emoji": "✨",
        "title": "The Beginning",
        "message": "From the moment we met, I knew there was something special about you. Every conversation, every laugh, every moment felt like magic. You walked into my life and changed everything. It was like finding the missing piece I didn't know I was looking for."
    },
    {
        "month": "Chapter 2",
        "emoji": "🌸",
        "title": "Growing Closer",
        "message": "With each passing day, I discovered more reasons to fall for you. Your smile, your kindness, the way you make me laugh - everything about you just feels right. We started creating our own little world together, filled with inside jokes and sweet moments."
    },
    {
        "month": "Chapter 3",
        "emoji": "🎈",
        "title": "First Adventures",
        "message": "Remember all our adventures? Every moment with you is an adventure, whether we're exploring new places or just spending quiet time together. You make ordinary moments extraordinary. Each memory we create together becomes a treasure I hold close to my heart."
    },
    {
        "month": "Chapter 4",
        "emoji": "💕",
        "title": "Falling Deeper",
        "message": "By now, I was completely sure - you're the one I want by my side. The way we understand each other, support each other, and bring out the best in one another is something truly special. You've become my best friend, my confidant, my everything."
    },
    {
        "month": "Chapter 5",
        "emoji": "🌟",
        "title": "Dreams Together",
        "message": "We started dreaming about the future, making plans, and building something beautiful together. Every day with you feels like a step toward forever, and I can't wait to see where this journey takes us. Our dreams are intertwined now, and that makes them even more beautiful."
    },
    {
        "month": "Chapter 6",
        "emoji": "❤️",
        "title": "Here We Are",
        "message": "And here we are - six incredible months together. Thank you for every smile, every hug, every moment of joy. You've made these months the happiest of my life, and this is just the beginning of our story. I love you more with each passing day, and I can't wait for all the chapters yet to come."
    }
]

# Display current page
current_page = st.session_state.current_page

st.markdown('<div class="book-container">', unsafe_allow_html=True)
page = pages[current_page]
st.markdown(f"""
    <div class="book-page" key="{current_page}">
        <p class="month-title">{page['emoji']} {page['month']}</p>
        <p class="page-title">{page['title']}</p>
        <p class="page-text">{page['message']}</p>
        <p class="page-number">Page {current_page + 1} of 6</p>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Display images for current month with consistent sizing
image_files = {
    0: ["month1.jpg", "month1.1.jpg"],  # Month 1 has 2 photos
    1: ["month2.jpg"],                   # Month 2 has 1 photo
    2: ["month3.jpg", "month3.3.jpg"],  # Month 3 has 2 photos
    3: ["month4.jpg"],                   # Month 4 has 1 photo
    4: ["month5.jpg"],                   # Month 5 has 1 photo
    5: ["month6.jpg"]                    # Month 6 has 1 photo
}

# Display images for the current page - all same size
if current_page in image_files:
    images = image_files[current_page]
    if len(images) == 1:
        # Single image - full width, fixed height
        st.image(images[0], use_container_width=True)
    else:
        # Multiple images - side by side, same height
        cols = st.columns(len(images))
        for idx, img in enumerate(images):
            with cols[idx]:
                st.image(img, use_container_width=True)
else:
    st.info(f"📷 Add your special photo from Month {current_page + 1} here!")

# Navigation buttons
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if current_page > 0:
        if st.button("⬅️ Previous", key="prev", use_container_width=True):
            st.session_state.current_page -= 1
            st.rerun()

with col3:
    if current_page < 5:
        if st.button("Next ➡️", key="next", use_container_width=True):
            st.session_state.current_page += 1
            st.rerun()

# Progress indicator
st.markdown("<br>", unsafe_allow_html=True)
progress_text = f"📖 Page {current_page + 1} of 6"
st.markdown(f"<p style='text-align: center; color: white; font-size: 1.1em;'>{progress_text}</p>", unsafe_allow_html=True)

# Final message on last page
if current_page == 5:
    st.markdown("---")
    st.markdown("""
        <div class="secret-message">
            💌 Happy 6 Month Anniversary, My Love! 💕<br>
            <span style="font-size: 0.6em;">Here's to forever together...</span>
        </div>
    """, unsafe_allow_html=True)