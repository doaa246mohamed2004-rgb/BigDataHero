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

# 3. قاعدة البيانات الشاملة (Knowledge Base)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة تفوق قدرة البرامج التقليدية على المعالجة، وتتميز بسرعة تدفقها وتنوعها. 🔍",
    "خصائص": "تتميز بـ 5Vs: الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)، الموثوقية (Veracity)، والقيمة (Value). ⚡",
    "استفادة_تعلم": "هتستفاد إيه؟ \n1. وظائف بمرتبات عالية (أعلى الرواتب تقنياً).\n2. القدرة على توقع المستقبل وبناء أنظمة ذكية.\n3. حل مشاكل معقدة في الطب والصناعة والبيئة. 🌟",
    "أدوات_تعلم": "أهم الأدوات هي: لغة Python، نظام Hadoop للتخزين الموزع، Apache Spark للمعالجة السريعة، وقواعد بيانات NoSQL. 💻",
    "خطوات_تعلم": "ابدأ بـ: \n1. تعلم لغة Python.\n2. افهم أساسيات الإحصاء.\n3. ادرس تقنيات تخزين الداتا (SQL & NoSQL).\n4. تعلم أدوات المعالجة الضخمة (Spark). 🚀",
    "ترتيب_تجميع": "دورة حياة البيانات: \n1. **التجميع (Collection):** من المصادر المختلفة.\n2. **التخزين (Storage):** في أنظمة موزعة.\n3. **المعالجة (Processing):** تنظيف وترتيب الداتا.\n4. **التحليل (Analysis):** استخراج الأنماط.\n5. **التصور (Visualization):** عرضها في رسوم بيانية. 📊",
    "تغيير_الحياة": "بتغير حياتنا عن طريق: تشخيص الأمراض مبكراً، تقليل زحام المرور بالخرائط الذكية، توفير استهلاك الطاقة، وحتى تحسين تجربة التسوق والترفيه. 🌍",
    "استفادة_اللعبة": "بعد ما تلعب 'بطل البيانات الضخمة'، هتكون فهمت إزاي تحول الأرقام لمعلومات مفيدة، وقدرت تواجه تحديات حقيقية بيواجهها مهندسين البيانات في العالم الواقعي! 🎮",
    "أمن_خصوصية": "تعتمد على التشفير القوي وقوانين صارمة (مثل GDPR) لحماية بيانات المستخدمين من الاختراق أو الاستخدام غير القانوني. 🛡️",
    "ذكاء_اصطناعي": "البيانات الضخمة هي المحرك الأساسي للذكاء الاصطناعي؛ فبدون بيانات ضخمة، لا يمكن للـ AI أن يتعلم أو يتطور. 🤖",
    "مجالات": "تستخدم في الطب، التعليم، الفضاء، البنوك، والمدن الذكية لتسهيل حياة البشر. 🏥🎓🚗"
}

# 4. إدارة الجلسة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "view" not in st.session_state:
    st.session_state.view = "chat"
if "not_found" not in st.session_state:
    st.session_state.not_found = False

quiz_data = [
    {"q": "أي مرحلة تأتي أولاً في التعامل مع البيانات؟", "a": ["التجميع", "التحليل"], "correct": "التجميع"},
    {"q": "هل لغة Python مهمة لتعلم البيانات الضخمة؟", "a": ["نعم", "لا"], "correct": "نعم"}
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
    if st.button("🔍 التعريف والخصائص"): st.session_state.q_auto = "تعريف"
    if st.button("📈 خطوات وأدوات التعلم"): st.session_state.q_auto = "تعلم"
    if st.button("📊 دورة حياة البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("🌍 تأثيرها على حياتنا"): st.session_state.q_auto = "تغيير"
    if st.button("🛡️ الأمن والذكاء"): st.session_state.q_auto = "أمن"
    if st.button("🎮 فائدة اللعبة"): st.session_state.q_auto = "لعبة"

# 6. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz"):
        choice = st.radio("الإجابة:", q_item["a"])
        if st.form_submit_button("إرسال"):
            if choice == q_item["correct"]: st.success("بطل! إجابة صحيحة 🎯")
            else: st.error("فكر مرة ثانية!")
else:
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">أهلاً بك يا بطل! أنا وكيلك الذكي. اسألني عن أي شيء يخص البيانات الضخمة أو كيف تصبح خبيراً فيها! 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اسألني عن خطوات التعلم، الأدوات، أو الاستفادة...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        ans = None
        q_low = query.lower()
        
        # منطق الرد المرن (Flexible Matching)
        if any(w in q_low for w in ["تعريف", "ماهي", "معنى"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "5vs"]): ans = kb["خصائص"]
        elif any(w in q_low for w in ["أستفاد", "استفاد", "فوائد", "اهمية", "أهمية"]) and "تعلم" in q_low: ans = kb["استفادة_تعلم"]
        elif any(w in q_low for w in ["أدوات", "ادوات", "برامج", "تكنولوجيا"]): ans = kb["أدوات_تعلم"]
        elif any(w in q_low for w in ["خطوات", "كيف أبدأ", "طريق"]): ans = kb["خطوات_تعلم"]
        elif any(w in q_low for w in ["ترتيب", "تجميع", "مراحل", "دورة حياة"]): ans = kb["ترتيب_تجميع"]
        elif any(w in q_low for w in ["تغير", "حياتنا", "تأثير"]): ans = kb["تغيير_الحياة"]
        elif any(w in q_low for w in ["هستفاد", "اللعبة", "لعبة", "بطل"]): ans = kb["استفادة_اللعبة"]
        elif any(w in q_low for w in ["أمن", "خصوصية", "تشفير"]): ans = kb["أمن_خصوصية"]
        elif any(w in q_low for w in ["ذكاء", "ai"]): ans = kb["ذكاء_اصطناعي"]
        elif any(w in q_low for w in ["مجالات", "طب", "تعليم", "مرور"]): ans = kb["مجالات"]

        if ans is None:
            st.session_state.not_found = True
            ans = "عذراً، هذه المعلومة غير متوفرة حالياً. يمكنك سؤالي عن أحد المواضيع الشاملة التالية:"
        else:
            st.session_state.not_found = False

        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()

    # الأيقونات التفاعلية عند عدم العثور على إجابة
    if st.session_state.get("not_found"):
        cols = st.columns(3)
        with cols[0]:
            if st.button("📈 خطوات التعلم"): st.session_state.q_auto = "خطوات"; st.rerun()
        with cols[1]:
            if st.button("📊 مراحل التجميع"): st.session_state.q_auto = "ترتيب"; st.rerun()
        with cols[2]:
            if st.button("🎮 فائدة اللعبة"): st.session_state.q_auto = "لعبة"; st.rerun()
