import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم نيون احترافي وحجم مدمج (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 32px !important; text-align: center; margin-bottom: 15px; }
    
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .sidebar-title { color: #00f2ff !important; text-align: center; font-size: 20px; font-weight: bold; text-shadow: 0 0 5px #00f2ff; margin-bottom: 15px; }
    
    .bot-text {
        background-color: #0d1a26; color: #00f2ff; border-right: 4px solid #00f2ff;
        padding: 12px; border-radius: 12px; margin-bottom: 10px;
        box-shadow: 0 0 8px rgba(0, 242, 255, 0.1); line-height: 1.5;
    }
    .user-text {
        background-color: #161b22; color: #ffffff; border-left: 4px solid #58a6ff;
        padding: 10px; border-radius: 10px; margin-bottom: 10px;
    }
    
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 2.8em; 
        background-color: #1f6feb; color: white; border: none; 
        font-weight: bold; font-size: 13px; transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #00f2ff !important; color: black !important; 
        box-shadow: 0 0 12px #00f2ff; transform: scale(1.02); 
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة
kb = {
    "تعريف": "بص يا بطل، **البيانات الضخمة** هي مجموعات بيانات ضخمة جداً ومعقدة، البرامج التقليدية مش بتقدر تعالجها، وبنحتاج أدوات ذكية لفهمها. 🔍",
    "خصائص": "**خصائص الـ 5Vs:** الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)، الموثوقية (Veracity)، والقيمة (Value). ⚡",
    "أهمية": "بتساعدنا في مجالات كتير زي: الطب، التجارة، المرور، والأمن السيبراني. 💎",
    "أنواع": "عندنا 3 أنواع: مهيكلة (جداول)، غير مهيكلة (صور وفيديو)، وشبه مهيكلة (JSON). 📂",
    "roadmap": "طريقك للنجاح: اتعلم Python، ثم SQL، ثم الإحصاء، وبعدها أدوات التخزين والمعالجة زي Hadoop و Spark. 🗺️",
    "مقارنة": "البيانات العادية: حجم صغير، تخزين في جهاز واحد، جداول منظمة. \nالبيانات الضخمة: حجم هائل، تخزين موزع، داتا متنوعة، وسرعة فائقة. ⚖️"
}

# 4. إدارة الحالة والأسئلة
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن إن الداتا صور وفيديوهات؟", "a": ["Variety (التنوع)", "Volume (الحجم)", "Value (القيمة)"], "correct": "Variety (التنوع)"},
    {"q": "أي أداة نستخدمها للجداول البسيطة والبيانات العادية؟", "a": ["Hadoop", "Excel", "Spark"], "correct": "Excel"}
]

# 5. الواجهة (Sidebar & Header)
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="sidebar-title">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.view = "quiz"
    if st.button("💬 ندردش"):
        st.session_state.view = "chat"
    
    st.markdown("---")
    st.subheader("🚀 وصول سريع")
    if st.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("📂 أنواع البيانات"): st.session_state.q_auto = "أنواع"
    if st.button("⚡ خصائص الـ 5Vs"): st.session_state.q_auto = "خصائص"
    if st.button("⚖️ الفرق بين البيانات"): st.session_state.q_auto = "مقارنة"
    if st.button("🗺️ الـ Roadmap"): st.session_state.q_auto = "roadmap"
    if st.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم بياني"

# 6. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 **تحدي:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("اختار الإجابة:", q_item["a"])
        if st.form_submit_button("إرسال"):
            if user_choice == q_item["correct"]:
                st.success("صح يا بطل! 🎯")
                st.balloons()
            else:
                st.error(f"للأسف خطأ.. الصح هو {q_item['correct']}")
else:
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    u_input = st.chat_input("اسألني عن أي حاجة في البيانات الضخمة...")
    query = u_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = "كلام جميل! حابب تعرف إيه تاني؟ 😊"
        chart_data = None
        q_low = query.lower()
        
        if any(w in q_low for w in ["تعريف", "ماهي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["أنواع", "انواع"]): res = kb["أنواع"]
        elif any(w in q_low for w in ["خصائص", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["مقارنة", "فرق"]): res = kb["مقارنة"]
        elif any(w in q_low for w in ["roadmap", "طريق"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            res = "ده رسم بياني بيوضح انفجار حجم البيانات عالمياً (بالزيتابايت) من 2010 لـ 2025: 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم (ZB)': [2, 15, 64, 180]}).set_index('السنة')
        
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.line_chart(chart_data)
        
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": res}
        if chart_data is not None: msg["chart"] = chart_data
        st.session_state.messages.append(msg)
