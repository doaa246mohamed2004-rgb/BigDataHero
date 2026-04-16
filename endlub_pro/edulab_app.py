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
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; border: none; height: 3em; }
    .stButton>button:hover { background-color: #ffffff !important; color: black !important; box-shadow: 0 0 20px #00f2ff; }
    table { width: 100%; color: white; border-collapse: collapse; margin: 10px 0; direction: rtl; }
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
    "أهمية": "🌟 **أهمية البيانات الضخمة:** تساعد في اتخاذ قرارات ذكية بناءً على حقائق، التنبؤ بالأزمات، وتحسين كفاءة العمل وتقليل التكاليف.",
    "تعليم": "🎓 **في التعليم:** توفر تعلم شخصي لكل طالب، تساعد في توقع الطلاب المتعثرين، وتساعد في تطوير المناهج الدراسية.",
    "roadmap": "🗺️ **خارطة طريق التعلم:**\n1. تعلم Python\n2. تعلم SQL\n3. تحليل البيانات (Pandas)\n4. أدوات الـ Big Data (Hadoop)\n5. الذكاء الاصطناعي."
}

# 4. نظام الأسئلة المطور
quiz_data = [
    {"q": "أي خاصية تعني سرعة إنتاج وتدفق البيانات؟", "a": ["Volume", "Velocity", "Variety"], "correct": "Velocity", "exp": "صح! Velocity هي السرعة."},
    {"q": "البيانات الضخمة تُخزن في:", "a": ["خادم واحد", "خوادم موزعة", "فلاش ميموري"], "correct": "خوادم موزعة", "exp": "برافو! التخزين الموزع Distributed هو الأساس."},
    {"q": "أي أداة تستخدم للبيانات الضخمة وليس العادية؟", "a": ["Excel", "Word", "Apache Spark"], "correct": "Apache Spark", "exp": "ممتاز! Spark مخصص للبيانات الضخمة."},
    {"q": "البيانات غير المهيكلة تعني:", "a": ["جداول منظمّة", "صور وفيديوهات", "ملفات Excel"], "correct": "صور وفيديوهات", "exp": "صحيح! الصور والفيديو بيانات غير منظمة."},
    {"q": "خاصية Veracity تعني:", "a": ["حجم البيانات", "دقة وموثوقية البيانات", "تنوع المصادر"], "correct": "دقة وموثوقية البيانات", "exp": "تمام! هي التأكد من صحة المعلومة."}
]

# 5. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown("""<div class="welcome-box">👋 مرحبا! أنا وكيلك الذكي في عالم البيانات الضخمة.<br>💡 هل تعلم أن 90% من بيانات العالم تم إنتاجها في آخر سنتين فقط؟</div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# Sidebar
st.sidebar.title("🎮 لوحة التحكم")
st.sidebar.link_button("🔙 العودة إلى اللعبة", "https://view.genially.com/69c2cab192730eedd4af164e")
st.sidebar.subheader("📌 اختصارات")

if st.sidebar.button("💡 ما هي البيانات الضخمة؟"): st.session_state.q = "تعريف"
if st.sidebar.button("⚖️ الفرق بين الأنواع"): st.session_state.q = "فرق"
if st.sidebar.button("🎓 البيانات في التعليم"): st.session_state.q = "تعليم"
if st.sidebar.button("🗺️ خارطة الطريق"): st.session_state.q = "roadmap"
if st.sidebar.button("📊 رسم بياني"): st.session_state.q = "رسم"
if st.sidebar.button("📝 اختبار جديد"): 
    st.session_state.quiz_item = random.choice(quiz_data)
    st.session_state.quiz_answered = False
    st.session_state.q = "quiz"

# عرض المحادثة السابقة
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    role = "user-text" if m["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{role}">{m["content"]}</div>', unsafe_allow_html=True)
    if "chart" in m: st.bar_chart(m["chart"])

# 6. منطق السؤال والرد
input_q = st.chat_input("اسألني أي سؤال... 🤖")
query = input_q or st.session_state.get("q")
if "q" in st.session_state: del st.session_state["q"]

if query:
    if query == "quiz":
        if "quiz_item" not in st.session_state:
            st.session_state.quiz_item = random.choice(quiz_data)
            st.session_state.quiz_answered = False
        
        item = st.session_state.quiz_item
        st.markdown(f'<div class="bot-text">📝 **سؤال التحدي:** {item["q"]}</div>', unsafe_allow_html=True)
        
        # نظام حل السؤال
        with st.container():
            user_choice = st.radio("اختر الإجابة:", item["a"], key="quiz_radio")
            if st.button("إرسال الإجابة"):
                if user_choice == item["correct"]:
                    st.success(f"✅ صح! {item['exp']}")
                    st.balloons()
                else:
                    st.error(f"❌ خطأ! الإجابة الصحيحة هي: {item['correct']}")
    
    elif any(word in query.lower() for word in ["رسم", "شكل", "مخطط"]):
        res = "📊 إليك مخطط نمو البيانات العالمي بالزيتابايت:"
        df = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        st.bar_chart(df)
        st.session_state.messages.append({"role": "assistant", "content": res, "chart": df})
    
    else:
        # البحث في قاعدة البيانات
        res = None
        search_map = {
            "تعريف": ["تعريف", "ماهي", "ايه هي", "البيانات الضخمة"],
            "خصائص": ["خصائص", "5v", "مميزات"],
            "فرق": ["فرق", "مقارنة", "تفرق"],
            "تعليم": ["تعليم", "طالب", "مدرسة"],
            "roadmap": ["roadmap", "خارطة", "أبدأ"]
        }
        for cat, keywords in search_map.items():
            if any(k in query.lower() for k in keywords):
                res = kb[cat]; break
        
        if not res: res = "عذراً يا بطل، حاول تسأل بشكل أوضح (مثلاً: ما هي خصائص البيانات؟) أو استخدم الأزرار!"
        
        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": res})
