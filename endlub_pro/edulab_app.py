import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم UI احترافي متناسق
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 30px !important; text-align: center; margin-bottom: 15px; }
    
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .sidebar-title { color: #00f2ff !important; text-align: center; font-size: 20px; font-weight: bold; margin-bottom: 15px; }
    
    .bot-text {
        background-color: #0d1a26; color: #00f2ff; border-right: 4px solid #00f2ff;
        padding: 12px; border-radius: 12px; margin-bottom: 10px; line-height: 1.6;
        box-shadow: 0 0 8px rgba(0, 242, 255, 0.1);
    }
    .user-text {
        background-color: #161b22; color: #ffffff; border-left: 4px solid #58a6ff;
        padding: 10px; border-radius: 10px; margin-bottom: 10px;
    }
    .stButton>button { 
        width: 100%; border-radius: 8px; background-color: #1f6feb; color: white; 
        font-size: 13px; font-weight: bold; height: 2.8em;
    }
    .stButton>button:hover { background-color: #00f2ff !important; color: black !important; box-shadow: 0 0 12px #00f2ff; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة بتيجي من مصادر كتير، والبرامج العادية مش بتقدر تعالجها. 🔍",
    "خصائص": "**خصائص الـ 5Vs:** \n1. الحجم \n2. السرعة \n3. التنوع \n4. الموثوقية \n5. القيمة. ⚡",
    "أهمية": "بتساعدنا نكتشف الأنماط المخفية، ونطور العلاجات الطبية، ونأمن البنوك، ونبني مدن ذكية متطورة. 💎",
    "مجالات": "موجودة في: الطب، البنوك، التجارة الإلكترونية، المواصلات، الفضاء، والتعليم. 🌍",
    "استخدامات": "بنستخدمها في: تحليل بيانات السوشيال ميديا، توقع الطقس، تحسين محركات البحث، وأنظمة الترجمة الفورية. 🛠️",
    "وظائف": "عالم بيانات، مهندس بيانات، محلل بيانات، ومسؤول أمن معلومات. 💼",
    "استفادة": "تعلمها بيفتح لك أبواب شغل بمرتبات عالية، وبيطور عندك مهارة حل المشكلات واتخاذ القرارات الذكية. 🌟",
    "تعليم": "في التعليم بتساعدنا في 'التعلم الشخصي' وتوقع مستوى الطلاب وتطوير مناهج تناسب كل طالب. 🎓",
    "roadmap": "طريقك: ابدأ بـ لغة بايثون، ثم قواعد البيانات، ثم الإحصاء، ثم أدوات هادوب وسبارك. 🗺️",
    "مقارنة": "البيانات العادية: حجم صغير في جهاز واحد. البيانات الضخمة: حجم هائل وموزعة على آلاف الأجهزة. ⚖️"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

# أسئلة الاختبار (عربية وسهلة)
quiz_data = [
    {"q": "هل البيانات الضخمة يمكن تخزينها بسهولة على جهاز كمبيوتر شخصي واحد؟", "a": ["نعم", "لا"], "correct": "لا"},
    {"q": "أي من هؤلاء يعتبر من خصائص البيانات الضخمة؟", "a": ["الحجم والسرعة", "اللون والشكل", "الطول والوزن"], "correct": "الحجم والسرعة"},
    {"q": "ما هي اللغة البرمجية الأشهر في تحليل البيانات الضخمة؟", "a": ["بايثون", "سي بلس بلس", "سكراتش"], "correct": "بايثون"},
    {"q": "البيانات التي تأتي من الصور والفيديوهات تسمى بيانات:", "a": ["متنوعة", "بسيطة", "صغيرة"], "correct": "متنوعة"}
]

# 5. الواجهة الأساسية
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="sidebar-title">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.view = "quiz"
    
    if st.button("💬 ندردش سوا"):
        st.session_state.messages = [] 
        st.session_state.view = "chat"
    
    st.markdown("---")
    st.subheader("🚀 وصول سريع")
    cols = st.columns(2)
    with cols[0]:
        if st.button("🔍 التعريف"): st.session_state.q_auto = "تعريف"
        if st.button("⚡ الخصائص"): st.session_state.q_auto = "خصائص"
        if st.button("💼 الوظائف"): st.session_state.q_auto = "وظائف"
    with cols[1]:
        if st.button("🎓 التعليم"): st.session_state.q_auto = "تعليم"
        if st.button("📊 الرسم"): st.session_state.q_auto = "رسم بياني"
        if st.button("🌟 الفوائد"): st.session_state.q_auto = "استفادة"

# 6. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 **تحدي ذكاء:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("اختار الإجابة الصحيحة:", q_item["a"])
        if st.form_submit_button("إرسال الإجابة"):
            if user_choice == q_item["correct"]:
                st.success("صح يا بطل! إجابة ممتازة 🎯")
                st.balloons()
            else: st.error(f"للأسف خطأ.. الإجابة الصح هي: {q_item['correct']}")

else:
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">مرحباً بك! أنا وكيلك الذكي في تعلم البيانات الضخمة. الصفحة الآن ملكك، اسألني عن أي شيء يخص هذا العالم الممتع! 😊</div>', unsafe_allow_html=True)

    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    u_input = st.chat_input("اكتب سؤالك هنا باللغة العربية...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        q_low = query.lower()
        ans = "كلام جميل! حابب تعرف إيه تاني بخصوص البيانات الضخمة؟ 😊"
        chart = None
        
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات"]): ans = kb["خصائص"]
        elif any(w in q_low for w in ["أهمية", "اهميه"]): ans = kb["أهمية"]
        elif any(w in q_low for w in ["مجالات", "فين"]): ans = kb["مجالات"]
        elif any(w in q_low for w in ["استخدامات", "نستخدمها"]): ans = kb["استخدامات"]
        elif any(w in q_low for w in ["وظائف", "شغل"]): ans = kb["وظائف"]
        elif any(w in q_low for w in ["استفادة", "فايدة"]): ans = kb["استفادة"]
        elif any(w in q_low for w in ["تعليم", "مدرسة"]): ans = kb["تعليم"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            ans = "الرسم البياني لنمو البيانات عالمياً: 📊"
            chart = pd.DataFrame({'سنة': ['2010', '2015', '2020', '2025'], 'حجم': [2, 15, 64, 180]}).set_index('سنة')

        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {ans}</div>', unsafe_allow_html=True)
        if chart is not None: st.line_chart(chart)
        
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart is not None: msg["chart"] = chart
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
