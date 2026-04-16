import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="wide")

# 2. تصميم نيون أزرق احترافي (UI/UX)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 17px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; font-size: 45px !important; text-align: center; }
    
    /* صندوق رد الوكيل */
    .bot-text {
        background-color: #0d1a26; color: #00f2ff; border-right: 5px solid #00f2ff;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2); line-height: 1.8;
    }
    
    /* صندوق رسالة المستخدم */
    .user-text {
        background-color: #161b22; color: #ffffff; border-left: 5px solid #30363d;
        padding: 15px; border-radius: 10px; margin-bottom: 20px;
    }
    
    /* صندوق الترحيب */
    .welcome-box {
        background: linear-gradient(90deg, #00d4ff, #0066ff); color: white !important;
        padding: 25px; border-radius: 20px; text-align: center; font-weight: bold; 
        margin-bottom: 30px; box-shadow: 0 0 20px #00f2ff;
    }

    /* الأزرار باللون الأزرق النيون */
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

# 3. قاعدة البيانات الشاملة (محتوى علمي بأسلوب صحاب)
kb = {
    "تعريف": "بص يا صاحبي، **البيانات الضخمة** دي عاملة زي البحر المالح، كميات مرعبة ومعقدة بتيجي من كل حتة (سوشيال ميديا، حساسات، موبايلات). الفكرة إنها كبيرة لدرجة إن البرامج العادية زي Excel بتستسلم قدامها ومبتقدرش تفتحها أصلاً! 🔍",
    
    "خصائص": "ركز معايا في الـ **5V's** عشان دي أساس اللعبة:\n1. **الحجم (Volume):** داتا بالأطنان (زيتابايت).\n2. **السرعة (Velocity):** الداتا بتطير، لازم تتحلل وهي لسه طازة.\n3. **التنوع (Variety):** مش بس أرقام، لا دي صور وفيديو وفويسات.\n4. **الموثوقية (Veracity):** هل الداتا دي صح ولا أي كلام؟\n5. **القيمة (Value):** الأهم، هنستفيد إيه من كل الزيطة دي؟ ⚡",
    
    "أهمية": "ليه بنهتم بيها؟ عشان هي 'النفط الجديد'! بتساعدنا نتوقع الأمراض قبل ما تحصل، وبتحمي البنوك من السرقة، وبتحسن التعليم عشان نعرف الطالب محتاج إيه بالظبط، وبتوفر طاقة الملايين في المدن الذكية. من غيرها إحنا تايهين! 💎",
    
    "أنواع": "الداتا 3 شلل:\n- **مهيكلة (Structured):** دي المؤدبة اللي في جداول.\n- **غير مهيكلة (Unstructured):** ودي الصايعة (صور، فيديوهات) وهي 80% من بيانات العالم.\n- **شبه مهيكلة (Semi-Structured):** زي ملفات الـ JSON، نص منظمة ونص لا. 📂",
    
    "استخدامات": "موجودة في كل حتة حواليك:\n- **الصحة:** تشخيص بدقة خيالية.\n- **التجارة:** أمازون بيقترح لك اللي عاوزه بالظبط.\n- **المرور:** جوجل مابس بيعرف الزحمة منين؟ من البيانات الضخمة!\n- **الرياضة:** تحليل أداء اللاعبين عشان الفوز. 🌍",
    
    "roadmap": "عوز تبقى وحش في المجال؟ ابدأ بـ **Python**، وبعدين اتعلم **SQL**، وادخل على **Hadoop** و **Spark** عشان تسيطر على الداتا العملاقة، وأخيراً اتعلم إزاي ترسم الداتا بـ **Power BI**. 🗺️"
}

# 4. نظام الأسئلة (في صميم المحتوى)
quiz_data = [
    {"q": "إيه هي الـ V اللي بتعبر عن إن الداتا صور وفيديوهات ونصوص؟", "a": ["Variety (التنوع)", "Volume (الحجم)", "Value (القيمة)"], "correct": "Variety (التنوع)"},
    {"q": "بيانات السوشيال ميديا (الصور والبوستات) تعتبر بيانات:", "a": ["مهيكلة", "غير مهيكلة", "شبه مهيكلة"], "correct": "غير مهيكلة"},
    {"q": "ليه بنقول على البيانات الضخمة إنها 'النفط الجديد'؟", "a": ["عشان لونها أسود", "عشان قيمتها العالية في استخراج المعلومات", "عشان بتشغل العربيات"], "correct": "عشان قيمتها العالية في استخراج المعلومات"}
]

# 5. إدارة الحالة
if "messages" not in st.session_state: st.session_state.messages = []
if "quiz_feedback" not in st.session_state: st.session_state.quiz_feedback = None
if "active_q" not in st.session_state: st.session_state.active_q = random.choice(quiz_data)
if "view" not in st.session_state: st.session_state.view = "chat"

# 6. الواجهة
st.markdown("<h1>🤖 Big Data Hero - نيون برو</h1>", unsafe_allow_html=True)

if "welcome" not in st.session_state:
    st.markdown(f"""<div class="welcome-box">
    👋 أهلاً بيك! أنا وكيلك الذكي في عالم البيانات الضخمة.<br>
    💡 معلومة على الماشي: إحنا بننتج داتا في يوم واحد أكتر من اللي أنتجته البشرية في قرون! جاهز ندوس؟
    </div>""", unsafe_allow_html=True)
    st.session_state.welcome = True

# الشريط الجانبي (Sidebar)
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
    if st.button("🔍 يعني إيه بيانات ضخمة؟"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ الخصائص (5Vs)"): st.session_state.q_auto = "خصائص"
    if st.button("💎 ليه هي مهمة؟"): st.session_state.q_auto = "أهمية"
    if st.button("📂 أنواع البيانات"): st.session_state.q_auto = "أنواع"
    if st.button("🌍 بنستخدمها في إيه؟"): st.session_state.q_auto = "استخدامات"

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
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    user_input = st.chat_input("قولي أي حاجة في دماغك عن البيانات الضخمة... 🤖")
    query = user_input or st.session_state.get("q_auto")
    if "q_auto" in st.session_state: del st.session_state["q_auto"]

    if query:
        res = None
        q_low = query.lower()

        if any(w in q_low for w in ["تعريف", "ماهي", "ايه هي"]): res = "بص يا سيدي.. " + kb["تعريف"]
        elif any(w in q_low for w in ["خصائص", "مميزات", "5v"]): res = "دي أهم حتة في الموضوع.. " + kb["خصائص"]
        elif any(w in q_low for w in ["أهمية", "مهمة", "لازمتها"]): res = "سؤال في الجون! " + kb["أهمية"]
        elif any(w in q_low for w in ["نوع", "انواع", "أنواع"]): res = "بص يا صاحبي، هما 3 أنواع أساسية: " + kb["أنواع"]
        elif any(w in q_low for w in ["استخدام", "بنعمل بيها ايه", "فين"]): res = "موجودة في كل حتة حواليك! " + kb["استخدامات"]
        elif any(w in q_low for w in ["roadmap", "أبدأ", "كيف"]): res = "عاش يا بطل، ده الطريق الصح: " + kb["roadmap"]

        if not res: 
            res = "كلامك جامد! بس قولي عاوز تعرف أكتر عن (التعريف، الأنواع، الخصائص، ولا الأهمية)؟ أنا معاك 😊"

        st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {res}</div>', unsafe_allow_html=True)
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": res}) 
