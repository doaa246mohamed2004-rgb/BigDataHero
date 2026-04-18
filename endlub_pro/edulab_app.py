import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة وتنسيق الـ CSS
st.set_page_config(page_title="Big Data Hero", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 16px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 26px !important; text-align: center; margin-bottom: 20px; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 1px solid #00f2ff; min-width: 280px; }
    
    /* تنسيق الأزرار الجانبية */
    .stButton>button { 
        width: 100%; border-radius: 10px; background-color: #1f6feb; 
        color: white; height: 3em; font-size: 13px !important; 
        margin-bottom: 8px; border: 1px solid #58a6ff; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #388bfd; border: 1px solid #00f2ff; transform: scale(1.02); }
    
    .game-link {
        display: block; width: 100%; text-align: center; background-color: #238636;
        color: white !important; padding: 12px; border-radius: 10px; text-decoration: none;
        font-weight: bold; font-size: 14px; margin-top: 20px; border: 1px solid #3fb950;
    }
    
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 5px solid #00f2ff; padding: 15px; border-radius: 15px; margin-bottom: 15px; line-height: 1.6; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 5px solid #58a6ff; padding: 12px; border-radius: 12px; margin-bottom: 15px; }
    
    .step-box { border: 1px solid #00f2ff; padding: 10px; border-radius: 8px; margin: 5px 0; text-align: center; background: #0d1117; color: #00f2ff; font-weight: bold; }
    .arrow { text-align: center; color: #58a6ff; font-size: 20px; }
    
    #MainMenu, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات الشاملة (Knowledge Base)
kb = {
    "تعريف": "البيانات الضخمة هي 'النفط الجديد'؛ مجموعات بيانات هائلة ومعقدة جداً نحتاج لأدوات غير تقليدية لاستخراج الكنوز منها. 🔍",
    
    "الفرق": """**الفرق بين البيانات العادية والضخمة:**
1. **البيانات العادية:** زي ملفات Excel، حجمها صغير، نقدر نعالجها بجهاز لابتوب عادي.
2. **البيانات الضخمة:** حجمها بالـ 'زيتابايت'، متنوعة (فيديو، صوت، حساسات)، ومحتاجة سيرفرات عملاقة ومعالجة موزعة (Distributed Processing) لأن الجهاز الواحد هينفجر لو حاول يشغلها! 💻🔥""",

    "ذكاء_اصطناعي": """**علاقة البيانات بالذكاء الاصطناعي (AI):**
البيانات الضخمة هي **'الغذاء'** والذكاء الاصطناعي هو **'المحرك'**. 
بدون بيانات ضخمة، الذكاء الاصطناعي مش هيقدر يتعلم؛ فكل ما زادت البيانات، زادت دقة الآلة في اتخاذ القرارات والتوقعات. هما وجهان لعملة واحدة! 🧠🤖""",

    "تغيير_الحياة": """البيانات الضخمة بتسهل حياتنا بشكل مذهل:
- **تخصيص الحياة:** التطبيقات بتفهم مودك وبترشح لك الأغاني والأفلام اللي تحبها (Personalization).
- **منع الجرائم:** البنوك بتكشف السرقة قبل ما تتم عن طريق تحليل نمط صرفك اللحظي.
- **إنقاذ الأرواح:** الساعات الذكية بتحلل بيانات قلبك وتتصل بالإسعاف لو حست بخطر وشيك.
- **المدن الذكية:** إشارات المرور بتعرف أماكن الزحمة وتفتح تلقائياً عشان تخلص مشوارك أسرع. 🚀""",

    "مجالات": """تطبيقات عملية مذهلة:
- **🏥 الطب:** تحليل ملايين السجلات الطبية لاكتشاف وباء قبل انتشاره بأسابيع.
- **🎓 التعليم:** 'التعلم التكيفي'؛ المنهج بيتغير شكله وصعوبته عشان يناسب سرعة فهمك إنت شخصياً.
- **🚗 المرور:** تقليل الحوادث بنسبة 40% عن طريق تحليل سلوك السائقين والطرق.
- **🛒 التجارة:** الشركات بتصنع اللي إنت محتاجه "بالظبط" قبل ما تطلبه حتى! ✨""",

    "خصائص": "تتميز بـ الـ 5Vs: (Volume, Velocity, Variety, Veracity, Value). ✨",
    "استفادة_تعلم": "تعلمها يجعلك 'بطل المستقبل'؛ فهي تفتح لك فرص عمل برواتب خرافية في جوجل وفيسبوك! 🌟",
    "خطوات_ترتيب": """مخطط رحلة البيانات:
<div class="step-box">1. التجميع 📥</div>
<div class="arrow">⬇️</div>
<div class="step-box">2. التخزين 🗄️</div>
<div class="arrow">⬇️</div>
<div class="step-box">3. المعالجة 🧼</div>
<div class="arrow">⬇️</div>
<div class="step-box">4. التحليل 🧠</div>
<div class="arrow">⬇️</div>
<div class="step-box">5. التنفيذ ✅</div>"""
}

# 3. إدارة الجلسة
if "messages" not in st.session_state: st.session_state.messages = []
if "view" not in st.session_state: st.session_state.view = "chat"

# 4. الواجهة الجانبية (Sidebar)
with st.sidebar:
    st.markdown('<h1>Big Data Hero</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;text-align:center;font-size:13px;">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    
    if st.button("🔍 1. تعريف البيانات"): st.session_state.q_auto = "تعريف"
    if st.button("⚖️ 2. العادية vs الضخمة"): st.session_state.q_auto = "الفرق"
    if st.button("⚡ 3. الخصائص الـ 5"): st.session_state.q_auto = "خصائص"
    if st.button("🤖 4. علاقتها بالذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"
    if st.button("🚀 5. كيف تسهل حياتنا؟"): st.session_state.q_auto = "تسهل"
    if st.button("🌍 6. مجالات الاستخدام"): st.session_state.q_auto = "مجالات"
    if st.button("📈 7. رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    
    st.markdown("---")
    if st.button("⛓️ مخطط ترتيب البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبر ذكاءك"): st.session_state.view = "quiz"
    if st.button("💬 بدء دردشة جديدة"): 
        st.session_state.messages = []
        st.session_state.view = "chat"
    
    st.markdown('<a href="https://view.genially.com/69c2cab192730eedd4af164e" target="_blank" class="game-link">🎮 العودة إلى مغامرة البيانات</a>', unsafe_allow_html=True)

# 5. منطق العرض
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار الأبطال</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="bot-text">اختبر معلوماتك يا بطل!</div>', unsafe_allow_html=True)
        q1 = st.radio("1. أي نوع بيانات يحتاج لمعالجة موزعة (Distributed Processing)؟", ["البيانات العادية", "البيانات الضخمة"])
        q2 = st.radio("2. العلاقة بين البيانات والذكاء الاصطناعي هي:", ["البيانات غذاء للذكاء الاصطناعي", "لا توجد علاقة"])
        if st.button("تحقق من إجابتك"):
            if q1 == "البيانات الضخمة" and q2 == "البيانات غذاء للذكاء الاصطناعي": st.success("رائع! أنت مشروع عالم بيانات ناجح 🎯")
            else: st.warning("حاول مرة أخرى لتصحح معلوماتك!")
else:
    st.markdown("<h1>🤖 الوكيل الذكي للبيانات</h1>", unsafe_allow_html=True)
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "رسم_بياني_تفاعلي" in m["content"]:
            chart_data = pd.DataFrame({'السنة': [2010, 2015, 2020, 2025], 'الزيتابايت': [2, 12, 64, 175]})
            st.area_chart(chart_data.set_index('السنة'))

    u_input = st.chat_input("اسألني أي شيء عن البيانات والذكاء الاصطناعي...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        ans = None
        q_low = query.lower()
        
        # منطق بحث مرن للرد على الأسئلة
        if any(w in q_low for w in ["تعريف", "ماهي", "ما هي"]): ans = kb["تعريف"]
        elif any(w in q_low for w in ["فرق", "عادية", "مقارنة"]): ans = kb["الفرق"]
        elif any(w in q_low for w in ["ذكاء", "ai", "صناعي"]): ans = kb["ذكاء_اصطناعي"]
        elif any(w in q_low for w in ["تسهل", "حياتنا", "فائدة"]): ans = kb["تغيير_الحياة"]
        elif any(w in q_low for w in ["مجالات", "طب", "تعليم", "مرور"]): ans = kb["مجالات"]
        elif any(w in q_low for w in ["خصائص", "5"]): ans = kb["خصائص"]
        elif "رسم" in q_low: ans = "إليك الرسم البياني لنمو البيانات: رسم_بياني_تفاعلي 📈"
        elif any(w in q_low for w in ["ترتيب", "مخطط", "خطوات"]): ans = kb["خطوات_ترتيب"]
        
        if ans is None: ans = "سؤال رائع! بكلمات بسيطة، البيانات الضخمة هي المحرك اللي بيخلي التكنولوجيا اللي حوالينا تبان كأنها سحر. جرب تضغط على 'علاقتها بالذكاء الاصطناعي' عشان تعرف أكتر!"

        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
