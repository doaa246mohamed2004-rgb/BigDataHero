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

# 3. قاعدة البيانات المطورة (أسئلة المناقشة والاحتمالات)
kb = {
    "تعريف": "البيانات الضخمة هي عبارة عن كميات هائلة من المعلومات بتيجي بسرعة رهيبة ومن مصادر متنوعة، والكمبيوترات العادية مش بتقدر تعالجها، فبنحتاج تكنولوجيا خاصة عشان نفهمها ونطلع منها فوائد. 🔍",
    "خصائص": "بتتميز بـ 5 حاجات أساسية (5Vs): \n1. **الحجم (Volume):** كميات داتا ضخمة.\n2. **السرعة (Velocity):** الداتا بتتحرك بسرعة اللحظة.\n3. **التنوع (Variety):** صور، فيديوهات، ونصوص.\n4. **الموثوقية (Veracity):** التأكد إن الداتا صحيحة.\n5. **القيمة (Value):** تحويل الداتا لقرار مفيد. ⚡",
    "مجالات_كاملة": """البيانات الضخمة موجودة في كل مكان:
- **في الطب:** تشخيص الأمراض مبكراً وتطوير الأدوية. 🏥
- **في التعليم:** التعلم الشخصي وتحليل مستوى الطلاب. 🎓
- **في المرور:** تحليل الزحام عبر GPS وتوفير الوقت. 🚗
- **في التجارة:** توقع احتياجات الزبائن وتحسين المبيعات. 🛒""",
    "استفادة": "لما تتعلم بيج داتا، هتقدر تشتغل في وظائف المستقبل بمرتبات مرتفعة، وتنمي مهارات حل المشكلات واتخاذ قرارات مبنية على الحقائق. 🌟",
    "مقارنة": "الفرق الجوهري: البيانات العادية حجمها صغير وتتخزن في ملف Excel، لكن البيانات الضخمة هائلة وموزعة عبر آلاف الأجهزة ولا يمكن فتحها بالبرامج التقليدية. ⚖️",
    "تغيير_الحياة": "بتغير حياتنا لأنها بتخلي الخدمات أسرع وأذكى، المدن بتبقى 'مدن ذكية' بتوفر كهرباء ومية، والرعاية الصحية بتبقى أدق. 🚀",
    "وظائف": "تقدر تشتغل: عالم بيانات (Data Scientist)، مهندس بيانات (Data Engineer)، أو محلل بيانات (Data Analyst). 💼",
    "برامج": "أهم الأدوات: Hadoop و Apache Spark لمعالجة الداتا، وقواعد بيانات NoSQL، ولغات Python و R. 💻",
    "أمن_خصوصية": "سؤال مهم! أمن البيانات الضخمة بيعتمد على التشفير (Encryption) وقوانين حماية الخصوصية زي (GDPR) عشان نضمن إن بيانات الناس مش بتتسرب أو تُستخدم غلط. 🛡️",
    "تخزين": "البيانات الضخمة مش بتتخزن في هارد ديسك واحد، بنستخدم حاجة اسمها 'التخزين الموزع' (Distributed Storage) زي نظام (HDFS)، وده بيسمح بتخزين الداتا على أجهزة كتير في نفس الوقت. 📦",
    "ذكاء_اصطناعي": "العلاقة قوية جداً! البيانات الضخمة هي 'الغذاء' للذكاء الاصطناعي؛ كل ما زادت البيانات، زادت قدرة الـ AI على التعلم واتخاذ قرارات أدق. 🤖",
    "تحديات": "أكبر التحديات هي: نقص الخبرات البشرية، تكلفة التخزين العالية، وضمان جودة الداتا (تكون نضيفة ومن غير أخطاء). ⚠️",
    "هدف": "هدفنا في 'Big Data Hero' إننا نحولك لـ 'بطل' فاهم إزاي البيانات بتدير العالم وبتحل مشاكله! 🎮"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"
if "not_found" not in st.session_state:
    st.session_state.not_found = False

quiz_data = [
    {"q": "أي نظام يستخدم لتخزين البيانات الضخمة بشكل موزع؟", "a": ["HDFS", "Flash Memory"], "correct": "HDFS"},
    {"q": "ما هو 'غذاء' الذكاء الاصطناعي الأساسي؟", "a": ["البيانات الضخمة", "البطاريات"], "correct": "البيانات الضخمة"}
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
    if st.button("⚡ الخصائص والأهمية"): st.session_state.q_auto = "خصائص"
    if st.button("🌍 المجالات الشاملة"): st.session_state.q_auto = "مجالات"
    if st.button("🛡️ الأمن والخصوصية"): st.session_state.q_auto = "أمن"
    if st.button("🤖 والذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"
    if st.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم"

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
        st.markdown('<div class="bot-text">مرحباً بك! أنا وكيلك الذكي لمشروع "Big Data Hero". جاهز للرد على أسئلة المناقشة وكل ما يخص عالم البيانات! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    u_input = st.chat_input("اسأل أي سؤال تقني أو عام عن البيانات الضخمة...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = None
        chart_data = None
        q_low = query.lower()
        
        # محرك البحث الذكي (Keyword Matching)
        if any(w in q_low for w in ["تعريف", "ماهي", "معنى"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "عادية"]): ans = kb["مقارنة"]
        elif any(w in q_low for w in ["خصائص", "5vs", "v"]): ans = kb["خصائص"]
        elif any(w in q_low for w in ["مجالات", "طب", "تعليم", "مرور", "استخدامات"]): ans = kb["مجالات_كاملة"]
        elif any(w in q_low for w in ["تغير", "حياتنا", "المستقبل"]): ans = kb["تغيير_الحياة"]
        elif "وظائف" in q_low or "أشتغل" in q_low: ans = kb["وظائف"]
        elif "برامج" in q_low or "أدوات" in q_low or "تقنيات" in q_low: ans = kb["برامج"]
        elif any(w in q_low for w in ["أمن", "خصوصية", "تشفير", "حماية"]): ans = kb["أمن_خصوصية"]
        elif any(w in q_low for w in ["تخزين", "hdfs", "هارد"]): ans = kb["تخزين"]
        elif any(w in q_low for w in ["ذكاء", "ai", "صناعي"]): ans = kb["ذكاء_اصطناعي"]
        elif any(w in q_low for w in ["تحديات", "صعوبات", "مشاكل"]): ans = kb["تحديات"]
        elif any(w in q_low for w in ["استفادة", "أهمية", "فوائد"]): ans = kb["استفادة"]
        elif any(w in q_low for w in ["رسم", "بياني", "نمو"]):
            ans = "إليكِ رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت): 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم': [2, 15, 64, 180]}).set_index('السنة')

        if ans is None:
            st.session_state.not_found = True
            ans = "هذه النقطة متقدمة جداً! حالياً يمكنني إفادتك في المواضيع التالية التي غالباً ما تُسأل في المناقشات:"
        else:
            st.session_state.not_found = False

        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart_data is not None: msg["chart"] = chart_data
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()

    if st.session_state.get("not_found"):
        cols = st.columns(3)
        with cols[0]:
            if st.button("🛡️ الأمن والخصوصية"): st.session_state.q_auto = "أمن"; st.rerun()
        with cols[1]:
            if st.button("🤖 الذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"; st.rerun()
        with cols[2]:
            if st.button("📦 طرق التخزين"): st.session_state.q_auto = "تخزين"; st.rerun()
