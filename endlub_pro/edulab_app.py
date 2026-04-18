import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة وتنسيق الـ CSS
st.set_page_config(page_title="Big Data Hero", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 16px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 32px !important; text-align: center; margin-bottom: 30px; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; min-width: 300px; }
    
    /* تنسيق الأزرار الجانبية */
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        background-color: #1f6feb; 
        color: white; 
        height: 3.5em; 
        font-weight: bold; 
        margin-bottom: 10px;
        border: 1px solid #58a6ff;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #388bfd;
        border: 1px solid #00f2ff;
        transform: scale(1.02);
    }
    
    /* تنسيق فقاعات الدردشة */
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 5px solid #00f2ff; padding: 15px; border-radius: 15px; margin-bottom: 15px; line-height: 1.6; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 5px solid #58a6ff; padding: 12px; border-radius: 12px; margin-bottom: 15px; }
    
    /* تنسيق المخطط */
    .step-box { border: 1px solid #00f2ff; padding: 10px; border-radius: 8px; margin: 5px 0; text-align: center; background: #0d1117; color: #00f2ff; font-weight: bold; }
    .arrow { text-align: center; color: #58a6ff; font-size: 20px; }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات (Knowledge Base)
kb = {
    "تعريف": "البيانات الضخمة هي 'بحر المعلومات' الهائل الذي يحيط بنا؛ هي مجموعات بيانات ضخمة ومعقدة جداً لدرجة أن البرامج العادية لا تستطيع التعامل معها، لكنها تحمل في طياتها أسراراً تغير مستقبلنا! 🔍",
    "خصائص": """البيانات الضخمة تتميز بـ **الـ 5Vs الشهيرة**:
1. **الحجم (Volume):** كميات هائلة من الداتا.
2. **السرعة (Velocity):** تتدفق بسرعة البرق.
3. **التنوع (Variety):** صور، نصوص، فيديوهات، وأرقام.
4. **الموثوقية (Veracity):** التأكد من صحة المعلومة.
5. **القيمة (Value):** الأهم، وهي استخراج فائدة من هذه الداتا. ✨""",
    "تغيير_الحياة": "بتغير حياتنا لأنها بتخلينا نتوقع المرض قبل حدوثه، ونحل زحمة المرور قبل ما تحصل، وبتحسن تعليمنا وصحتنا وحتى طريقة تسوقنا؛ هي المحرك الخفي لمدن المستقبل الذكية! 🚀",
    "مجالات": """أبرز المجالات التي تستخدمها:
- **الطب:** لتشخيص الأمراض بدقة مذهلة. 🏥
- **التعليم:** لتخصيص المنهج لكل طالب حسب قدراته. 🎓
- **المرور:** لإدارة الخرائط الذكية وتقليل الحوادث. 🚗
- **التجارة:** لتقديم عروض تهمك أنت شخصياً. 🛒""",
    "فائدة_اللعبة": "أهلاً بك في 'مغامرة بطل البيانات'! هنا ستكتشف من هي البيانات الضخمة، وكيف تلعب دور البطولة في حياتنا، وكيف نستخدمها بذكاء لتسهيل كل خطوة نخطوها نحو المستقبل. استعد لتكون أنت المتحكم في هذا البحر من المعلومات! 🎮",
    "استفادة_تعلم": "تعلمها يجعلك 'خبير المستقبل'؛ فهي تفتح لك أبواب العمل في كبرى شركات التكنولوجيا العالمية، وتمنحك القدرة على قراءة المستقبل من خلال الأرقام. 🌟",
    "برامج": "أهم البرامج هي: **Python** للبرمجة، **Hadoop** للتخزين الضخم، **Apache Spark** للمعالجة السريعة، و **Tableau** لرسم البيانات. 💻",
    "خطوات_ترتيب": """إليك مخطط رحلة البيانات من التجميع حتى التنفيذ:
<div class="step-box">1. التجميع (Collection) 📥</div>
<div class="arrow">⬇️</div>
<div class="step-box">2. التخزين (Storage) 🗄️</div>
<div class="arrow">⬇️</div>
<div class="step-box">3. المعالجة والتنظيف (Processing) 🧼</div>
<div class="arrow">⬇️</div>
<div class="step-box">4. التحليل (Analysis) 🧠</div>
<div class="arrow">⬇️</div>
<div class="step-box">5. التنفيذ واتخاذ القرار (Action) ✅</div>""",
    "رسم_بياني": "تشير الدراسات إلى أن حجم البيانات حول العالم يتضاعف كل عامين تقريباً، ومن المتوقع أن يصل حجم الداتا العالمية إلى أكثر من 175 زيتابايت بحلول عام 2025! 📈"
}

# 3. إدارة الجلسة (Session State)
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

# 4. الواجهة الجانبية (Sidebar) بتنظيمك الجديد
with st.sidebar:
    st.markdown('<h1>Big Data Hero</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;text-align:center;font-weight:bold;">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    
    if st.button("🔍 1. تعريف البيانات الضخمة"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ 2. الخصائص والأهمية"): st.session_state.q_auto = "خصائص"
    if st.button("🚀 3. كيف تغير حياتنا؟"): st.session_state.q_auto = "تغيير"
    if st.button("🌍 4. مجالات الاستخدام"): st.session_state.q_auto = "مجالات"
    if st.button("📈 5. رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    
    st.markdown("---")
    st.markdown('<p style="color:#58a6ff;text-align:right;">🛠️ ركن الأبطال</p>', unsafe_allow_html=True)
    if st.button("🎮 فائدة اللعبة"): st.session_state.q_auto = "لعبة"
    if st.button("🎓 استفادة وبرامج التعلم"): st.session_state.q_auto = "استفادة"
    if st.button("⛓️ مخطط ترتيب البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبر ذكاءك"): st.session_state.view = "quiz"
    if st.button("💬 بدء دردشة جديدة"): 
        st.session_state.messages = []
        st.session_state.view = "chat"

# 5. منطق العرض والأسئلة (Quiz)
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار الأبطال</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="bot-text">اختبر معلوماتك في البيانات الضخمة يا بطل!</div>', unsafe_allow_html=True)
        q1 = st.radio("1. ما هي الخاصية التي تعني 'تنوع' البيانات (صور، نصوص، إلخ)؟", ["Volume", "Variety", "Velocity"])
        q2 = st.radio("2. أي مرحلة تأتي أولاً في معالجة البيانات؟", ["التحليل", "التخزين", "التجميع"])
        
        if st.button("تحقق من إجابتك"):
            score = 0
            if q1 == "Variety": score += 1
            if q2 == "التجميع": score += 1
            if score == 2: st.success("رائع! إجابات كاملة وصحيحة 🎯")
            else: st.warning(f"لقد حصلت على {score}/2، حاول مرة أخرى!")

else:
    # واجهة الدردشة
    st.markdown("<h1>🤖 الوكيل الذكي للبيانات</h1>", unsafe_allow_html=True)
    
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اسألني أي شيء عن البيانات الضخمة...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        ans = None
        q_low = query.lower()
        
        if "تعريف" in q_low or "1" in q_low: ans = kb["تعريف"]
        elif "خصائص" in q_low or "أهمية" in q_low or "2" in q_low: ans = kb["خصائص"]
        elif "تغير" in q_low or "حياتنا" in q_low or "3" in q_low: ans = kb["تغيير_الحياة"]
        elif "مجالات" in q_low or "4" in q_low: ans = kb["مجالات"]
        elif "رسم" in q_low or "نمو" in q_low or "5" in q_low: ans = kb["رسم_بياني"]
        elif "لعبة" in q_low or "مغامرة" in q_low: ans = kb["فائدة_اللعبة"]
        elif "استفادة" in q_low or "تعلم" in q_low or "برامج" in q_low: ans = kb["استفادة_تعلم"] + "\n\n" + kb["برامج"]
        elif "ترتيب" in q_low or "مخطط" in q_low or "خطوات" in q_low: ans = kb["خطوات_ترتيب"]

        if ans is None: ans = "أنا هنا لمساعدتك! اختر موضوعاً من القائمة الجانبية لنبدأ."

        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
