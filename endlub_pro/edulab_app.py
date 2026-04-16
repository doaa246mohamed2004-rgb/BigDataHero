import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم نيون أزرق (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 17px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; font-size: 45px !important; text-align: center; }
    
    .bot-text {
        background-color: #0d1a26; color: #00f2ff; border-right: 5px solid #00f2ff;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2); line-height: 1.8;
    }
    
    .user-text {
        background-color: #161b22; color: #ffffff; border-left: 5px solid #30363d;
        padding: 15px; border-radius: 10px; margin-bottom: 20px;
    }
    
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background-color: #0066ff; color: white; border: none; 
        font-weight: bold; transition: 0.3s; box-shadow: 0 0 10px #0066ff;
    }
    .stButton>button:hover { 
        background-color: #00f2ff !important; color: black !important; 
        box-shadow: 0 0 20px #00f2ff; transform: scale(1.02); 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (كل المحتوى اللي طلبتيه)
kb = {
    "تعريف": "بص يا بطل، **الالبيانات الضخمة** دي عالم تاني! هي مجموعات بيانات هائلة ومعقدة بتيجي من كل حتة، والبرامج العادية بتعجز قدامها تماماً. 🔍",
    
    "خصائص": "تتميز البيانات الضخمة بخمس خصائص أساسية (الـ **5V's**): \n1. **الحجم (Volume):** كميات هائلة بالبيتابايت. \n2. **السرعة (Velocity):** تدفق مستمر في الوقت الفعلي. \n3. **التنوع (Variety):** نصوص وصور وفيديوهات وملفات صوتية. \n4. **الموثوقية (Veracity):** دقة البيانات وجودة مصادرها. \n5. **القيمة (Value):** الفائدة والنتائج الذكية اللي بنطلع بيها. ⚡",
    
    "أهمية": "بتغير شكل حياتنا! بتساعد في تحسين الرعاية الصحية، وبتخلي التسوق أذكى باقتراحات مخصصة، وبتطور المدن الذكية لتقليل الزحام، وكمان بتزود الأمان البنكي بكشف الاحتيال، وتوفر ترفيه مخصص ليك. 💎",
    
    "أنواع": "الداتا عندنا 3 أنواع يا بطل: \n1. **بيانات مهيكلة:** زي الجداول المنظمة (Excel). \n2. **بيانات غير مهيكلة:** زي الصور والفيديوهات والبوستات. \n3. **بيانات شبه مهيكلة:** زي ملفات XML و JSON. 📂",

    "مجالات": "موجودة في كل مكان: في الطب (توقع الأمراض)، في التجارة (تحليل سلوك المشترين)، في المرور (تقليل الزحام)، وفي التعليم (تخصيص المحتوى لكل طالب). 🌍",
    
    "roadmap": """🗺️ **خارطة طريق تعلم البيانات الضخمة:**
1. ابدأ بـ **Python** لسهولتها وتعدد مكتباتها.
2. اتعلم قواعد البيانات **SQL** و **NoSQL**.
3. ادرس أساسيات **الرياضيات والإحصاء** للتحليل الدقيق.
4. تعمق في **Hadoop** للتخزين و **Apache Spark** للمعالجة السريعة.
5. اتعلم أدوات العرض (**Tableau** أو **Power BI**) لعرض نتائجك.""",

    "مراحل": """⚙️ **مراحل تجميع ومعالجة البيانات:**
1. **التجميع (Ingestion):** سحب البيانات من المواقع والتطبيقات.
2. **التخزين (Storage):** حفظها في مستودعات زي **Data Lakes**.
3. **المعالجة (Processing):** تنظيف وترتيب البيانات باستخدام **Spark**.
4. **التحليل (Analysis):** استخراج الأنماط والتوقعات.
5. **العرض (Visualization):** تقديم النتائج في رسوم بيانية.""",

    "مقارنة": """⚖️ **الفرق بين البيانات العادية والبيانات الضخمة:**

**من حيث الحجم:** البيانات العادية حجمها صغير (جيجابايت)، أما الضخمة فهي هائلة (تيرابايت وبيتابايت).

**من حيث طبيعة البيانات:** العادية بتكون 'مهيكلة' ومنظمة في جداول، لكن الضخمة 'غير مهيكلة' ومتنوعة كصور وفيديوهات وتغريدات.

**من حيث السرعة:** العادية بتحدث ببطء، أما الضخمة بتتدفق بسرعة البرق وفي الوقت الفعلي.

**من حيث الأدوات:** العادية بنستخدم لها Excel و SQL، والضخمة محتاجة أدوات معقدة زي Hadoop و Spark.

**من حيث التخزين:** العادية بتخزن في مكان واحد مركزي، لكن الضخمة بتعتمد على 'التخزين الموزع' على آلاف الأجهزة."""
}

# 4. نظام الأسئلة
quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن إن الداتا صور وفيديوهات ونصوص؟", "a": ["Variety (التنوع)", "Volume (الحجم)", "Value (القيمة)"], "correct": "Variety (التنوع)"},
    {"q": "المرحلة اللي بيتم فيها تنظيف البيانات وترتيبها تسمى:", "a": ["التخزين", "المعالجة", "التجميع"], "correct": "المعالجة"},
    {"q": "أي أداة تستخدم للبيانات العادية والجداول البسيطة؟", "a": ["Hadoop", "Excel", "Apache Spark"], "correct": "Excel"}
]

