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
    
    .welcome-box {
        background: linear-gradient(90deg, #00d4ff, #0066ff); color: white !important;
        padding: 25px; border-radius: 20px; text-align: center; font-weight: bold; 
        margin-bottom: 30px; box-shadow: 0 0 20px #00f2ff;
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

    /* تنسيق الجداول لتناسب ستايل النيون */
    table { width: 100%; border-collapse: collapse; margin: 20px 0; color: white; }
    th { background-color: #0066ff; color: white; padding: 10px; text-align: center; }
    td { border: 1px solid #30363d; padding: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (المحتوى المضاف)
kb = {
    "تعريف": "بص يا بطل، **البيانات الضخمة** دي عالم تاني! هي مجموعات بيانات هائلة ومعقدة بتيجي من كل حتة، والبرامج العادية بتعجز قدامها. 🔍",
    
    "خصائص": "ركز معايا في الـ **5V's**:\n1. **الحجم (Volume):** داتا بالأطنان.\n2. **السرعة (Velocity):** تدفق لحظي.\n3. **التنوع (Variety):** صور وفيديو ونصوص.\n4. **الموثوقية (Veracity):** جودة ودقة البيانات.\n5. **القيمة (Value):** الفائدة اللي بنطلع بيها. ⚡",
    
    "أهمية": "هي 'النفط الجديد'! بتساعدنا نتوقع الأمراض، ونحمي البنوك من الاحتيال، ونبني مدن ذكية بتوفر طاقة. 💎",
    
    "أنواع": "الداتا 3 أنواع: **مهيكلة** (جداول)، **غير مهيكلة** (صور وفيديو)، و**شبه مهيكلة** (XML/JSON). 📂",
    
    "roadmap": """🗺️ **خارطة الطريق لدخول المجال:**
1. **تعلم لغة برمجة:** ابدأ بـ **Python** فهي الأفضل.
2. **قواعد البيانات:** تعلم **SQL** للبيانات المنظمة و **NoSQL** للضخمة.
3. **الرياضيات والإحصاء:** عشان تفهم تحليل البيانات صح.
4. **أدوات المجال:** اتعلم **Hadoop** للتخزين و **Spark** للمعالجة.
5. **تحليل البيانات:** اتقن أدوات العرض زي **Tableau** أو **Power BI**.""",

    "مراحل": """⚙️ **مراحل تجميع ومعالجة البيانات:**
1. **التجميع (Ingestion):** سحب البيانات من المواقع والتطبيقات.
2. **التخزين (Storage):** وضعها في مستودعات زي **Data Lakes**.
3. **المعالجة (Processing):** تنظيف وترتيب البيانات باستخدام **Spark**.
4. **التحليل (Analysis):** استخراج الأنماط والتوقعات.
5. **العرض (Visualization):** تقديم النتائج في رسوم بيانية.""",

    "مقارنة": """⚖️ **الفرق بين البيانات العادية والضخمة:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | جيجابايت (محدودة) | تيرابايت وأكثر |
| **البنية** | مهيكلة (جداول) | متنوعة (صور/نصوص) |
| **المعالجة** | مركزية (جهاز واحد) | موزعة (عدة خوادم) |
| **الأدوات** | SQL, Excel | Hadoop, Spark |"""
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
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
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
    if st.button("🗺️ خارطة الطريق (Roadmap)"): st.session_state.q_auto = "roadmap"
    if st.button("⚖️ مقارنة البيانات"): st.session_state.q_auto = "مقارنة"
    if st.button("⚙️ مراحل المعالجة"): st.session_state.q_auto = "مراحل"

# 7. منطق العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.active_q
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
    if not st.session_state.messages:
        st.markdown('<div class="bot-text">👋 أهلاً بيك! أنا وكيلك الذكي. جاهز تكتشف مراحل معالجة البيانات الضخمة أو تاخد الـ Roadmap؟ 😊</div>', unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "chart" in m: st.bar_chart(m["chart"])

    user_input = st.chat_input("اكتب سؤالك هنا (عن الطريق، الفرق، أو المراحل)...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = ""
        chart_data = None
        q_low = query.lower()

        if any(w in q_low for w in ["تعريف", "ماهي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["roadmap", "طريق", "كيف ابدأ"]): res = kb["roadmap"]
        elif any(w in q_low for w in ["فرق", "مقارنة"]): res = kb["مقارنة"]
        elif any(w in q_low for w in ["مراحل", "خطوات", "تجميع"]): res = kb["مراحل"]
        elif any(w in q_low for w in ["خصائص", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["رسم", "بياني"]):
            res = "إليك نمو البيانات عالمياً: 📊"
            chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        else:
            res = "كلامك جامد! اسألني عن الـ Roadmap أو مراحل المعالجة أو الفرق بين أنواع البيانات. 😊"

        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        if chart_data is not None: st.bar_chart(chart_data)
        
        st.session_state.messages.append({"role": "user", "content": query})
        new_msg = {"role": "assistant", "content": res}
        if chart_data is not None: new_msg["chart"] = chart_data
        st.session_state.messages.append(new_msg)
