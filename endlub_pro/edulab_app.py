\import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم أزرق نيون احترافي
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
    
    table { width: 100%; border-collapse: collapse; background-color: #0d1a26; color: white; border-radius: 10px; margin: 20px 0; }
    th { background-color: #0066ff; color: white; padding: 15px; }
    td { border-bottom: 1px solid #30363d; padding: 12px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات
kb = {
    "تعريف": "بص يا صاحبي، **البيانات الضخمة** دي عاملة زي البحر المالح، كميات مرعبة ومعقدة بتيجي من كل حتة. الفكرة إنها كبيرة لدرجة إن البرامج العادية زي Excel بتستسلم قدامها! 🔍",
    "خصائص": "ركز معايا في الـ **5V's**:\n1. **الحجم (Volume)**\n2. **السرعة (Velocity)**\n3. **التنوع (Variety)**\n4. **الموثوقية (Veracity)**\n5. **القيمة (Value)** ⚡",
    "أهمية": "هي 'النفط الجديد'! بتساعدنا نتوقع الأمراض، ونحمي البنوك، ونطور التعليم، ونبني مدن ذكية بتفكر. 💎",
    "أنواع": "الداتا 3 شلل: **مهيكلة** (جداول)، **غير مهيكلة** (صور وفيديو)، و**شبه مهيكلة** (XML/JSON). 📂",
    "استخدامات": "في الصحة، التجارة (زي أمازون)، المرور، وحتى في الرياضة لتحليل أداء اللاعبين. 🌍",
    "roadmap": "ابدأ بـ **Python**، ثم **SQL**، ثم انطلق لـ **Hadoop** و **Spark**. 🗺️"
}

# 4. نظام الأسئلة
quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن إن الداتا صور وفيديوهات ونصوص؟", "a": ["Variety (التنوع)", "Volume (الحجم)", "Value (القيمة)"], "correct": "Variety (التنوع)"},
    {"q": "بيانات السوشيال ميديا تعتبر بيانات:", "a": ["مهيكلة", "غير مهيكلة", "شبه مهيكلة"], "correct": "غير مهيكلة"},
    {"q": "ليه بنقول على البيانات الضخمة إنها 'النفط الجديد'؟", "a": ["عشان لونها أسود", "عشان قيمتها العالية في استخراج المعلومات", "عشان بتشغل العربيات"], "correct": "عشان قيمتها العالية في استخراج المعلومات"}
]

# 5. إدارة الحالة
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة
st.markdown("<h1>🤖 Big Data Hero</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown(f"""<div class="welcome-box">
    👋 أهلاً بيك! أنا وكيلك الذكي في عالم البيانات الضخمة.<br>
    💡 معلومة على الماشي: إحنا بننتج داتا في يوم واحد أكتر من اللي أنتجته البشرية في قرون! جاهز ندوس؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي
with st.sidebar:
    st.title("⚙️ الإعدادات")
    if st.button("📝 اختبر نفسك"):
        st.session_state.active_q = random.choice(quiz_data)
        st.session_state.quiz_feedback = None
        st.session_state.view = "quiz"
    if st.button("💬 ندردش"):
        st.session_state.view = "chat"
    st.markdown("---")
    st.subheader("🚀 أسئلة سريعة")
    if st.button("🔍 ما هي البيانات الضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ الخصائص (5Vs)"): st.session_state.q_auto = "خصائص"
    if st.button("💎 الأهمية"): st.session_state.q_auto = "أهمية"
    if st.button("📂 الأنواع"): st.session_state.q_auto = "أنواع"

# 7. العرض
if st.session_state.view == "quiz":
    q_item = st.session_state.active_q
    st.markdown(f'<div class="bot-text">📝 **تحدي الصحاب:** {q_item["q"]}</div>', unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_choice = st.radio("ها.. تفتكر إيه الإجابة؟", q_item["a"])
        submitted = st.form_submit_button("إرسال")
        if submitted:
            if user_choice == q_item["correct"]:
                st.session_state.quiz_feedback = ("success", "يا لعيب! إجابة في الجون.. أنت فعلاً وحش بيانات! 🎯")
            else:
                st.session_state.quiz_feedback = ("error", f"لا يا صاحبي مش دي.. الإجابة الصح هي: {q_item['correct']}. حاول تاني!")
    if st.session_state.quiz_feedback:
        status, msg = st.session_state.quiz_feedback
        if status == "success": st.success(msg); st.balloons()
        else: st.error(msg)
else:
    # الترحيب الآلي في الدردشة
    if not st.session_state.messages:
        initial_bot_msg = "أهلاً بيك! أنا وكيلك الذكي في عالم البيانات الضخمة. تحب نبدأ بإيه النهاردة؟ 😊"
        st.session_state.messages.append({"role": "assistant", "content": initial_bot_msg})

    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    # خانة الكتابة مع النص المطلوب
    user_input = st.chat_input("اكتب سؤالك هنا...")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        q_low = query.lower()
        if any(w in q_low for w in ["تعريف", "ماهي"]): res = kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "5v"]): res = kb["خصائص"]
        elif any(w in q_low for w in ["أهمية", "لازمتها"]): res = kb["أهمية"]
        elif any(w in q_low for w in ["نوع", "أنواع"]): res = kb["أنواع"]
        elif any(w in q_low for w in ["استخدام", "فين"]): res = kb["استخدامات"]
        elif any(w in q_low for w in ["roadmap", "كيف"]): res = kb["roadmap"]

        if not res: res = "كلامك جامد! بس قولي عاوز تعرف أكتر عن إيه في البيانات الضخمة؟"

        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": res})
