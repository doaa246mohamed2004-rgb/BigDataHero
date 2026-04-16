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

    table { width: 100%; border-collapse: collapse; margin: 20px 0; color: white; background-color: #0d1a26; }
    th { background-color: #0066ff; color: white; padding: 10px; text-align: center; border: 1px solid #30363d; }
    td { border: 1px solid #30363d; padding: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات (بالعامية المصرية)
kb = {
    "تعريف": "بص يا بطل، **البيانات الضخمة** دي عالم تاني! هي مجموعات بيانات هائلة ومعقدة بتيجي من كل حتة (سوشيال ميديا، موبايلات، حساسات)، والبرامج العادية زي Excel بتعجز قدامها تماماً. 🔍",
    
    "خصائص": "ركز معايا في الـ **5V's** عشان دول أصل الحكاية:\n1. **الحجم (Volume):** داتا مرعبة بالبيتابايت.\n2. **السرعة (Velocity):** تدفق سريع جداً في الوقت الفعلي.\n3. **التنوع (Variety):** نصوص، صور، فيديوهات، وفويسات.\n4. **الموثوقية (Veracity):** دقة البيانات وصحة مصادرها.\n5. **القيمة (Value):** النتائج والفوائد الذكية اللي بنطلع بيها. ⚡",
    
    "أهمية": "البيانات الضخمة بتغير حياتنا! بتساعد في تشخيص الأمراض بدقة، وبتخلي التسوق أسهل باقتراحات مخصصة ليك، وبتطور المدن الذكية عشان تقلل الزحام، وحتى في كشف الاحتيال البنكي وحماية خصوصيتك. 💎",
    
    "roadmap": """🗺️ **عشان تبدأ صح في المجال ده، امشي على الطريق ده:**
1. **البرمجة:** ابدأ بـ **Python** عشان سهلة وليها مكتبات كتير.
2. **قواعد البيانات:** اتعلم **SQL** للبيانات المنظمة و **NoSQL** للبيانات الضخمة.
3. **الرياضيات:** أساسيات الإحصاء هي اللي هتخليك تفهم الداتا صح.
4. **الأدوات التقنية:** اتعمق في **Hadoop** للتخزين و **Spark** للمعالجة السريعة.
5. **العرض (Visualization):** اتعلم **Power BI** أو **Tableau** عشان ترسم نتائجك بشكل احترافي.""",

    "مراحل": """⚙️ **مراحل طبخ البيانات (عشان نطلع معلومة مفيدة):**
1. **التجميع (Ingestion):** بنسحب الداتا من المواقع والتطبيقات.
2. **التخزين (Storage):** بنحطها في مستودعات عملاقة زي **Data Lakes**.
3. **المعالجة (Processing):** تنظيف وترتيب الداتا باستخدام أدوات زي **Spark**.
4. **التحليل (Analysis):** هنا بنطلع الأنماط والتوقعات الذكية.
5. **العرض (Visualization):** تقديم النتائج في صور ورسوم سهلة الفهم.""",

    "مقارنة": """⚖️ **الفرق بين البيانات العادية والضخمة في كلمتين:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | جيجابايت (صغير) | تيرابايت وبيتابايت (هائل) |
| **البنية** | مهيكلة (جداول ومنظمة) | غير مهيكلة (صور وفيديوهات) |
| **السرعة** | تحديث بطيء (شهرياً مثلاً) | سرعة البرق (في ثواني) |
| **الأدوات** | Excel / SQL | Hadoop / Spark |
| **التخزين** | جهاز واحد أو سيرفر | تخزين موزع على آلاف الأجهزة |"""
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

# 6. الواجهة والعنوان
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

# الشريط الجانبي
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
    if st.button("🔍 يعني إيه بيانات ضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("🗺️ الطريق للمجال (Roadmap)"): st.session_state.q_auto = "roadmap"
    if st.button("⚖️ الفرق بين أنواع البيانات"): st.session_state.q_auto = "مقارنة"
    if st.button("⚡ خصائص الـ 5Vs"): st.session_state.q_auto = "خصائص"
    if st.button("⚙️ مراحل المعالجة"): st.session_state.q_auto = "مراحل"
    if st.button("💎 أهميتها في حياتنا"): st.session_state.q_auto = "أهمية"

# 7. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.get("active_q", quiz_data[0])
    st.markdown(f'<div class="bot-text">📝 **تحدي الأبطال:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("تفتكر إيه الإجابة؟", q_item["a"])
        submitted = st.form_submit_button("إرسال")
        if submitted:
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "يا لعيب! إجابة صحيحة عبقرية! 🎯")
            else:
                st.session_state.quiz_feedback = ("error", f"حاول تاني يا بطل! الصح هي: {q_item['correct']}")
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)
else:
    # الترحيب الأولي
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">👋 أهلاً بيك يا بطل! أنا وكيلك الذكي في عالم البيانات الضخمة.   😊</div>', unsafe_allow_html=True)
    
    # عرض تاريخ المحادثة
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    # خانة الكتابة
    user_input = st.chat_input("اكتب سؤالك هنا يا بطل...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = ""
        q_low = query.lower()

        # منطق الردود
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["roadmap", "طريق", "كيف ابدأ"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "انواع"]): res = kb["مقارنة"]
        elif any(w in q_low for w in ["مراحل", "خطوات", "معالجة"]): res = kb["مراحل"]
        elif any(w in q_low for w in ["خصائص", "5v", "مميزات"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["أهمية", "لازمتها", "حياتنا"]): res = kb["أهمية"]
        else:
            res = "كلامك جامد! بس قولي حابب ندردش في (التعريف، الـ Roadmap، مراحل المعالجة، ولا المقارنة)؟"

        # عرض الرد الحالي وحفظه
        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": res})
