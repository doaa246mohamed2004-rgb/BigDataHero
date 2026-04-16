import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم CSS احترافي (Modern Neon UI)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 17px; direction: rtl; text-align: right; }
    h1 { color: #58a6ff !important; text-shadow: 0 0 15px #58a6ff; font-size: 45px !important; text-align: center; margin-bottom: 30px; }
    
    /* صندوق رد الوكيل */
    .bot-text {
        background-color: #161b22; color: #58a6ff; border-right: 5px solid #58a6ff;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 242, 255, 0.1); line-height: 1.8;
    }
    
    /* صندوق رسالة المستخدم */
    .user-text {
        background-color: #21262d; color: #f0f6fc; border-left: 5px solid #30363d;
        padding: 15px; border-radius: 10px; margin-bottom: 20px; font-weight: 500;
    }
    
    /* صندوق الترحيب */
    .welcome-box {
        background: linear-gradient(135deg, #1f6feb 0%, #00d4ff 100%); color: #ffffff !important;
        padding: 25px; border-radius: 20px; text-align: center; font-weight: bold; 
        margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    /* الأزرار والجداول */
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #238636; color: white; border: none; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #2ea043; box-shadow: 0 0 15px #2ea043; transform: translateY(-2px); }
    
    table { width: 100%; border-collapse: collapse; background-color: #161b22; color: white; border-radius: 10px; overflow: hidden; margin: 20px 0; }
    th { background-color: #58a6ff; color: black; padding: 15px; text-align: center; }
    td { border-bottom: 1px solid #30363d; padding: 12px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات المطورة (المحتوى العلمي الشامل)
kb = {
    "تعريف": "بصي يا ستي، **البيانات الضخمة** دي عالم تاني! هي مجموعات بيانات هائلة ومعقدة جداً، بتيجي بسرعة البرق ومن مصادر كتير (صور، حساسات، بوستات)، لدرجة إن البرامج العادية زي Excel بـ 'تهنج' قدامها ومبتعرفش تخزنها ولا تعالجها. 🔍",
    
    "خصائص": "سؤال ممتاز! البيانات دي بنعرفها بـ **الـ 5 ركائز (5V's)**:\n1. **الحجم (Volume):** كميات خيالية بالبيتابايت.\n2. **السرعة (Velocity):** تدفق لحظي زي بيانات البورصة.\n3. **التنوع (Variety):** أشكال كتير (نصوص، فيديو، صور).\n4. **الموثوقية (Veracity):** جودة ودقة البيانات.\n5. **القيمة (Value):** الفائدة اللي بنطلع بيها في الآخر. ⚡",
    
    "أنواع": "تخيلي إن البيانات 3 أنواع:\n- **مهيكلة (Structured):** منظمة في جداول زي بيانات الموظفين.\n- **غير مهيكلة (Unstructured):** ودي الأكتر انتشاراً (صور، فيديوهات، فويسات).\n- **شبه مهيكلة (Semi-Structured):** زي ملفات JSON و XML. 📂",
    
    "مراحل": "عشان نحول البيانات دي لمعلومات، بنمشي في 5 خطوات:\n1. **التجميع (Ingestion):** نسحب البيانات من كل مكان.\n2. **التخزين (Storage):** نحطها في مستودعات عملاقة (Data Lakes).\n3. **المعالجة (Processing):** ننظفها ونرتبها بـ Spark.\n4. **التحليل (Analysis):** نطلع الأنماط والتوقعات.\n5. **العرض (Visualization):** نرسمها في جداول ورسوم سهلة. ⚙️",
    
    "فرق": """⚖️ **مقارنة سريعة بين عالمين:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | جيجابايت (محدودة) | تيرابايت وأكثر |
| **البنية** | جداول منظمة | متنوعة (صور/نصوص) |
| **المعالجة** | جهاز واحد مركزى | خوادم موزعة |
| **الأدوات** | SQL, Excel | Hadoop, Spark |""",
    
    "استخدامات": "موجودة في كل تفصيلة في يومنا! مثلاً:\n- **الصحة:** تشخيص الأمراض قبل ما تزيد.\n- **التجارة:** أمازون ونون بيعرفوا ذوقك إزاي؟ بالبيانات الضخمة!\n- **المدن الذكية:** تنظيم المرور وتوفير الكهرباء.\n- **الأمن:** كشف عمليات الاحتيال البنكي في ثواني. 🌍",
    
    "roadmap": "خطوة بطلة منك! عشان تبقي خبيرة، امشي على الطريق ده:\n1. تعلمي **Python** (اللغة الأم للمجال).\n2. اتقني **SQL** و **NoSQL** للتعامل مع قواعد البيانات.\n3. افهمي **إحصاء** عشان تحللي صح.\n4. اتعلمي أدوات المجال التقيلة (**Hadoop** و **Spark**).\n5. اتعلمي أدوات العرض زي **Power BI** أو **Tableau**. 🗺️"
}

# 4. نظام الاختبار التفاعلي
quiz_data = [
    {"q": "أي نوع من البيانات يمثل الصور والفيديوهات؟", "a": ["مهيكلة", "غير مهيكلة", "شبه مهيكلة"], "correct": "غير مهيكلة"},
    {"q": "أداة تستخدم لـ 'معالجة' البيانات الضخمة وتنظيفها بسرعة؟", "a": ["Apache Spark", "Excel", "Notepad"], "correct": "Apache Spark"},
    {"q": "البيانات الضخمة تُخزن في مستودعات تسمى:", "a": ["Data Lakes", "Flash Memory", "Hard Disk"], "correct": "Data Lakes"}
]

# 5. إدارة الحالة (Session State)
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة والترحيب
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown(f"""<div class="welcome-box">
    👋 أهلاً بيكي يا دعاء! أنا وكيلك الذكي ومساعدك في عالم البيانات الضخمة.<br>
    💡 هل تعلمين أننا ننتج 2.5 كوينتليون بايت من البيانات يومياً؟ جاهزة نكتشف الكنز ده؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.title("🎮 غرف التحكم")
    if st.button("📝 تحدي المعلومات (Quiz)"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.quiz_feedback = None
        st.session_state.view = "quiz"
    
    if st.button("💬 ندردش شوية"):
        st.session_state.view = "chat"
    
    st.markdown("---")
    st.subheader("📌 وصول سريع للمعلومة")
    if st.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ الخصائص الـ 5"): st.session_state.q_auto = "خصائص"
    if st.button("⚙️ مراحل المعالجة"): st.session_state.q_auto = "مراحل"
    if st.button("⚖️ المقارنة"): st.session_state.q_auto = "فرق"
    if st.button("🗺️ كيف أبدأ؟"): st.session_state.q_auto = "roadmap"

# 7. منطق العرض (الاختبار أو المحادثة)
if st.session_state.view == "quiz":
    q_item = st.session_state.active_q
    st.markdown(f'<div class="bot-text">📝 **تحدي الأبطال:** {q_item["q"]}</div>', unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        user_choice = st.radio("إجابتك إيه يا بطلة؟", q_item["a"])
        submitted = st.form_submit_button("إرسال الإجابة")
        if submitted:
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "يا لعيب! إجابة صحيحة عبقرية.. أنتي فعلاً Big Data Hero! 🎯")
            else:
                st.session_state.quiz_feedback = ("error", f"ممم، قربتي! بس الإجابة الصح هي: **{q_item['correct']}**. حاولي تاني في السؤال اللي جاي! 😊")
    
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)

else:
    # عرض تاريخ المحادثة
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.bar_chart(m["chart"])

    # إدخال المستخدم
    user_input = st.chat_input("اسأليني عن الأنواع، المراحل، أو الاستخدامات... 🤖")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        chart_data = None
        q_low = query.lower()

        # منطق الرد التفاعلي الذكي
        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): res = "سؤال ممتاز! " + kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات", "5v"]): res = "بصي يا ستي، الموضوع ليه أبعاد كتير.. " + kb["خصائص"]
        elif any(w in q_low for w in ["نوع", "انواع", "أنواع"]): res = "البيانات مش كلها زي بعضها، بصي كدة: " + kb["أنواع"]
        elif any(w in q_low for w in ["مراحل", "خطوات", "ازاي بنعالج"]): res = "الموضوع بيمشي بنظام دقيق جداً: " + kb["مراحل"]
        elif any(w in q_low for w in ["فرق", "مقارنة", "تفرق"]): res = "الفرق جوهري وكبير، شوفي الجدول ده: " + kb["فرق"]
        elif any(w in q_low for w in ["استخدام", "أهمية", "حياة", "نعمل بيها ايه"]): res = "تصدقي إنها داخلة في كل تفصيلة في يومنا؟ " + kb["استخدامات"]
        elif any(w in q_low for w in ["roadmap", "خطة", "أبدأ", "كيف"]): res = "خطوة بطلة منك! " + kb["roadmap"]
        elif any(w in q_low for w in ["رسم", "شكل", "مخطط"]):
            res = "شوفي الرسم البياني ده، بيوضح إزاي البيانات بتنفجر في العالم كل سنة (بالزيتابايت)! 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')

        if not res: 
            res = "كلامك مثير للاهتمام يا دعاء! أنا هنا عشان ندردش في التعريفات، الأنواع، أو إزاي تبدأي في المجال ده. 😊"

        # عرض الرد الحالي
        st.markdown(f'<div class="user-text">👤 أنتِ: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.bar_chart(chart_data)
        
        # حفظ في التاريخ
        st.session_state.messages.append({"role": "user", "content": query})
        msg_bot = {"role": "assistant", "content": res}
        if chart_data is not None: msg_bot["chart"] = chart_data
        st.session_state.messages.append(msg_bot)
