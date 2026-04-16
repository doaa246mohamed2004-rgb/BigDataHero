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

# 3. قاعدة البيانات (بالعامية المصرية)
kb = {
    "تعريف": "بص يا بطل، **البيانات الضخمة** دي مجموعات بيانات هائلة ومعقدة بتيجي من كل حتة، والبرامج العادية زي Excel بتعجز قدامها تماماً. 🔍",
    
    "خصائص": "تتميز البيانات الضخمة بخمس خصائص أساسية (الـ **5V's**): الحجم (Volume) اللي بيتقاس بالبيتابايت، والسرعة (Velocity) في تدفق البيانات لحظياً، والتنوع (Variety) لأنها بتشمل نصوص وصور وفيديو، والموثوقية (Veracity) اللي بتضمن جودة البيانات، وأخيراً القيمة (Value) وهي الفائدة والنتائج الذكية اللي بنستخرجها. ⚡",
    
    "أهمية": "البيانات الضخمة بتغير حياتنا! بتساعد في تحسين الرعاية الصحية، وبتخلي التسوق أذكى باقتراحات مخصصة، وبتطور المدن الذكية لتقليل الزحام، وكمان بتزود الأمان البنكي بكشف الاحتيال. 💎",
    
    "roadmap": """🗺️ **خريطة طريق تعلم البيانات الضخمة:**
1. **البرمجة:** ابدأ بـ **Python** لسهولتها ومكتباتها الكتير.
2. **قواعد البيانات:** اتعلم **SQL** للمنظمة و **NoSQL** للبيانات غير المنظمة.
3. **الرياضيات:** أساسيات الإحصاء عشان تعرف تحلل صح.
4. **أدوات المجال:** اتعلم **Hadoop** للتخزين الموزع و **Spark** للمعالجة السريعة.
5. **العرض (Visualization):** اتقن **Tableau** أو **Power BI** لعرض نتائجك.""",

    "مراحل": """⚙️ **مراحل معالجة البيانات الضخمة:**
1. **التجميع (Ingestion):** سحب البيانات من المواقع والتطبيقات.
2. **التخزين (Storage):** حفظها في مستودعات زي **Data Lakes**.
3. **المعالجة (Processing):** تنظيف وترتيب البيانات باستخدام **Spark**.
4. **التحليل (Analysis):** استخراج الأنماط والتوقعات.
5. **العرض (Visualization):** تقديم النتائج في رسوم بيانية.""",

    "مقارنة": """⚖️ **الفرق بين البيانات العادية والضخمة:**
• **الحجم:** العادية حجمها صغير (جيجابايت)، لكن الضخمة هائلة (تيرابايت وبيتابايت).
• **الطبيعة:** العادية جداول منظمة، والضخمة متنوعة (صور وفيديوهات ومنشورات).
• **السرعة:** العادية بتحدث ببطء، لكن الضخمة بتتدفق بسرعة البرق في الوقت الفعلي.
• **الأدوات:** العادية بتتعالج بـ Excel و SQL، والضخمة محتاجة Hadoop و Spark.
• **التخزين:** العادية في جهاز واحد، والضخمة متوزعة على مئات الأجهزة المتصلة."""
}

# 4. نظام الأسئلة
quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن إن الداتا صور وفيديوهات ونصوص؟", "a": ["Variety (التنوع)", "Volume (الحجم)", "Value (القيمة)"], "correct": "Variety (التنوع)"},
    {"q": "المرحلة اللي بيتم فيها تنظيف البيانات وترتيبها تسمى:", "a": ["التخزين", "المعالجة", "التجميع"], "correct": "المعالجة"}
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
    if st.button("🗺️ الـ Roadmap"): st.session_state.q_auto = "roadmap"
    if st.button("⚖️ الفرق بين البيانات"): st.session_state.q_auto = "مقارنة"
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
    # عرض الرسايل القديمة
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.line_chart(m["chart"])

    # إدخال المستخدم
    user_input = st.chat_input("اسألني عن الـ Roadmap أو الفرق بين البيانات...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = "كلامك جامد! اسألني عن الـ Roadmap أو المقارنة. 😊"
        chart_data = None
        q_low = query.lower()

        if any(w in q_low for w in ["تعريف", "ماهي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["roadmap", "طريق", "كيف"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["فرق", "مقارنة"]): res = kb["مقارنة"]
        elif any(w in q_low for w in ["مراحل", "خطوات"]): res = kb["مراحل"]
        elif any(w in q_low for w in ["رسم", "بياني", "نمو"]):
            res = "بص يا بطل، ده رسم بياني بيوضح انفجار حجم البيانات عالمياً بالزيتابايت من 2010 لحد 2025: 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2015', '2020', '2025'], 'الحجم (ZB)': [2, 15, 64, 180]}).set_index('السنة')
        
        # عرض الرد
        st.markdown(f'<div class="user-text">👤: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.line_chart(chart_data)
        
        # حفظ في التاريخ
        st.session_state.messages.append({"role": "user", "content": query})
        new_msg = {"role": "assistant", "content": res}
        if chart_data is not None: new_msg["chart"] = chart_data
        st.session_state.messages.append(new_msg)
