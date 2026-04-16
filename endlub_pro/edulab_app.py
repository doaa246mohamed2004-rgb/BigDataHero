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
        box-shadow: 0 0 20px #00f2ff;
    }
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; height: 3em; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #ffffff !important; box-shadow: 0 0 20px #00f2ff; transform: scale(1.02); }
    table { width: 100%; color: white; border-collapse: collapse; margin: 10px 0; direction: rtl; }
    th, td { border: 1px solid #30363d; padding: 12px; text-align: center; }
    th { background-color: #00f2ff; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات بأسلوب "محادثة طبيعية"
kb = {
    "تعريف": "بصي يا ستي، البيانات الضخمة دي مش مجرد أرقام، دي 'كنز' من المعلومات المعقدة اللي بتيجي من السوشيال ميديا والحساسات بسرعة البرق، لدرجة إن الكمبيوترات العادية بتنهج قدامها ومبتعرفش تخزنها! 🔍",
    "خصائص": "سؤال ذكي! البيانات دي بنعرفها بـ 5 حاجات أساسية (5V's): أولاً 'الحجم' المرعب، وتاني حاجة 'السرعة' في التدفق، وتالت حاجة 'التنوع' (صور وفيديو ونصوص)، ورابعاً 'الموثوقية' عشان نتأكد إنها صح، وأخيراً 'القيمة' اللي بنطلع بيها في الآخر. ⚡",
    "فرق": "تخيلي الفرق بين مكتبة صغيرة في بيت (بيانات عادية) وبين مكتبة عملاقة زي مكتبة الإسكندرية (بيانات ضخمة)! العادية بتبقى جداول ومنظمة، لكن الضخمة فيها كل حاجة ومحتاجة أدوات تقيلة زي Hadoop عشان نفهمها. ⚖️",
    "استخدامات": "موجودة في كل مكان حوليكي! مثلاً 'نتفليكس' بتعرف ذوقك من تحليل بياناتك، والمدن الذكية بتنظم المرور عشان الزحمة، وحتى الدكاترة بيستخدموها عشان يتوقعوا الأمراض قبل ما تحصل. عالم مدهش صح؟ 🌍",
    "تعليم": "في التعليم هي بتعمل ثورة! البوتات بتقدر تعرف نقط ضعفك وتديكي محتوى يناسبك لوحدك (Personalized Learning)، وبتقدر تنبه المدرسين لو في طالب محتاج مساعدة زيادة. 🎓",
    "roadmap": "عشان تبقي بطلة في المجال ده، ابدئي بـ Python لأنها لغة سهلة وذكية، وبعدين SQL عشان تتعاملي مع البيانات، وادخلي بعدها على أدوات الـ Big Data زي Hadoop وSpark. الطريق ممتع جداً! 🗺️",
    "وظائف": "المستقبل كله ليكي! ممكن تشتغلي محللة بيانات، أو عالمة بيانات بتعمل نماذج ذكية، أو مهندسة أنظمة ضخمة. الرواتب والفرص في المجال ده خيالية. 💼",
    "منصات": "عندك مواقع زي Coursera وUdacity بتقدم كورسات من Google وIBM.. وكمان Kaggle ده ملعب عالمي تقدري تدربي فيه على بيانات حقيقية. 🚀"
}

# 4. نظام الأسئلة
quiz_data = [
    {"q": "تفتكري إيه الخاصية اللي معناها إن البيانات بتيجي بسرعة هائلة؟", "a": ["Velocity", "Volume", "Variety"], "correct": "Velocity"},
    {"q": "لو عاوزين نعالج بيانات ضخمة جداً، نستخدم Excel ولا Hadoop؟", "a": ["Hadoop", "Excel", "Word"], "correct": "Hadoop"},
    {"q": "البيانات اللي زي الصور والفيديو بنسميها بيانات:", "a": ["غير مهيكلة", "مهيكلة", "صغيرة"], "correct": "غير مهيكلة"}
]

# 5. إدارة الحالة
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown(f"""<div class="welcome-box">
    👋 أهلاً بيكي يا دعاء! أنا وكيلك الذكي ومساعدك في رحلة البيانات الضخمة.<br>
    💡 معلومة سريعة كدة: تخيلي إن 90% من بيانات العالم اتعملت في آخر سنتين بس! جاهزة نبدأ؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي
st.sidebar.title("🎮 غرف الوكيل")
if st.sidebar.button("📝 تحدي المعلومات (Quiz)"):
    st.session_state.active_q = random.choice(quiz_data)
    st.session_state.quiz_feedback = None
    st.session_state.view = "quiz"

if st.sidebar.button("💬 ندردش شوية"):
    st.session_state.view = "chat"

st.sidebar.subheader("📌 أسئلة شائعة")
if st.sidebar.button("🔍 يعني إيه بيانات ضخمة؟"): st.session_state.q_auto = "تعريف"
if st.sidebar.button("🌍 بنستخدمها في إيه؟"): st.session_state.q_auto = "استخدامات"
if st.sidebar.button("🗺️ عاوزة أبدأ أتعلم"): st.session_state.q_auto = "roadmap"

# 7. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.active_q
    st.markdown(f'<div class="bot-text">📝 **فكرّي في دي:** {q_item["q"]}</div>', unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        user_choice = st.radio("إجابتك إيه؟", q_item["a"])
        submitted = st.form_submit_button("ارسل الإجابة")
        if submitted:
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "يا لعيب! إجابة صحيحة عبقرية.. أنتي فعلاً Big Data Hero! 🎯")
            else:
                st.session_state.quiz_feedback = ("error", f"ممم، قربتي! بس الإجابة الأدق هي {q_item['correct']}. حاولي تاني في السؤال اللي جاي! 😊")
    
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)

else:
    for m in st.session_state.messages:
        role = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.bar_chart(m["chart"])

    user_input = st.chat_input("اسأليني كأننا بنفكر مع بعض... 🤖")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        chart_data = None
        q_low = query.lower()

        # ردود تفاعلية
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): 
            res = "سؤال ممتاز! " + kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات", "5v"]): 
            res = "بصي يا ستي، الموضوع ليه أبعاد كتير.. " + kb["خصائص"]
        elif any(w in q_low for w in ["استخدامات", "فين", "حياة", "نعمل بيها ايه", "أهمية"]): 
            res = "تصدقي إنها داخلة في كل تفصيلة في يومنا؟ " + kb["استخدامات"]
        elif any(w in q_low for w in ["تعليم", "طالب", "مدرسة"]): 
            res = "دي بقى حتتي المفضلة! " + kb["تعليم"]
        elif any(w in q_low for w in ["roadmap", "خطة", "أبدأ", "كيف"]): 
            res = "خطوة بطلة منك! " + kb["roadmap"]
        elif any(w in q_low for w in ["رسم", "شكل", "مخطط"]):
            res = "شوفي الرسم البياني ده، بيوضح إزاي البيانات بتنفجر في العالم كل سنة! 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')

        if not res: 
            res = "كلامك مثير للاهتمام! ممكن توضحي أكتر؟ أنا هنا عشان ندردش في التعريفات، الخصائص، أو إزاي تبدأي في المجال ده. 😊"

        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.bar_chart(chart_data)
        
        st.session_state.messages.append({"role": "user", "content": query})
        msg_bot = {"role": "assistant", "content": res}
        if chart_data is not None: msg_bot["chart"] = chart_data
        st.session_state.messages.append(msg_bot)
