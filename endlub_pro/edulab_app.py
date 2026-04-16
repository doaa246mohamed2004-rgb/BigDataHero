import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم احترافي صغير ومتناسق (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 30px !important; text-align: center; }
    
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .sidebar-title { color: #00f2ff !important; text-align: center; font-size: 20px; font-weight: bold; margin-bottom: 20px; }
    
    .bot-text {
        background-color: #0d1a26; color: #00f2ff; border-right: 4px solid #00f2ff;
        padding: 12px; border-radius: 12px; margin-bottom: 10px; line-height: 1.5;
    }
    .user-text {
        background-color: #161b22; color: #ffffff; border-left: 4px solid #58a6ff;
        padding: 10px; border-radius: 10px; margin-bottom: 10px;
    }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #1f6feb; color: white; font-size: 13px; }
    .stButton>button:hover { background-color: #00f2ff !important; color: black !important; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (المحتوى اللي هيطلع لما تسألي)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة بتيجي من مصادر كتير، والبرامج العادية مش بتقدر تعالجها. 🔍",
    "خصائص": "**خصائص الـ 5Vs:** \n1. الحجم (Volume) \n2. السرعة (Velocity) \n3. التنوع (Variety) \n4. الموثوقية (Veracity) \n5. القيمة (Value). ⚡",
    "أهمية": "أهميتها كبيرة جداً؛ بتساعدنا نتوقع الأمراض، ونفهم سلوك المستهلكين، ونطور المدن الذكية، ونمنع جرائم الإنترنت. 💎",
    "مجالات": "موجودة في كل حتة: الطب، البنوك، التجارة الإلكترونية، المواصلات، والتعليم الذكي. 🌍",
    "استخدامات": "بنستخدمها في: تحليل بيانات السوشيال ميديا، تحسين محركات البحث، وتطوير أنظمة الذكاء الاصطناعي. 🛠️",
    "roadmap": "ابدأ بـ Python، ثم قواعد البيانات SQL، ثم الإحصاء، وبعدها Hadoop و Spark. 🗺️",
    "مقارنة": "البيانات العادية حجمها صغير في جهاز واحد، أما الضخمة فهي هائلة وموزعة على شبكة أجهزة. ⚖️"
}

# 4. إدارة الحالة
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

# 5. الواجهة
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="sidebar-title">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك"): st.session_state.view = "quiz"
    if st.button("💬 ندردش"): st.session_state.view = "chat"
    st.markdown("---")
    st.subheader("🚀 وصول سريع")
    if st.button("🔍 التعريف"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ الخصائص"): st.session_state.q_auto = "خصائص"
    if st.button("💎 الأهمية"): st.session_state.q_auto = "أهمية"
    if st.button("🌍 المجالات"): st.session_state.q_auto = "مجالات"
    if st.button("🛠️ الاستخدامات"): st.session_state.q_auto = "استخدامات"
    if st.button("📊 الرسم البياني"): st.session_state.q_auto = "رسم بياني"

# 6. منطق الرد الذكي
if st.session_state.view == "chat":
    # عرض الرسايل القديمة
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    # استقبال السؤال
    u_input = st.chat_input("اسألني عن الخصائص، الأهمية، أو المجالات...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        q_low = query.lower()
        ans = "كلامك جميل! حابب تعرف إيه تاني بخصوص البيانات الضخمة؟ 😊"
        chart = None
        
        # المنطق اللي بيفتش في سؤالك
        if any(w in q_low for w in ["تعريف", "ماهي", "يعني ايه"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "5v"]): ans = kb["خصائص"]
        elif any(w in q_low for w in ["أهمية", "اهميه", "لازمتها"]): ans = kb["أهمية"]
        elif any(w in q_low for w in ["مجالات", "فين"]): ans = kb["مجالات"]
        elif any(w in q_low for w in ["استخدامات", "نستخدمها"]): ans = kb["استخدامات"]
        elif any(w in q_low for w in ["مقارنة", "فرق"]): ans = kb["مقارنة"]
        elif any(w in q_low for w in ["roadmap", "طريق"]): ans = kb["roadmap"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            ans = "ده رسم بياني بيوضح انفجار حجم البيانات عالمياً (بالزيتابايت) لعام 2025: 📊"
            chart = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم (ZB)': [2, 15, 64, 180]}).set_index('السنة')

        # عرض الرد فوراً
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {ans}</div>', unsafe_allow_html=True)
        if chart is not None: st.line_chart(chart)
        
        # حفظ في الذاكرة
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart is not None: msg["chart"] = chart
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun() # عشان يظهر الرد فوراً
