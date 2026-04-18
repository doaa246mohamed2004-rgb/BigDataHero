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
    .stButton>button { width: 100%; border-radius: 8px; background-color: #1f6feb; color: white; height: 2.8em; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة
kb = {
    "تعريف": "الالبيانات الضخمة هي مجموعات بيانات هائلة ومعقدة بتيجي من مصادر كتير، والبرامج العادية مش بتقدر تعالجها. 🔍",
    "خصائص": "خصائص الـ 5Vs هي: الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)، الموثوقية (Veracity)، والقيمة (Value). ⚡",
    "وظائف": "من أهم الوظائف: عالم بيانات، مهندس بيانات، ومحلل بيانات. 💼",
    "تعليم": "في التعليم بتساعدنا نفهم مستوى كل طالب ونقدم له محتوى يناسب قدراته بالظبط. 🎓",
    "استفادة": "بتعلمك إزاي تاخد قرارات صح بناءً على الأرقام وتفتح لك مجالات شغل عالمية. 🌟",
    "أهمية": "أهميتها إنها بتخلينا نتوقع المستقبل، زي توقع الأمراض أو حالة الطقس وتحسين أمن البنوك. 💎",
    "هدف_اللعبة": "في اللعبة دي، بنتعلم إزاي نحول الأرقام الضخمة لمعلومات مفيدة، وبنفهم إزاي التكنولوجيا بتفكر عشان تحل مشاكل العالم الحقيقي باستخدام البيانات! 🎮🚀"
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
    if st.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ خصائص الـ 5Vs"): st.session_state.q_auto = "خصائص"
    if st.button("💎 أهمية البيانات"): st.session_state.q_auto = "أهمية"
    if st.button("📊 نمو البيانات"): st.session_state.q_auto = "رسم بياني"
    if st.button("🎮 ماذا نتعلم هنا؟"): st.session_state.q_auto = "هدف"

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
    # عرض الرسائل السابقة
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">مرحباً بك! أنا وكيلك الذكي. اسألني عن أي شيء يخص البيانات الضخمة! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    # مدخلات المستخدم
    u_input = st.chat_input("اكتب سؤالك هنا...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = "كلام جميل! حابب تعرف إيه تاني بخصوص البيانات الضخمة؟ 😊"
        chart = None
        q_low = query.lower()
        
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): ans = kb["تعريف"]
        elif "خصائص" in q_low: ans = kb["خصائص"]
        elif "أهمية" in q_low or "اهميه" in q_low: ans = kb["أهمية"]
        elif "وظائف" in q_low: ans = kb["وظائف"]
        elif "تعليم" in q_low: ans = kb["تعليم"]
        elif "نتعلم" in q_low or "هدف" in q_low: ans = kb["هدف_اللعبة"]
        elif "رسم" in q_low or "بياني" in q_low:
            ans = "إليك رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت): 📊"
            chart = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم': [2, 15, 64, 180]}).set_index('السنة')

        # عرض الرد الحالي
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {ans}</div>', unsafe_allow_html=True)
        if chart is not None: st.line_chart(chart)
        
        # حفظ في التاريخ
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart is not None: msg["chart"] = chart
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