# 5. إدارة الحالة
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ الوكيل الذكي")
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.quiz_feedback = None
        st.session_state.view = "quiz"
    if st.button("💬 ندردش"):
        st.session_state.view = "chat"
    st.markdown("---")
    st.subheader("🚀 وصول سريع")
    if st.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("📂 أنواع البيانات"): st.session_state.q_auto = "أنواع"
    if st.button("⚡ خصائص الـ 5Vs"): st.session_state.q_auto = "خصائص"
    if st.button("🌍 المجالات والاستخدامات"): st.session_state.q_auto = "مجالات"
    if st.button("💎 أهميتها في حياتنا"): st.session_state.q_auto = "أهمية"
    if st.button("⚖️ الفرق بين أنواع البيانات"): st.session_state.q_auto = "مقارنة"
    if st.button("🗺️ طريق مجال البيانات الضخمه"): st.session_state.q_auto = "طريق مجال البيانات الضخمه"
    if st.button("⚙️ مراحل المعالجة"): st.session_state.q_auto = "مراحل"
    if st.button("📊 رسم بياني للنمو"): st.session_state.q_auto = "رسم بياني"

# 7. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 **تحدي الأبطال:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("الإجابة:", q_item["a"])
        if st.form_submit_button("إرسال"):
            if user_choice == q_item["correct"]: st.session_state.quiz_feedback = ("success", "صح! 🎯")
            else: st.session_state.quiz_feedback = ("error", f"خطأ، الصح: {q_item['correct']}")
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        st.success(msg) if status == "success" else st.error(msg)
else:
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">👋 أهلاً بيك يا بطل! أنا وكيلك الذكي في عالم البيانات الضخمة. جاهز نكتشف كل حاجة سوا؟ 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    user_input = st.chat_input("اسألني عن أي حاجة في البيانات الضخمة...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = "كلامك جامد! حابب تعرف أكتر عن إيه؟ 😊"
        chart_data = None
        q_low = query.lower()

        if any(w in q_low for w in ["تعريف", "ماهي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["أنواع", "انواع"]): res = kb["أنواع"]
        elif any(w in q_low for w in ["خصائص", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["مجالات", "استخدامات"]): res = kb["مجالات"]
        elif any(w in q_low for w in ["أهمية", "لازمتها"]): res = kb["أهمية"]
        elif any(w in q_low for w in ["مقارنة", "فرق"]): res = kb["مقارنة"]
        elif any(w in q_low for w in ["roadmap", "طريق"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["مراحل", "خطوات"]): res = kb["مراحل"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            res = "بص يا بطل، ده رسم بياني بيوضح انفجار حجم البيانات عالمياً (بالزيتابايت) لحد سنة 2025: 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم (ZB)': [2, 15, 64, 180]}).set_index('السنة')
        
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.line_chart(chart_data)
        
        st.session_state.messages.append({"role": "user", "content": query})
        new_msg = {"role": "assistant", "content": res}
        if chart_data is not None: new_msg["chart"] = chart_data
        st.session_state.messages.append(new_msg)
