import streamlit as st
import random

# 1. VEB-SAYTNING ASOSIY SOZLAMALARI VA DIZAYNI
st.set_page_config(page_title="Zukko Bolajon - O'quv Markazi", page_icon="🎒", layout="centered")

# Bolalarga mos yorqin va quvnoq dizayn (CSS)
st.markdown("""
    <style>
    /* Umumiy fon */
    .stApp {
        background-color: #f0f8ff;
        color: #333333;
    }
    
    /* Bosh sarlavha */
    .main-title {
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #ff4b4b;
        font-size: 3rem;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #1e90ff;
        font-size: 1.5rem;
        margin-bottom: 30px;
    }
    
    /* Kurs kartochkalari */
    .course-card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border: 3px solid #ffd700;
        margin-bottom: 20px;
    }
    
    /* Sidebar menyusi */
    section[data-testid="stSidebar"] {
        background-color: #ffe4e1 !important;
    }
    
    /* Tugmalar */
    div.stButton > button {
        background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(255, 105, 180, 0.4) !important;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Bosh sarlavhalar
st.markdown("<h1 class='main-title'>🎒 ZUKKO BOLAJON</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Sizning sevimli aqlli maktabingiz! 🚀</p>", unsafe_allow_html=True)

# 2. YON PANEL (SIDEBAR) NAVIGATSIYASI
st.sidebar.markdown("<h2 style='text-align:center; color:#ff4b4b; font-family:Comic Sans MS;'>🗺️ BILIMLAR OLAMI</h2>", unsafe_allow_html=True)
sahifa = st.sidebar.radio("Qaysi fanni o'rganamiz?", ["🏠 Bosh sahifa", "🔢 Quvnoq Matematika", "🌍 Tabiatshunoslik (Dunyo tanish)", "🇬🇧 Ingliz tili alifbosi"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align:center; color:#555; font-weight:bold;'>✨ Bilim olish - eng katta boylik! ✨</p>", unsafe_allow_html=True)

# ==============================================================================
# 1. BOSH SAHIFA
# ==============================================================================
if sahifa == "🏠 Bosh sahifa":
    st.markdown("""
        <div class='course-card'>
            <h2>👋 Salom, kichik aqlli do'stim!</h2>
            <p style='font-size: 1.2rem; line-height: 1.6;'>
                Zukko Bolajon platformasiga xush kelibsiz! Bu yerda siz zerikarli darslarni unutasiz. 
                Chap tarafdagi menyu orqali o'zingizga yoqqan fanni tanlang va qiziqarli sayohatni boshlang! 🎉
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📚 Bizning darslarimiz:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🔢 **Matematika**\n\nQo'shish va ayirishni o'yinlar orqali o'rganamiz.")
    with col2:
        st.success("🌍 **Tabiatshunoslik**\n\nYaylovlar, hayvonlar va sayyoramiz sirlari.")
    with col3:
        st.warning("🇬🇧 **Ingliz tili**\n\nAlifbo va birinchi so'zlarni quvnoq yodlaymiz.")

# ==============================================================================
# 2. QUVNOQ MATEMATIKA
# ==============================================================================
elif sahifa == "🔢 Quvnoq Matematika":
    st.markdown("<div class='course-card' style='border-color: #1e90ff;'><h2>🔢 Quvnoq Matematika darsi</h2><p>Bugun biz raqamlarni qo'shishni o'rganamiz!</p></div>", unsafe_allow_html=True)
    
    st.subheader("💡 Qoida bilan tanishamiz:")
    st.success("Sizda 2 ta olma bor edi 🍎🍎. Oyijoningiz yana 3 ta olma berdi 🍎🍎🍎. Jami sizda 5 ta olma bo'ldi! Ya'ni: 2 + 3 = 5")
    
    st.markdown("---")
    st.subheader("🧠 O'zingni sinab ko'r! (Kichik O'yin)")
    
    # Oddiy savol-javob o'yini
    st.write("Misolni yeching: **4 + 5 = ?**")
    javob = st.number_input("Javobingizni yozing:", min_value=0, max_value=20, step=1)
    
    if st.button("Tekshirish 🎯"):
        if javob == 9:
            st.balloons()
            st.success("🎉 Barakalla! To'g'ri javob: 9! Siz haqiqiy matematikiz! 🌟")
        else:
            st.error("❌ O'ylab ko'ring, qaytadan urinib ko'ring! Siz albatta uddalaysiz! 💪")

# ==============================================================================
# 3. TABIATSHUNOSLIK
# ==============================================================================
elif sahifa == "🌍 Tabiatshunoslik (Dunyo tanish)":
    st.markdown("<div class='course-card' style='border-color: #2ed573;'><h2>🌍 Jonli Tabiat va Hayvonot Olami</h2><p>Biz yashayotgan dunyo juda ajoyib va mo'jizalarga boy!</p></div>", unsafe_allow_html=True)
    
    st.subheader("🦁 Hayvonlar haqida qiziqarli faktlar:")
    st.info("🦒 **Jirafa** — dunyodagi eng uzun bo'yinli hayvon. U hatto daraxtlarning eng tepasidagi barglarni ham bemalol yeya oladi!")
    st.info("🐋 **Ko'k kit** — dunyodagi eng katta jonzot. Uning tili vazni bitta filning vazniga teng keladi!")
    
    st.markdown("---")
    st.subheader("❓ Tezkor Savol-Javob:")
    savol = st.radio("Dunyodagi eng tez yuguradigan hayvon qaysi?", ["Fil 🐘", "To'tiqush 🦜", "Gepard (Qoplon) 🐆"])
    
    if st.button("Javobni tasdiqlash 🌲"):
        if savol == "Gepard (Qoplon) 🐆":
            st.success("🎉 To'g'ri! Gepard soatiga 100 km dan tezroq yugura oladi! ⚡")
        else:
            st.warning("Uh, bu emas. Boshqa hayvonni tanlab ko'ring! 🐆")

# ==============================================================================
# 4. INGLIZ TILI ALIFBOSI
# ==============================================================================
elif sahifa == "🇬🇧 Ingliz tili alifbosi":
    st.markdown("<div class='course-card' style='border-color: #ffa500;'><h2>🇬🇧 English for Kids</h2><p>Ingliz tilini birinchi harflardan o'rganamiz!</p></div>", unsafe_allow_html=True)
    
    st.subheader("🅰️ Alifbo harflari va so'zlar:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h3 style='color:#ff4b4b; text-align:center;'>🍎 A</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align:center;'><b>Apple</b><br>(Olma)</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='color:#1e90ff; text-align:center;'>🧸 B</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align:center;'><b>Bear</b><br>(Ayiq)</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<h3 style='color:#2ed573; text-align:center;'>🐱 C</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align:center;'><b>Cat</b><br>(Mushuk)</p>", unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("🎮 So'z topish o'yini:")
    st.write("Ingliz tilida **'Mushuk'** qanday yoziladi?")
    mushuk_javob = st.text_input("Harflarni kiriting (masalan: dog, apple...):").strip().lower()
    
    if st.button("Tekshirib ko'rish 🇬🇧"):
        if mushuk_javob == "cat":
            st.balloons()
            st.success("🎉 Super! To'g'ri, Mushuk ingliz tilida 'Cat' bo'ladi! 🐱")
        else:
            st.error("❌ Noto'g'ri. Kichik eslatma: Yuqoridagi rasmli harflarga yaxshilab e'tibor bering! 😉")
