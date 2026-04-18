import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة وتنسيق الـ CSS
st.set_page_config(page_title="Big Data Hero", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 16px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 26px !important; text-align: center; margin-bottom: 20px; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; min-width: 280px; }
    
    /* جعل زرار القائمة ظاهر وواضح */
    [data-testid="stSidebarNav"] { padding-top: 20px; }
    
    /* تنسيق الأزرار الجانبية وتصغير الخط */
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        background-color: #1f6feb; 
        color: white; 
        height: 3em; 
        font-weight: normal; 
        font-size: 13px !important; 
        margin-bottom: 8px;
        border: 1px solid #58a6ff;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #388bfd;
        border: 1px solid #00f2ff;
        transform: scale(1.02);
    }
    
    /* زر العودة للعبة */
    .game-link {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #238636;
        color: white !important;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
        margin-top: 20px;
        border: 1px solid #3fb950;
    }
    
    /* تنسيق فقاعات الدردشة */
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 5px solid #00f2ff; padding: 15px; border-radius: 15px; margin-bottom: 15px; line-height: 1.6; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 5px solid #58a6ff; padding: 12px; border-radius: 12px; margin-bottom: 15px; }
    
    /* تنسيق المخطط */
    .step-box { border: 1px solid #00f2ff; padding: 10px; border-radius: 8px; margin: 5px 0; text-align: center; background: #0d1117; color: #00f2ff; font-weight: bold; }
    .arrow { text-align: center; color: #58a6ff; font-size: 20px; }
    
    /* إخفاء القوائم غير الضرورية مع الإبقاء على Header الخاص بالقائمة */
    #MainMenu, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات (Knowledge Base)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة تفوق قدرة البرامج التقليدية على المعالجة. 🔍",
    "خصائص": """تتميز بـ **الـ 5Vs**: (الحجم، السرعة، التنوع، الموثوقية، والقيمة). ✨""",
    "تغيير_الحياة": "بتسهل حياتنا من خلال تحسين الرعاية الصحية، تنظيم المرور، وتوفير تجربة تعليمية مخصصة! 🚀",
    "مجالات": "تستخدم في: الطب 🏥، التعليم 🎓، المرور 🚗، والتجارة 🛒.",
    "استفادة_تعلم": "تعلمها يفتح لك أبواب المستقبل في البرمجة وتحليل البيانات. 🌟",
    "برامج": "أهم البرامج: **Python**، **Hadoop**، **Spark**، و **Tableau**. 💻",
    "خطوات_ترتيب": """مخطط رحلة البيانات:
<div class="step-box">1. التجميع 📥</div>
<div class="arrow">⬇️</div>
<div class="step-box">2. التخزين 🗄️</div>
<div class="arrow">⬇️</div>
<div class="step-box">3. المعالجة 🧼</div>
<div class="arrow">⬇️</div>
<div class="step-box">4. التحليل 🧠</div>
<div class="arrow">⬇️</div>
<div class="step-box">5. التنفيذ ✅</div>""",
    "رسم_بياني": "حجم البيانات يتضاعف كل عامين، ومن المتوقع وصوله لـ 175 زيتابايت بحلول 2025! 📈"
}

# 3. إدارة الجلسة
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

# 4. الواجهة الجانبية (Sidebar)
with st.sidebar:
    st.markdown('<h1>Big Data Hero</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;text-align:center;font-size:13px;">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    
    if st.button("🔍 1. تعريف البيانات"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ 2. الخصائص والأهمية"): st.session_state.q_auto = "خصائص"
    if st.button("🚀 3. كيف تغير حياتنا؟"): st.session_state.q_auto = "تغيير"
    if st.button("🌍 4. مجالات الاستخدام"): st.session_state.q_auto = "مجالات"
    if st.button("📈 5. رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    
    st.markdown("---")
    if st.button("🎓 استفادة وبرامج التعلم"): st.session_state.q_auto = "استفادة"
    if st.button("⛓️ مخطط ترتيب البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبر ذكاءك"): st.session_state.view = "quiz"
    if st.button("💬 بدء دردشة جديدة"): 
        st.session_state.messages = []
        st.session_state.view = "chat"
    
    st.markdown('<a href="https://view.genially.com/69c2cab192730eedd4af164e" target="_blank" class="game-link">🎮 العودة إلى مغامرة البيانات</a>', unsafe_allow_html=True)

# 5. منطق العرض
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار الأبطال</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="bot-text">اختبر معلوماتك يا بطل!</div>', unsafe_allow_html=True)
        q1 = st.radio("1. ما هي الخاصية التي تعني 'تنوع' البيانات؟", ["Volume", "Variety", "Velocity"])
        q2 = st.radio("2. أي مرحلة تأتي أولاً؟", ["التحليل", "التجميع"])
        if st.button("تحقق من إجابتك"):
            if q1 == "Variety" and q2 == "التجميع": st.success("بطل! إجابات صحيحة 🎯")
            else: st.warning("حاول مرة أخرى!")
else:
    st.markdown("<h1>🤖 الوكيل الذكي للبيانات</h1>", unsafe_allow_html=True)
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اسألني أي شيء...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        ans = None
        q_low = query.lower()
        if "تعريف" in q_low or "1" in q_low: ans = kb["تعريف"]
        elif "خصائص" in q_low or "2" in q_low: ans = kb["خصائص"]
        elif "تغير" in q_low or "3" in q_low: ans = kb["تغيير_الحياة"]
        elif "مجالات" in q_low or "4" in q_low: ans = kb["مجالات"]
        elif "رسم" in q_low or "5" in q_low: ans = kb["رسم_بياني"]
        elif "استفادة" in q_low or "تعلم" in q_low: ans = kb["استفادة_تعلم"] + "\n\n" + kb["برامج"]
        elif "ترتيب" in q_low or "مخطط" in q_low: ans = kb["خطوات_ترتيب"]
        if ans is None: ans = "أنا هنا لمساعدتك! اختر موضوعاً من القائمة الجانبية."
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
