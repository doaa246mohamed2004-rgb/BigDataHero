import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero", layout="wide")

# 2. تصميم UI
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 30px !important; text-align: center; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 4px solid #00f2ff; padding: 12px; border-radius: 12px; margin-bottom: 10px; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 4px solid #58a6ff; padding: 10px; border-radius: 10px; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #1f6feb; color: white; height: 2.8em; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات (بدون فواصل عربية في الأكواد)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة بتيجي من مصادر كتير. 🔍",
    "خصائص": "خصائص الـ 5Vs هي: الحجم، السرعة، التنوع، الموثوقية، والقيمة. ⚡",
    "وظائف": "من وظائفها: عالم بيانات، مهندس بيانات، ومحلل بيانات. 💼",
    "تعليم": "بتساعد في تخصيص المحتوى لكل طالب حسب مستواه وسرعته. 🎓",
    "استفادة": "بتوفر فرص عمل بمرتبات عالية وتنمي مهارات التفكير المنطقي. 🌟",
    "أهمية": "بتساعد في كشف الأنماط الخفية وتطوير العلاجات الطبية وتأمين البنوك. 💎"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"

quiz_data = [
    {"q": "هل يمكن تخزين البيانات الضخمة على جهاز واحد؟", "a": ["نعم", "لا"], "correct": "لا"},
    {"q": "بايثون هي اللغة الأهم في تحليل البيانات؟", "a": ["صح", "خطأ"], "correct": "صح"}
]

# 5. الواجهة
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p style="color:#00f2ff;text-align:center;">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.view = "quiz"
    if st.button("💬 ندردش سوا"):
        st.session_state.messages = []
        st.session_state.view = "chat"
    st.markdown("---")
    if st.button("🔍 التعريف"): st.session_state.q_auto = "تعريف"
    if st.button("💼 الوظائف"): st.session_state.q_auto = "وظائف"
    if st.button("🎓 التعليم"): st.session_state.q_auto = "تعليم"

# 6. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz"):
        choice = st.radio("الإجابة:", q_item["a"])
        if st.form_submit_button("إرسال"):
            if choice == q_item["correct"]: st.success("صح! 🎯")
            else: st.error("حاول تاني!")
else:
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">مرحباً بك! أنا وكيلك الذكي. اسألني عن أي شيء! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اكتب سؤالك هنا...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = "حابب تعرف إيه تاني؟ 😊"
        if "تعريف" in query or "ماهي" in query: ans = kb["تعريف"]
        elif "خصائص" in query: ans = kb["خصائص"]
        elif "تعليم" in query: ans = kb["تعليم"]
        elif "وظائف" in query: ans = kb["وظائف"]
        elif "أهمية" in query: ans = kb["أهمية"]
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
