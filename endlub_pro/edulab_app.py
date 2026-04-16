import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم نيون مدمج واحترافي (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 15px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 30px !important; text-align: center; margin-bottom: 20px; }
    
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; }
    .sidebar-title { color: #00f2ff !important; text-align: center; font-size: 20px; font-weight: bold; margin-bottom: 20px; }
    
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
        font-size: 13px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #00f2ff !important; color: black !important; 
        box-shadow: 0 0 12px #00f2ff; 
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات المطورة (الأقسام الجديدة)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة بتيجي من مصادر كتير، والبرامج العادية مش بتقدر تعالجها. 🔍",
    "خصائص": "**خصائص الـ 5Vs:** \n1. الحجم (Volume) \n2. السرعة (Velocity) \n3. التنوع (Variety) \n4. الموثوقية (Veracity) \n5. القيمة (Value). ⚡",
    "أهمية": "أهميتها بتكمن في قدرتها على كشف الأنماط الخفية، وتحسين الرعاية الصحية، وزيادة كفاءة المدن الذكية، وتأمين المعاملات المالية. 💎",
    "مجالات": "موجودة في كل مكان: الطب، البنوك، التجارة الإلكترونية، المواصلات، والتعليم الذكي. 🌍",
    "استخدامات": "بنستخدمها في تحليل سلوك المستهلكين، توقع الأعطال قبل حدوثها، وتحسين نتائج محركات البحث. 🛠️",
    
    "وظائف": """💼 **أهم وظائف عالم البيانات الضخمة:**
1. **محلل بيانات (Data Analyst):** بيفهم الأرقام وبيطلع منها تقارير.
2. **مهندس بيانات (Data Engineer):** بيبني 'المواسير' اللي بتنقل الداتا.
3. **عالم بيانات (Data Scientist):** بيستخدم الذكاء الاصطناعي لتوقع المستقبل.
4. **مسؤول أمن البيانات:** بيحمي المعلومات من الاختراق. 🛡️""",

    "استفادة": """🌟 **ليه تتعلم بيانات ضخمة؟**
1. **فرص عمل بمرتبات عالية:** الطلب عليها عالمي ومستمر.
2. **تطوير مهارات التفكير المنطقي:** بتعلمك إزاي تاخد قرارات بناءً على حقائق.
3. **القدرة على حل المشكلات المعقدة:** هتكون قادر تفهم مشاكل كانت مستحيلة الحل زمان. 🚀""",

    "تعليم": """🎓 **تسهيلات البيانات الضخمة في التعليم:**
1. **التعلم الشخصي:** تخصيص المحتوى لكل طالب حسب مستواه وسرعته.
2. **التنبؤ بالنتائج:** مساعدة المدرسين في معرفة الطلاب اللي محتاجين دعم بدري.
3. **تحسين المناهج:** معرفة إيه الأجزاء اللي الطلاب بيفهموها بسرعة وإيه اللي بيحتاج شرح أكتر. 📚""",

    "roadmap": "ابدأ بـ Python، ثم قواعد البيانات SQL، ثم الإحصاء، وبعدها Hadoop و Spark. 🗺️",
    "مقارنة": "البيانات العادية حجمها صغير وتخزن في جهاز واحد، أما الضخمة فهي هائلة وموزعة على شبكة أجهزة. ⚖️"
}

# 4. إدارة الحالة والأسئلة (أسئلة منطقية للطلبة)
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن 'سرعة' تدفق البيانات؟", "a": ["Velocity (السرعة)", "Volume (الحجم)", "Variety (التنوع)"], "correct": "Velocity (السرعة)"},
    {"q": "مين الشخص المسؤول عن بناء أنظمة نقل وتخزين البيانات الضخمة؟", "a": ["مهندس البيانات", "محلل البيانات", "المصمم"], "correct": "مهندس البيانات"},
    {"q": "إزاي بتفيد البيانات الضخمة الطالب في التعليم؟", "a": ["تخصيص المحتوى حسب مستواه", "زيادة عدد ساعات الدراسة", "إلغاء المناهج"], "correct": "تخصيص المحتوى حسب مستواه"}
]

# 5. الواجهة
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="sidebar-title">⚙️ الوكيل الذكي</p>', unsafe_allow_html=True)
    if st.button("📝 اختبر نفسك (Quiz)"): 
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.view = "quiz"
    if st.button("💬 ندردش"): st.session_state.view = "chat"
    st.markdown("---")
    st.subheader("🚀 وصول سريع للمحتوى")
    if st.button("🔍 التعريف"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ الخصائص (5Vs)"): st.session_state.q_auto = "خصائص"
    if st.button("💼 وظائف المجال"): st.session_state.q_auto = "وظائف"
    if st.button("🌟 فايدة تعلمها"): st.session_state.q_auto = "استفادة"
    if st.button("📚 دورها في التعليم"): st.session_state.q_auto = "تعليم"
    if st.button("📊 الرسم البياني"): st.session_state.q_auto = "رسم بياني"

# 6. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 **سؤال للأبطال:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("اختار الإجابة:", q_item["a"])
        if st.form_submit_button("إرسال الإجابة"):
            if user_choice == q_item["correct"]:
                st.success("صح يا عبقري! 🎯")
                st.balloons()
            else: st.error(f"للأسف خطأ.. الصح هو: {q_item['correct']}")
else:
    # رسالة الترحيب الأولى
    if not st.session_state.messages:
        welcome_msg = "👋 مرحباً بك! أنا وكيلك الذكي في تعلم البيانات الضخمة. جاهز نكتشف سوا إزاي العالم ده بيشتغل؟ 😊"
        st.markdown(f'<div class="bot-text">{welcome_msg}</div>', unsafe_allow_html=True)

    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    u_input = st.chat_input("اسألني عن الوظائف، التعليم، أو الاستفادة...")
    query = u_input or st.session_state.get("q_auto")
    
    if query:
        q_low = query.lower()
        ans = "معلومة مهمة! حابب تعرف إيه تاني بخصوص عالم البيانات الضخمة؟ 😊"
        chart = None
        
        if any(w in q_low for w in ["تعريف", "ماهي", "يعني ايه"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "5v"]): ans = kb["خصائص"]
        elif any(w in q_low for w in ["وظائف", "شغل", "أشتغل"]): ans = kb["وظائف"]
        elif any(w in q_low for w in ["استفادة", "ليه أتعلم", "فايدة"]): ans = kb["استفادة"]
        elif any(w in q_low for w in ["تعليم", "مدرسة", "طالب"]): ans = kb["تعليم"]
        elif any(w in q_low for w in ["أهمية", "اهميه"]): ans = kb["أهمية"]
        elif any(w in q_low for w in ["مجالات", "فين"]): ans = kb["مجالات"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            ans = "بص على الانفجار الهائل في حجم البيانات عالمياً لحد سنة 2025: 📊"
            chart = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم (ZB)': [2, 15, 64, 180]}).set_index('السنة')

        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {ans}</div>', unsafe_allow_html=True)
        if chart is not None: st.line_chart(chart)
        
        st.session_state.messages.append({"role": "user", "content": query})
        msg = {"role": "assistant", "content": ans}
        if chart is not None: msg["chart"] = chart
        st.session_state.messages.append(msg)
        
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
