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

# 3. قاعدة البيانات الموسعة
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة تفوق قدرة البرامج التقليدية على المعالجة. 🔍",
    "خصائص": "خصائص الـ 5Vs هي: الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)، الموثوقية (Veracity)، والقيمة (Value). ⚡",
    "مجالات": "تنتشر في: الطب، البنوك، التجارة الإلكترونية، المواصلات، الفضاء، والمدن الذكية. 🌍",
    "تعليم": "في التعليم: توفر 'التعلم الشخصي'، وتتوقع مستوى الطلاب المتعثرين، وتساعد في تطوير المناهج الرقمية. 🎓",
    "استفادة": "الاستفادة: توفر فرص عمل بمرتبات مرتفعة، وتنمي مهارة حل المشكلات واتخاذ القرارات الذكية بناءً على الحقائق. 🌟",
    "مقارنة": "الفرق: البيانات العادية محدودة الحجم وتخزن في جهاز واحد، بينما الضخمة هائلة وموزعة عبر آلاف الأجهزة. ⚖️",
    "طب": "في الطب: تستخدم في تشخيص الأمراض مبكراً، واكتشاف علاجات جديدة، ومراقبة صحة المرضى عن بُعد. 🏥",
    "تغيير_الحياة": "تغير حياتنا بجعل المدن أذكى، والخدمات أسرع، وتقديم حلول دقيقة لمشاكل الفقر، المناخ، والصحة العامة. 🚀",
    "وظائف": "الوظائف المتاحة: عالم بيانات (Data Scientist)، مهندس بيانات (Data Engineer)، ومحلل بيانات ضخمة (Big Data Analyst). 💼",
    "برامج": "أهم البرامج والأدوات: Hadoop، Apache Spark، NoSQL databases، لغة Python، ولغة R. 💻",
    "أهمية": "أهميتها تكمن في خفض التكاليف، توفير الوقت، اتخاذ قرارات دقيقة، وتطوير منتجات تناسب احتياجات الناس. 💎",
    "هدف": "في اللعبة دي، بنتعلم إزاي نحول الأرقام الضخمة لمعلومات مفيدة تحل مشاكل العالم الحقيقي! 🎮"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"
if "not_found" not in st.session_state:
    st.session_state.not_found = False

quiz_data = [
    {"q": "أي برنامج يستخدم للتعامل مع البيانات الضخمة؟", "a": ["Hadoop", "Excel"], "correct": "Hadoop"},
    {"q": "هل الحجم (Volume) هو أحد خصائص البيانات الضخمة؟", "a": ["نعم", "لا"], "correct": "نعم"}
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
    if st.button("💼 الوظائف والبرامج"): st.session_state.q_auto = "وظائف"
    if st.button("🏥 الطب والتعليم"): st.session_state.q_auto = "تعليم"
    if st.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    if st.button("🌍 كيف تغير حياتنا؟"): st.session_state.q_auto = "تغيير"

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
        st.markdown('<div class="bot-text">مرحباً بك يا بطلة! أنا وكيلك الذكي. اسأليني أي سؤال عن عالم البيانات الضخمة! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    # مدخلات المستخدم
    u_input = st.chat_input("اسألني أي سؤال هنا...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = None
        chart_data = None
        q_low = query.lower()
        
        # البحث الذكي في قاعدة البيانات
        if any(w in q_low for w in ["تعريف", "ماهي"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["فرق", "مقارنة"]): ans = kb["مقارنة"]
        elif "خصائص" in q_low: ans = kb["خصائص"]
        elif "أهمية" in q_low or "اهميه" in q_low: ans = kb["أهمية"]
        elif "وظائف" in q_low: ans = kb["وظائف"]
        elif "برامج" in q_low or "أدوات" in q_low: ans = kb["برامج"]
        elif "طب" in q_low: ans = kb["طب"]
        elif "تعليم" in q_low: ans = kb["تعليم"]
        elif "مجالات" in q_low: ans = kb["مجالات"]
        elif "تغير" in q_low or "حياتنا" in q_low: ans = kb["تغيير_الحياة"]
        elif any(w in q_low for w in ["نتعلم", "هدف"]): ans = kb["هدف"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            ans = "إليكِ رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت): 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم': [2, 15, 64, 180]}).set_index('السنة')

        # التعامل مع السؤال غير المتوفر
        if ans is None:
            st.session_state.not_found = True
            ans = "عذراً، هذه المعلومة غير متوفرة حالياً. يمكنك سؤالي عن أحد المواضيع التالية:"
        else:
            st.session_state.not_found = False

        # إضافة الرسالة للتاريخ
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart_data is not None: msg["chart"] = chart_data
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()

    # إظهار الأيقونات التفاعلية لو السؤال غير موجود
    if st.session_state.get("not_found"):
        cols = st.columns(3)
        with cols[0]:
            if st.button("🔍 التعريف"): st.session_state.q_auto = "تعريف"; st.rerun()
        with cols[1]:
            if st.button("🏥 الطب"): st.session_state.q_auto = "طب"; st.rerun()
        with cols[2]:
            if st.button("💻 البرامج"): st.session_state.q_auto = "برامج"; st.rerun()
        
        cols2 = st.columns(3)
        with cols2[0]:
            if st.button("💼 الوظائف"): st.session_state.q_auto = "وظائف"; st.rerun()
        with cols2[1]:
            if st.button("⚡ الخصائص"): st.session_state.q_auto = "خصائص"; st.rerun()
        with cols2[2]:
            if st.button("🌍 حياتنا"): st.session_state.q_auto = "تغيير"; st.rerun()
