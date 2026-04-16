import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم نيون احترافي (UI/UX) متطور
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
        box-shadow: 0 0 20px #00f2ff;
    }
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; height: 3em; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #ffffff !important; box-shadow: 0 0 20px #00f2ff; transform: scale(1.02); }
    table { width: 100%; color: white; border-collapse: collapse; margin: 10px 0; direction: rtl; }
    th, td { border: 1px solid #30363d; padding: 12px; text-align: center; }
    th { background-color: #00f2ff; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (المحتوى العلمي الكامل)
kb = {
    "تعريف": "🔍 **ما هي البيانات الضخمة؟**\n\nهي مجموعات بيانات كبيرة جداً ومعقدة، تتولد بسرعة هائلة من مصادر مختلفة مثل (وسائل التواصل الاجتماعي، الحساسات، والأجهزة الذكية). ضخمة لدرجة أن الأدوات التقليدية لا تستطيع التعامل معها بسهولة.",
    "خصائص": "⚡ **خصائص الـ 5V's الأساسية:**\n\n1. **الحجم (Volume):** كميات هائلة تقاس بالبيتابايت.\n2. **السرعة (Velocity):** تدفق البيانات في وقت قياسي.\n3. **التنوع (Variety):** أشكال مختلفة (نصوص، صور، فيديو).\n4. **الموثوقية (Veracity):** مدى دقة وجودة البيانات.\n5. **القيمة (Value):** الفائدة المستخرجة بعد التحليل.",
    "فرق": """⚖️ **الفرق بين البيانات العادية والضخمة:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | صغيرة (جيجابايت) | ضخمة جداً (بيتابايت) |
| **التخزين** | خادم واحد مركزي | موزعة Distributed |
| **النوع** | مهيكلة (جداول) | غير مهيكلة (صور/فيديو) |
| **الأدوات** | Excel / SQL | Hadoop / Spark |""",
    "استخدامات": "🌍 **استخدامات البيانات الضخمة في حياتنا اليومية:**\n\n- **الرعاية الصحية:** التنبؤ بالأوبئة وتشخيص الأمراض بدقة.\n- **التجارة الإلكترونية:** ترشيح المنتجات (أمازون ونون).\n- **المدن الذكية:** تنظيم المرور وتوفير الطاقة.\n- **الترفيه:** اقتراحات يوتيوب ونتفليكس.",
    "تعليم": "🎓 **البيانات الضخمة في التعليم:**\n\n- **التعلم الشخصي:** تقديم محتوى يناسب قدرات كل طالب.\n- **تحسين النتائج:** مساعدة الطلاب المعرضين لخطر الرسوب مبكراً.\n- **تطوير المناهج:** اكتشاف الأجزاء الصعبة وتعديلها.",
    "roadmap": "🗺️ **كيف أبدأ تعلم البيانات الضخمة؟ (الخريطة الذهنية):**\n\n1. **تعلم Python:** هي اللغة الأساسية للبيانات.\n2. **تعلم SQL:** للتعامل مع قواعد البيانات.\n3. **تحليل البيانات:** اتقان مكتبات مثل Pandas & NumPy.\n4. **أدوات Big Data:** تعلم Hadoop و Spark.\n5. **الذكاء الاصطناعي:** لبناء نماذج تنبؤية ذكية.",
    "وظائف": "💼 **الوظائف المتاحة:**\n- محلل بيانات (Data Analyst).\n- عالم بيانات (Data Scientist).\n- مهندس بيانات ضخمة (Big Data Engineer).\n- إخصائي ذكاء أعمال (BI Developer).",
    "منصات": "🚀 **منصات التعلم:**\n- **Coursera & EdX:** كورسات من Google و IBM و Harvard.\n- **Kaggle:** للتطبيق العملي والمنافسة.\n- **Datacamp:** لتعلم البرمجة بشكل تفاعلي."
}

# 4. نظام الأسئلة (Interactive Quiz)
quiz_data = [
    {"q": "أي من الـ 5V's تعبر عن دقة وجودة البيانات؟", "a": ["Veracity", "Volume", "Variety"], "correct": "Veracity"},
    {"q": "أداة متطورة تستخدم لمعالجة البيانات الضخمة:", "a": ["Hadoop", "Excel", "Notepad"], "correct": "Hadoop"},
    {"q": "البيانات الضخمة تُخزن بطريقة:", "a": ["موزعة (Distributed)", "مركزية (Centralized)", "ورقية"], "correct": "موزعة (Distributed)"}
]

# 5. إدارة الحالة (Session State)
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

# رسالة الترحيب "هل تعلم"
if "welcome" not in st.session_state:
    st.markdown(f"""<div class="welcome-box">
    👋 مرحبا انا وكيلك الذكى فى عالم البيانات الضخمة<br>
    💡 هل تعلم أن 90% من بيانات العالم تم إنتاجها في آخر سنتين فقط؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي (Sidebar)
st.sidebar.title("🎮 لوحة التحكم")
if st.sidebar.button("📝 اختبر معلوماتك (Quiz)"):
    st.session_state.active_q = random.choice(quiz_data)
    st.session_state.quiz_feedback = None
    st.session_state.view = "quiz"

if st.sidebar.button("💬 العودة للمحادثة"):
    st.session_state.view = "chat"

st.sidebar.subheader("📌 اختصارات سريعة")
if st.sidebar.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
if st.sidebar.button("⚡ الخصائص (5V's)"): st.session_state.q_auto = "خصائص"
if st.sidebar.button("⚖️ الفرق بين الأنواع"): st.session_state.q_auto = "فرق"
if st.sidebar.button("🎓 البيانات في التعليم"): st.session_state.q_auto = "تعليم"
if st.sidebar.button("🗺️ كيف أبدأ؟"): st.session_state.q_auto = "roadmap"
if st.sidebar.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم"

# 7. منطق العرض
if st.session_state.view == "quiz":
    # عرض قسم الاختبار
    q_item = st.session_state.active_q
    st.markdown(f'<div class="bot-text">📝 **سؤال التحدي:** {q_item["q"]}</div>', unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        user_choice = st.radio("اختر الإجابة الصحيحة:", q_item["a"])
        submitted = st.form_submit_button("إرسال الإجابة")
        if submitted:
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "🎯 ممتاز! إجابة صحيحة. لقد حصلت على Badge محترف البيانات!")
            else:
                st.session_state.quiz_feedback = ("error", f"❌ خطأ بسيط، الإجابة الصحيحة هي: {q_item['correct']}")
    
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)

else:
    # عرض المحادثة (Chat)
    for m in st.session_state.messages:
        role = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.bar_chart(m["chart"])

    user_input = st.chat_input("اسألني أي سؤال عن البيانات الضخمة... 🤖")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        chart_data = None
        q_low = query.lower()

        # البحث الذكي في قاعدة البيانات
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "تفرق"]): res = kb["فرق"]
        elif any(w in q_low for w in ["استخدام", "فين", "حياة", "نعمل بيها ايه", "أهمية"]): res = kb["استخدامات"]
        elif any(w in q_low for w in ["تعليم", "طالب", "مدرسة"]): res = kb["تعليم"]
        elif any(w in q_low for w in ["وظيفة", "شغل", "أشتغل"]): res = kb["وظائف"]
        elif any(w in q_low for w in ["roadmap", "خطة", "أبدأ", "كيف"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["رسم", "شكل", "مخطط"]):
            res = "📊 إليك مخطط يوضح الانفجار الهائل في حجم البيانات العالمي (بالزيتابايت):"
            chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')

        if not res: res = "عذراً يا بطل، حاول تسأل بشكل أوضح عن (التعريف، الخصائص، الاستخدامات، أو الخريطة التعليمية)!"

        # عرض الرد
        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.bar_chart(chart_data)
        
        # حفظ في التاريخ
        st.session_state.messages.append({"role": "user", "content": query})
        msg_bot = {"role": "assistant", "content": res}
        if chart_data is not None: msg_bot["chart"] = chart_data
        st.session_state.messages.append(msg_bot)
