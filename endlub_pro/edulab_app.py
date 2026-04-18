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

# 3. قاعدة البيانات الشاملة (معلومات تفصيلية للطالب)
kb = {
    "تعريف": "البيانات الضخمة هي عبارة عن كميات هائلة من المعلومات بتيجي بسرعة رهيبة ومن مصادر متنوعة (زي السوشيال ميديا والحساسات)، والكمبيوترات العادية مش بتقدر تعالجها، فبنحتاج تكنولوجيا خاصة عشان نفهمها ونطلع منها فوائد. 🔍",
    "خصائص": "بتتميز بـ 5 حاجات أساسية (5Vs): \n1. **الحجم (Volume):** كميات داتا بالتيرا والزيتابايت.\n2. **السرعة (Velocity):** الداتا بتتحرك وبتتولد بسرعة اللحظة.\n3. **التنوع (Variety):** صور، فيديوهات، نصوص، وأرقام.\n4. **الموثوقية (Veracity):** التأكد إن الداتا صحيحة مش مزيفة.\n5. **القيمة (Value):** أهم حاجة إننا نحول الداتا دي لقرار مفيد. ⚡",
    "مجالات_كاملة": """البيانات الضخمة موجودة في كل مكان حولنا:
- **في الطب:** بتساعد الدكاترة يشخصوا الأمراض قبل ما تظهر أعراضها، وبتستخدم في تحليل الجينات وتطوير الأدوية بسرعة. 🏥
- **في التعليم:** بتعرف المدرسين نقاط ضعف كل طالب وتعمله خطة مذاكرة تناسبه هو لوحده (التعلم الشخصي). 🎓
- **في زحمة المرور:** برامج زي Google Maps بتحلل بيانات ملايين الموبايلات عشان تقولك الطريق الزحمة فين وتعرفك أسرع طريق توفر بيه وقتك وبنزينك. 🚗💨
- **في التجارة:** المواقع زي أمازون بتعرف إنت بتحب إيه وتقترح عليك منتجات تهمك فعلاً. 🛒""",
    "استفادة": "لما تتعلم بيج داتا، هتقدر تشتغل في وظائف المستقبل بمرتبات خيالية، وهتكون عندك قدرة إنك تحل مشاكل معقدة وتوقع اللي هيحصل في المستقبل بناءً على الأرقام مش التخمين. 🌟",
    "مقارنة": "الفرق الجوهري: البيانات العادية حجمها صغير وتتخزن في ملف Excel على جهاز واحد، لكن البيانات الضخمة هائلة وموزعة عبر آلاف الأجهزة (Servers) ولا يمكن فتحها بالبرامج التقليدية. ⚖️",
    "تغيير_الحياة": "بتغير حياتنا لأنها بتخلي الخدمات أسرع وأذكى؛ المدن بتبقى 'مدن ذكية' بتوفر كهرباء ومية، والرعاية الصحية بتبقى أدق، وحتى الترفيه والرياضة بقوا يعتمدوا عليها لتحسين أداء اللاعبين واختيار الخطط. 🚀",
    "وظائف": "تقدر تشتغل: \n1. **عالم بيانات (Data Scientist):** اللي بيطلع الأسرار من الداتا.\n2. **مهندس بيانات (Data Engineer):** اللي بيبني المواسير اللي بتمشي فيها الداتا.\n3. **محلل بيانات:** اللي بيشرح النتائج للمديرين. 💼",
    "برامج": "أهم الأدوات اللي لازم تعرفها: Hadoop و Apache Spark لمعالجة الداتا، وقواعد بيانات NoSQL، ولغات برمجة زي Python و R. 💻",
    "هدف": "هدفنا في 'Big Data Hero' إننا نحولك من مجرد مستخدم للتكنولوجيا لـ 'بطل' فاهم إزاي البيانات بتدير العالم وبتحل مشاكله! 🎮"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"
if "not_found" not in st.session_state:
    st.session_state.not_found = False

quiz_data = [
    {"q": "ما هي الأداة التي تستخدم لتحليل الزحام المروري باستخدام البيانات الضخمة؟", "a": ["خرائط جوجل", "برنامج الرسام"], "correct": "خرائط جوجل"},
    {"q": "هل البيانات الضخمة تساعد في تشخيص الأمراض مبكراً؟", "a": ["نعم", "لا"], "correct": "نعم"}
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
    if st.button("🌍 المجالات (طب، تعليم، مرور)"): st.session_state.q_auto = "مجالات"
    if st.button("💼 الوظائف والبرامج"): st.session_state.q_auto = "وظائف"
    if st.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    if st.button("🚀 كيف تغير حياتنا؟"): st.session_state.q_auto = "تغيير"

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
        st.markdown('<div class="bot-text">مرحباً بك يا بطلة! أنا وكيلك الذكي. اسأليني عن الطب، التعليم، أو حتى زحمة المرور والبيانات الضخمة! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    u_input = st.chat_input("اسألني أي سؤال هنا...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = None
        chart_data = None
        q_low = query.lower()
        
        # البحث المطور والربط بين الكلمات
        if any(w in q_low for w in ["تعريف", "ماهي"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "عادية"]): ans = kb["مقارنة"]
        elif "خصائص" in q_low: ans = kb["خصائص"]
        elif any(w in q_low for w in ["مجالات", "طب", "تعليم", "مرور", "زحمة", "استخدامات"]): ans = kb["مجالات_كاملة"]
        elif any(w in q_low for w in ["تغير", "حياتنا", "حياه"]): ans = kb["تغيير_الحياة"]
        elif "وظائف" in q_low: ans = kb["وظائف"]
        elif "برامج" in q_low or "أدوات" in q_low: ans = kb["برامج"]
        elif any(w in q_low for w in ["استفادة", "فوائد", "اهميه", "أهمية"]): ans = kb["استفادة"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            ans = "إليكِ رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت): 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم': [2, 15, 64, 180]}).set_index('السنة')

        if ans is None:
            st.session_state.not_found = True
            ans = "عذراً، هذه المعلومة غير متوفرة حالياً. يمكنك سؤالي عن أحد المواضيع الشاملة التالية:"
        else:
            st.session_state.not_found = False

        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart_data is not None: msg["chart"] = chart_data
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()

    # الأيقونات التفاعلية المحدثة
    if st.session_state.get("not_found"):
        cols = st.columns(3)
        with cols[0]:
            if st.button("🏥 المجالات والطب"): st.session_state.q_auto = "مجالات"; st.rerun()
        with cols[1]:
            if st.button("🔍 التعريف والفرق"): st.session_state.q_auto = "فرق"; st.rerun()
        with cols[2]:
            if st.button("💻 البرامج والأدوات"): st.session_state.q_auto = "برامج"; st.rerun()
