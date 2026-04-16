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
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; font-size: 42px !important; text-align: center; }
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
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; height: 3em; border: none; }
    .stButton>button:hover { background-color: #ffffff !important; box-shadow: 0 0 20px #00f2ff; }
    table { width: 100%; color: white; border-collapse: collapse; margin: 10px 0; direction: rtl; }
    th, td { border: 1px solid #30363d; padding: 12px; text-align: center; }
    th { background-color: #00f2ff; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (كل المحتوى العلمي)
kb = {
    "تعريف": "🔍 **ما هي البيانات الضخمة؟**\n\nهي مجموعات بيانات كبيرة ومعقدة، تتولد بسرعة هائلة من مصادر مختلفة. الأدوات التقليدية لا تستطيع التعامل معها بسهولة.",
    "خصائص": "⚡ **خصائص الـ 5V's:**\n1. **الحجم (Volume)**\n2. **السرعة (Velocity)**\n3. **التنوع (Variety)**\n4. **الموثوقية (Veracity)**\n5. **القيمة (Value)**",
    "فرق": """⚖️ **الفرق بين البيانات العادية والضخمة:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | جيجابايت | بيتابايت فأكثر |
| **التخزين** | خادم واحد | خوادم موزعة |
| **النوع** | مهيكلة (جداول) | غير مهيكلة (صور/فيديو) |""",
    "استخدامات": "🌍 **استخدامات البيانات الضخمة في حياتنا:**\n- **الصحة:** تشخيص الأمراض وتوقع الأوبئة.\n- **التجارة:** ترشيح المنتجات (مثل أمازون).\n- **المدن الذكية:** تنظيم المرور وتوفير الطاقة.\n- **الترفيه:** اقتراحات يوتيوب ونتفليكس.",
    "تعليم": "🎓 **البيانات الضخمة في التعليم:**\n- **تعلم شخصي:** محتوى يناسب كل طالب.\n- **تحسين النتائج:** مساعدة الطلاب المعرضين للرسوب.\n- **تطوير المناهج:** اكتشاف الأجزاء الصعبة وتعديلها.",
    "وظائف": "💼 **الوظائف المتاحة:**\n- محلل بيانات (Data Analyst).\n- عالم بيانات (Data Scientist).\n- مهندس بيانات ضخمة (Big Data Engineer).",
    "منصات": "🚀 **مواقع للتعلم:**\n- Coursera, Udacity, EdX, Kaggle, Datacamp.",
    "roadmap": "🗺️ **خارطة طريق التعلم:**\n1. Python\n2. SQL\n3. Pandas & NumPy\n4. Hadoop & Spark\n5. AI Models"
}

# 4. نظام الأسئلة المطور (في صميم المحتوى)
quiz_data = [
    {"q": "أي خاصية تعبر عن 'تنوع' أشكال البيانات (صور، نصوص، فيديو)؟", "a": ["Variety", "Volume", "Value"], "correct": "Variety"},
    {"q": "تُخزن البيانات الضخمة في خوادم:", "a": ["مركزية (واحد)", "موزعة (Distributed)", "فلاش ميموري"], "correct": "موزعة (Distributed)"},
    {"q": "من استخدامات البيانات الضخمة في التجارة الإلكترونية:", "a": ["ترشيح المنتجات", "كتابة المقالات", "تعديل الصور"], "correct": "ترشيح المنتجات"}
]

# 5. إدارة الحالة (Session State)
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)

# 6. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown("""<div class="welcome-box">👋 مرحبا! أنا وكيلك الذكي في عالم البيانات الضخمة.<br>💡 هل تعلم أن 90% من بيانات العالم تم إنتاجها في آخر سنتين فقط؟</div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي (Sidebar)
st.sidebar.title("🎮 التحكم")
if st.sidebar.button("📝 اختبر معلوماتك"):
    st.session_state.active_q = random.choice(quiz_data)
    st.session_state.quiz_feedback = None
    st.session_state.view = "quiz"

if st.sidebar.button("🏠 العودة للمحادثة"): st.session_state.view = "chat"

st.sidebar.subheader("📌 اختصارات سريعة")
if st.sidebar.button("💡 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
if st.sidebar.button("🌍 الاستخدامات"): st.session_state.q_auto = "استخدامات"
if st.sidebar.button("🗺️ خارطة الطريق"): st.session_state.q_auto = "roadmap"

# 7. منطق العرض (اختبار أم محادثة)
if st.session_state.get("view") == "quiz":
    # عرض قسم الاختبار
    q_item = st.session_state.active_q
    st.markdown(f'<div class="bot-text">📝 سؤال: {q_item["q"]}</div>', unsafe_allow_html=True)
    
    with st.container():
        user_choice = st.radio("اختر الإجابة الصحيحة:", q_item["a"], key="r_quiz")
        if st.button("إرسال الإجابة"):
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "✅ إجابة صحيحة! بطل البيانات.")
            else:
                st.session_state.quiz_feedback = ("error", f"❌ خطأ! الإجابة الصح هي: {q_item['correct']}")
    
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)
else:
    # عرض المحادثة
    for m in st.session_state.messages:
        role = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role}">{m["content"]}</div>', unsafe_allow_html=True)

    user_input = st.chat_input("اسألني عن الاستخدامات، التعريف، أو الوظائف...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        # منطق البحث الذكي (Keyword Matching)
        q_low = query.lower()
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "تفرق"]): res = kb["فرق"]
        elif any(w in q_low for w in ["استخدامات", "فين", "حياة", "نعمل بيها ايه"]): res = kb["استخدامات"]
        elif any(w in q_low for w in ["تعليم", "طالب", "مدرسة"]): res = kb["تعليم"]
        elif any(w in q_low for w in ["وظيفة", "شغل", "أشتغل"]): res = kb["وظائف"]
        elif any(w in q_low for w in ["تعلم", "كورس", "موقع"]): res = kb["منصات"]
        elif any(w in q_low for w in ["roadmap", "خطة", "أبدأ"]): res = kb["roadmap"]
        
        if not res: res = "معلومة شيقة! اسألني أكتر عن استخدامات البيانات أو خصائصها."
        
        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": res})
