import streamlit as st
import pandas as pd
import random

# 1. إعدادات الصفحة وتنسيق الـ CSS المطور
st.set_page_config(page_title="Big Data Hero 🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* تحسين الخلفية العامة والخطوط */
    .stApp { background: linear-gradient(135deg, #010409 0%, #0d1117 100%); }
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 16px; direction: rtl; text-align: right; }
    
    /* تنسيق العناوين بتأثير نيون */
    h1 { color: #00f2ff !important; text-shadow: 0 0 15px #00f2ff; font-size: 30px !important; text-align: center; margin-bottom: 25px; border-bottom: 2px solid #1f6feb; padding-bottom: 10px; }
    h2, h3 { color: #58a6ff !important; direction: rtl; text-align: right; }

    /* تحسين شكل السايدبار */
    [data-testid="stSidebar"] { background-color: #0d1117; border-left: 2px solid #00f2ff; }
    
    /* تنسيق الأزرار لتكون تفاعلية أكثر */
    .stButton>button { 
        width: 100%; border-radius: 12px; background: linear-gradient(45deg, #1f6feb, #388bfd); 
        color: white; height: 3.2em; font-size: 14px !important; font-weight: bold;
        margin-bottom: 10px; border: none; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(31, 111, 235, 0.3);
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0, 242, 255, 0.4); border: 1px solid #00f2ff; }
    
    /* رابط اللعبة */
    .game-link {
        display: block; width: 100%; text-align: center; background: linear-gradient(45deg, #238636, #2ea043);
        color: white !important; padding: 15px; border-radius: 12px; text-decoration: none;
        font-weight: bold; font-size: 15px; margin-top: 20px; border: 1px solid #3fb950;
    }
    
    /* فقاعات الدردشة المحسنة */
    .bot-text { background-color: #0d1a26; color: #ffffff; border-right: 5px solid #00f2ff; padding: 18px; border-radius: 15px; margin-bottom: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3); line-height: 1.8; }
    .user-text { background-color: #161b22; color: #00f2ff; border-left: 5px solid #58a6ff; padding: 12px; border-radius: 12px; margin-bottom: 15px; font-weight: 500; }
    
    /* صناديق الخطوات */
    .step-box { border: 2px solid #00f2ff; padding: 12px; border-radius: 12px; margin: 8px 0; text-align: center; background: rgba(0, 242, 255, 0.1); color: #00f2ff; font-weight: bold; font-size: 18px; }
    
    #MainMenu, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات المطورة
kb = {
    "تعريف": "البيانات الضخمة (Big Data) هي 'منجم الذهب' الرقمي؛ هي كميات هائلة من المعلومات اللي بتنتج كل ثانية من موبايلاتنا، وحساسات الشوارع، وحتى الأجهزة المنزلية! 🔍✨",
    
    "الفرق": """🌟 **مقارنة الأبطال:**
1. **البيانات العادية:** زي جدول درجاتك، حجمها صغير، وسهل تفتحها على أي لابتوب.
2. **البيانات الضخمة:** حجمها بالـ 'زيتابايت' (مليار تيرابايت!)، وسرعتها رهيبة، ومحتاجة 'جيش' من السيرفرات عشان يقدر يحللها. 🔥""",

    "ذكاء_اصطناعي": """🤝 **الثنائي الخارق:**
البيانات الضخمة هي **'البنزين'** والذكاء الاصطناعي هو **'المحرك'**. 
الـ AI من غير بيانات ضخمة بيبقى زي الطفل الذكي اللي مبيقرأش كتب؛ كل ما تدي بيانات أكتر، الـ AI بيبقى عبقري في توقعاته! 🧠🤖""",

    "تغيير_الحياة": """🚀 **كيف غيرت عالمنا؟**
- **الطب الذكي:** تشخيص الأمراض قبل ما تظهر أعراضها! 🏥
- **أمانك المالي:** البنك بيعرف إن كارتك اتسرق في ثانية لو لقوا عملية شراء مش شبه عاداتك. 💳
- **مدن المستقبل:** إشارات مرور ذكية بتقلل الزحمة تلقائياً. 🚦""",

    "خصائص": """✨ **الخصائص الـ 5 (5Vs):**
1. **Volume (الحجم):** كميات خرافية.
2. **Velocity (السرعة):** بتنتج وتتحلل في لحظتها.
3. **Variety (التنوع):** صور، فيديوهات، نصوص، أصوات.
4. **Veracity (الموثوقية):** التأكد إن البيانات صحيحة مش "دوشة".
5. **Value (القيمة):** أهم حاجة.. إزاي نحولها لفلوس أو فايدة! 💎""",

    "خطوات_ترتيب": """⛓️ **مخطط رحلة البيانات الضخمة:**
<div class="step-box">1️⃣ التجميع (Collection) 📥</div>
<div style="text-align:center; color:#58a6ff;">⬇️</div>
<div class="step-box">2️⃣ التخزين (Storage) 🗄️</div>
<div style="text-align:center; color:#58a6ff;">⬇️</div>
<div class="step-box">3️⃣ المعالجة (Processing) 🧼</div>
<div style="text-align:center; color:#58a6ff;">⬇️</div>
<div class="step-box">4️⃣ التحليل (Analysis) 🧠</div>
<div style="text-align:center; color:#58a6ff;">⬇️</div>
<div class="step-box">5️⃣ اتخاذ القرار (Action) ✅</div>"""
}

# 3. إدارة الجلسة
if "messages" not in st.session_state: 
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك يا بطل في مركز الذكاء التعليمي! أنا وكيلك الذكي، اسألني عن أي شيء في عالم البيانات الضخمة. 🤖✨"}]
if "view" not in st.session_state: st.session_state.view = "chat"

# 4. الواجهة الجانبية (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.markdown('<h1>Big Data Hero</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00f2ff;text-align:center;font-size:14px;font-weight:bold;">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    
    # توزيع الأزرار بشكل أفضل
    cols = st.columns(1)
    if st.button("🔍 1. التعريف"): st.session_state.q_auto = "تعريف"
    if st.button("⚖️ 2. العادية vs الضخمة"): st.session_state.q_auto = "الفرق"
    if st.button("⚡ 3. الخصائص الـ 5"): st.session_state.q_auto = "خصائص"
    if st.button("🤖 4. علاقتها بالذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"
    if st.button("🚀 5. كيف تسهل حياتنا؟"): st.session_state.q_auto = "تسهل"
    if st.button("📈 6. رسم بياني للنمو"): st.session_state.q_auto = "رسم"
    
    st.markdown("---")
    if st.button("⛓️ رحلة البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبار الأبطال"): st.session_state.view = "quiz"
    if st.button("🔄 محادثة جديدة"): 
        st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك مجدداً! كيف يمكنني مساعدتك اليوم؟"}]
        st.session_state.view = "chat"
        st.rerun()
    
    st.markdown('<a href="https://view.genially.com/69c2cab192730eedd4af164e" target="_blank" class="game-link">🎮 العودة للمغامرة</a>', unsafe_allow_html=True)

# 5. منطق العرض
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار التحدي</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="bot-text">خلينا نشوف مين بطل البيانات الحقيقي هنا! 💪</div>', unsafe_allow_html=True)
        q1 = st.radio("1️⃣ أي خاصية تعبر عن 'تنوع' البيانات (فيديو، نصوص، صوت)؟", ["Volume", "Variety", "Velocity"])
        q2 = st.radio("2️⃣ من هو 'الوقود' الذي يغذي محرك الذكاء الاصطناعي؟", ["البيانات الضخمة", "الكهرباء فقط"])
        
        if st.button("إرسال الإجابات"):
            if q1 == "Variety" and q2 == "البيانات الضخمة":
                st.balloons()
                st.success("عبقري! إجاباتك كاملة وصحيحة 🎯")
            else:
                st.error("أوه! هناك خطأ بسيط، راجع 'المحطات التعليمية' وجرب تاني.")
else:
    st.markdown("<h1>🤖 الوكيل التعليمي الذكي</h1>", unsafe_allow_html=True)
    
    # عرض الدردشة
    chat_container = st.container()
    with chat_container:
        for m in st.session_state.messages:
            role_class = "user-text" if m["role"] == "user" else "bot-text"
            st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
            if "📊" in m["content"]:
                chart_data = pd.DataFrame({'السنة': [2010, 2015, 2020, 2025], 'حجم البيانات (زيتابايت)': [2, 12, 64, 175]})
                st.area_chart(chart_data.set_index('السنة'))

    # إدخال المستخدم
    u_input = st.chat_input("اسألني عن أي شيء...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        ans = None
        q_low = query.lower()
        
        # منطق الرد المطور
        if any(w in q_low for w in ["تعريف", "ماهي", "ما هي"]): 
            ans = kb["تعريف"] + "\n\n💡 **هل تعلم؟** أن البيانات الضخمة تسمى أيضاً 'نفط القرن الحادي والعشرين'."
        elif any(w in q_low for w in ["فرق", "عادية", "مقارنة"]): 
            ans = kb["الفرق"]
        elif any(w in q_low for w in ["ذكاء", "ai", "صناعي"]): 
            ans = kb["ذكاء_اصطناعي"]
        elif any(w in q_low for w in ["تسهل", "حياتنا", "فائدة"]): 
            ans = kb["تغيير_الحياة"]
        elif any(w in q_low for w in ["خصائص", "5"]): 
            ans = kb["خصائص"]
        elif "رسم" in q_low: 
            ans = "إليك الرسم البياني لتطور حجم البيانات عالمياً: 📊📈"
        elif any(w in q_low for w in ["ترتيب", "مخطط", "خطوات"]): 
            ans = kb["خطوات_ترتيب"]
        
        if ans is None:
            ans = "هذا سؤال ذكي جداً! بكلمات بسيطة، البيانات الضخمة هي اللي بتخلي تطبيقات زي 'تيك توك' أو 'نتفليكس' تعرف ذوقك بالظبط. تحب تعرف أكتر عن 'خصائص البيانات'؟"

        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
