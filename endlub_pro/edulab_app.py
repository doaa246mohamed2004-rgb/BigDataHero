import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم نيون احترافي (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #ffffff !important; font-family: 'Arial'; font-size: 18px; line-height: 1.6; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 42px !important; text-align: center; }
    .bot-text {
        color: #00f2ff; font-weight: bold; padding: 20px; border-right: 6px solid #00f2ff;
        background-color: #091a2a; border-radius: 15px; margin-bottom: 15px;
        direction: rtl; text-align: right; box-shadow: 0 0 15px #00f2ff;
    }
    .user-text {
        color: #ffffff; font-weight: bold; padding: 15px; direction: rtl;
        text-align: right; border-bottom: 2px solid #30363d; margin-bottom: 15px;
    }
    .welcome-box {
        background: linear-gradient(90deg, #00f2ff, #0066ff); color: black !important;
        padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; margin-bottom: 20px;
    }
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; border: none; }
    .stButton>button:hover { background-color: #ffffff; box-shadow: 0 0 20px #00f2ff; }
    table { width: 100%; color: white; border-collapse: collapse; margin: 10px 0; }
    th, td { border: 1px solid #30363d; padding: 12px; text-align: center; }
    th { background-color: #00f2ff; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة
kb = {
    "تعريف": "🔍 **ما هي البيانات الضخمة؟**\n\nهي مجموعات بيانات كبيرة جداً ومعقدة، بتتولد بسرعة هائلة من مصادر زي السوشيال ميديا والحساسات. الأدوات التقليدية مش بتقدر تعالجها بسهولة بسبب حجمها وسرعتها.",
    "خصائص": "⚡ **خصائص الـ 5V's الأساسية:**\n\n* **الحجم (Volume):** كميات هائلة بالبيتابايت.\n* **السرعة (Velocity):** تدفق فوري للبيانات.\n* **التنوع (Variety):** نصوص، صور، وفيديو.\n* **الموثوقية (Veracity):** مدى دقة وجودة البيانات.\n* **القيمة (Value):** الفائدة اللي بنطلع بيها بعد التحليل.",
    "فرق": """⚖️ **مقارنة بين البيانات العادية والضخمة:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | صغيرة (جيجابايت) | ضخمة جداً (بيتابايت فأكثر) |
| **التخزين** | خادم واحد مركزي | موزعة على عدة خوادم |
| **النوع** | مهيكلة (جداول) | غير مهيكلة (فيديو، صوت) |
| **الأدوات** | Excel / SQL | Hadoop / Spark |""",
    "أهمية": "🌟 **أهمية البيانات الضخمة:**\n\n* **اتخاذ قرارات ذكية:** بناءً على حقائق مش مجرد توقعات.\n* **التنبؤ بالمستقبل:** زي توقع الأزمات أو تغيرات الطقس.\n* **تحسين الكفاءة:** تقليل التكاليف والوقت في الشغل.",
    "حياة": "🌍 **في حياتنا اليومية:**\n\n* **الصحة:** توقع الأوبئة وتشخيص الأمراض.\n* **التجارة:** ترشيحات المنتجات في (أمازون ونون).\n* **المدن الذكية:** تنظيم المرور وتوفير الطاقة.\n* **الترفيه:** اقتراحات الأفلام في (يوتيوب ونتفليكس).",
    "تعليم": "🎓 **البيانات الضخمة في التعليم:**\n\n* **التعلم الشخصي:** محتوى يناسب قدرات كل طالب.\n* **تحسين النتائج:** مساعدة الطلاب المعرضين لخطر الرسوب مبكراً.\n* **تطوير المناهج:** اكتشاف الأجزاء الصعبة وتعديلها.",
    "وظائف": "💼 **الوظائف المتاحة:**\n\n* محلل بيانات (Data Analyst).\n* عالم بيانات (Data Scientist).\n* مهندس بيانات ضخمة (Big Data Engineer).\n* إخصائي ذكاء أعمال (BI Developer).",
    "تعلم": "🚀 **منصات التعلم:**\n\n* **Coursera & EdX:** كورسات من Google و IBM.\n* **Kaggle:** للتطبيق العملي والمنافسة.\n* **Datacamp:** لتعلم Python و SQL.",
    "roadmap": "🗺️ **خارطة طريق تعلم البيانات الضخمة:**\n\n1.  **تعلم Python:** هي الأساس في التعامل مع البيانات.\n2.  **تعلم SQL:** عشان تعرف تتعامل مع قواعد البيانات.\n3.  **تحليل البيانات:** اتعلم مكتبات Pandas و NumPy.\n4.  **أدوات الـ Big Data:** ابدأ في Hadoop و Spark.\n5.  **الذكاء الاصطناعي:** لعمل نماذج تنبؤية ذكية."
}

# نظام الأسئلة (Interactive Quiz)
quiz_data = [
    {"q": "أي من الـ 5V's تعبر عن دقة وجودة البيانات؟", "a": ["Veracity", "Volume", "Variety"], "correct": "Veracity"},
    {"q": "أداة متطورة تستخدم لمعالجة البيانات الضخمة:", "a": ["Hadoop", "Excel", "Notepad"], "correct": "Hadoop"},
    {"q": "البيانات الضخمة تُخزن بطريقة:", "a": ["موزعة (Distributed)", "مركزية (Centralized)", "ورقية"], "correct": "موزعة (Distributed)"}
]

# خريطة البحث
search_map = {
    "تعريف": ["تعريف", "يعني ايه", "ماهي", "البيانات الضخمة"],
    "خصائص": ["خصائص", "مميزات", "5v", "صفات"],
    "فرق": ["فرق", "مقارنة", "تفرق", "عادية"],
    "أهمية": ["أهمية", "اهميه", "فائدة"],
    "حياة": ["حياة", "يومية", "صحة", "تجارة", "مرور"],
    "تعليم": ["تعليم", "مدرسة", "جامعة", "طالب"],
    "وظائف": ["شغل", "وظيفة", "وظائف", "أشتغل"],
    "تعلم": ["كورس", "موقع", "منصات", "أتعلم"],
    "roadmap": ["كيف ابدأ", "خطة", "خارطة طريق", "طريق"]
}

# 4. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

# رسالة الترحيب "هل تعلم"
if "welcome" not in st.session_state:
    st.markdown("""<div class="welcome-box">
    👋 مرحبا! أنا وكيلك الذكي في عالم البيانات الضخمة.<br>
    💡 هل تعلم أن 90% من بيانات العالم تم إنتاجها في آخر سنتين فقط؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي (Sidebar)
st.sidebar.title("🎮 لوحة التحكم")
st.sidebar.link_button("🔙 العودة إلى اللعبة", "https://view.genially.com/69c2cab192730eedd4af164e")

st.sidebar.subheader("📌 اختصارات سريعة")
if st.sidebar.button("💡 ما هي البيانات الضخمة؟"): st.session_state.q = "تعريف"
if st.sidebar.button("⚖️ الفرق بين الأنواع"): st.session_state.q = "فرق"
if st.sidebar.button("🎓 البيانات في التعليم"): st.session_state.q = "تعليم"
if st.sidebar.button("🗺️ كيف أبدأ التعلم؟"): st.session_state.q = "roadmap"
if st.sidebar.button("📊 رسم بياني للنمو"): st.session_state.q = "رسم"
if st.sidebar.button("📝 اختبار سريع"): st.session_state.q = "quiz"

# 5. عرض المحادثة
if "messages" not in st.session_state: st.session_state.messages = []

for m in st.session_state.messages:
    role = "user-text" if m["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{role}">{m["content"]}</div>', unsafe_allow_html=True)
    if "chart" in m: st.bar_chart(m["chart"])

# 6. استقبال السؤال
input_q = st.chat_input("اسألني أي سؤال عن البيانات الضخمة... 🤖")
query = input_q or st.session_state.get("q")
if "q" in st.session_state: del st.session_state["q"]

if query:
    if query != "quiz":
        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": query})

    res = None
    msg = {"role": "assistant"}

    # منطق الردود
    if query == "quiz":
        q_item = random.choice(quiz_data)
        st.markdown(f'<div class="bot-text">📝 **اختبار سريع:** {q_item["q"]}</div>', unsafe_allow_html=True)
        ans = st.radio("اختر الإجابة:", q_item["a"], key="quiz")
        if st.button("تأكيد"):
            if ans == q_item["correct"]:
                st.success("🎯 بطل! إجابة صحيحة. حصلت على Badge محترف البيانات!")
                st.balloons()
            else: st.error(f"❌ خطأ بسيط، الإجابة هي: {q_item['correct']}")
    
    elif any(word in query.lower() for word in ["رسم", "شكل", "مخطط"]):
        res = "📊 إليك مخطط يوضح الانفجار الهائل في حجم البيانات (بالزيتابايت):"
        df = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        msg["chart"] = df
    else:
        # البحث الذكي
        for cat, keywords in search_map.items():
            if any(word in query.lower() for word in keywords):
                res = kb[cat]; break
    
    if query != "quiz":
        if not res: res = "عذراً يا بطل، حاول تسأل بشكل أوضح أو استخدم الأزرار في الجنب!"
        msg["content"] = res
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        if "chart" in msg: st.bar_chart(msg["chart"])
        st.session_state.messages.append(msg)
