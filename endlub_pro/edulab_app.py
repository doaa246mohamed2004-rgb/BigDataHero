import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero", layout="wide")

# 2. تصميم الواجهة (UI)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 30px !important; text-align: center; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 4px solid #00f2ff; padding: 12px; border-radius: 12px; margin-bottom: 10px; line-height: 1.6; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 4px solid #58a6ff; padding: 10px; border-radius: 10px; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #1f6feb; color: white; height: 2.8em; font-weight: bold; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات المطورة (تشمل كل طلباتك)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة تفوق قدرة البرامج التقليدية على المعالجة. 🔍",
    "خصائص": "خصائص الـ 5Vs هي: الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)، الموثوقية (Veracity)، والقيمة (Value). ⚡",
    "مجالات": "تنتشر في: الطب، البنوك، التجارة الإلكترونية، المواصلات، الفضاء، والمدن الذكية. 🌍",
    "تعليم": "في التعليم: توفر 'التعلم الشخصي'، وتتوقع مستوى الطلاب المتعثرين، وتساعد في تطوير المناهج الرقمية. 🎓",
    "استفادة": "الاستفادة: توفر فرص عمل بمرتبات مرتفعة، وتنمي مهارة حل المشكلات واتخاذ القرارات الذكية بناءً على الحقائق. 🌟",
    "مقارنة": "الفرق: البيانات العادية محدودة الحجم وتخزن في جهاز واحد، بينما الضخمة هائلة وموزعة عبر آلاف الأجهزة. ⚖️",
    "طب": "في الطب: تستخدم في تشخيص الأمراض مبكراً، واكتشاف علاجات جديدة، ومراقبة صحة المرضى عن بُعد. 🏥",
    "تغيير_الحياة": "تغير حياتنا بجعل المدن أذكى، والخدمات أسرع، وتقديم حلول دقيقة لمشاكل الفقر، المناخ، والصحة العامة. 🚀",
    "هدف_اللعبة": "في اللعبة دي، بنتعلم إزاي نحول الأرقام الضخمة لمعلومات مفيدة تحل مشاكل العالم الحقيقي! 🎮"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"

quiz_data = [
    {"q": "هل البيانات الضخمة تخزن في جهاز كمبيوتر واحد؟", "a": ["نعم", "لا"], "correct": "لا"},
    {"q": "من مجالات البيانات الضخمة الطب والتعليم؟", "a": ["صح", "خطأ"], "correct": "صح"}
]

# 5. الواجهة الأساسية
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p style="color:#00f2ff;text-align:center;font-weight:bold;">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.view = "quiz"
    if st.button("💬 ندردش سوا"):
        st.session_state.messages = []
        st.session_state.view = "chat"
    
    st.markdown("---")
    st.subheader("🚀 وصول سريع")
    if st.button("🔍 التعريف والفرق"): st.session_state.q_auto = "فرق"
    if st.button("🏥 في الطب"): st.session_state.q_auto = "طب"
    if st.button("🎓 في التعليم"): st.session_state.q_auto = "تعليم"
    if st.button("🌍 كيف تغير حياتنا؟"): st.session_state.q_auto = "تغيير"
    if st.button("💼 الفوائد والمجالات"): st.session_state.q_auto = "فوائد"

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
        st.markdown('<div class="bot-text">مرحباً بك يا بطل! أنا وكيلك الذكي. اسألني عن أي شيء في عالم البيانات الضخمة! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اكتب سؤالك هنا...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = "معلومة رائعة! هل تريد معرفة المزيد؟ 😊"
        q_low = query.lower()
        
        if any(w in q_low for w in ["تعريف", "ماهي"]): ans = kb["تعريف"]
        elif "فرق" in q_low or "مقارنة" in q_low: ans = kb["mقارنة"]
        elif "طب" in q_low: ans = kb["طب"]
        elif "تعليم" in q_low: ans = kb["تعليم"]
        elif "مجالات" in q_low: ans = kb["مجالات"]
        elif "تغير" in q_low or "حياتنا" in q_low: ans = kb["تغيير_الحياة"]
        elif "استفادة" in q_low or "فوائد" in q_low: ans = kb["استفادة"]
        elif "نتعلم" in q_low or "هدف" in q_low: ans = kb["هدف_اللعبة"]
        
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {ans}</div>', unsafe_allow_html=True)
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
