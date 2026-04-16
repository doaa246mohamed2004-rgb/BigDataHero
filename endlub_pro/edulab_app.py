import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم الواجهة النيون (CSS) - عشان تليق على لعبتك
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #ffffff !important; font-family: 'Arial'; font-size: 19px; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 45px !important; text-align: center; }
    .bot-text {
        color: #00f2ff; font-weight: bold; padding: 20px; border-right: 6px solid #00f2ff;
        background-color: #091a2a; border-radius: 15px; margin-bottom: 15px;
        direction: rtl; text-align: right; box-shadow: 0 0 15px #00f2ff;
    }
    .user-text {
        color: #ffffff; font-weight: bold; padding: 15px; direction: rtl;
        text-align: right; border-bottom: 2px solid #30363d; margin-bottom: 15px;
    }
    .stChatInput { direction: rtl; border-color: #00f2ff !important; }
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات (مجهزة للرد بالعامية والفصحى)
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة هي: مجموعات بيانات ضخمة جداً ومعقدة، البرامج العادية مش بتقدر تتعامل معاها ولا تحللها.",
    "خصائص": "📌 الخصائص الأساسية (3Vs):\n\n1. Volume (الحجم): يعني كمية بيانات مهولة.\n2. Velocity (السرعة): سرعة إنتاج البيانات وتدفقها.\n3. Variety (التنوع): أنواع كتيرة زي الصور والفيديوهات والنصوص.",
    "خطوات": "👣 خطوات التحليل:\n1. الجمع والفرز.\n2. التخزين والمعالجة.\n3. التحليل والاستنتاج.\n4. اتخاذ القرار.",
    "أهمية": "🌟 الأهمية: بتساعدنا نفهم المستقبل، وناخد قرارات ذكية في الطب والتجارة والتعليم.",
    "الطب": "🏥 الرعاية الصحية: بنستخدمها عشان نتوقع الأمراض قبل ما تحصل ونعالج الناس بدقة أكتر.",
    "النقل": "🚗 النقل: بتساعد في تنظيم زحمة المرور وإدارة العربيات اللي بتمشي لوحدها.",
    "وظائف": "👨‍💻 تشتغل إيه؟\nممكن تكون (محلل بيانات) أو (مهندس بيانات ضخمة) أو (خبير ذكاء اصطناعي). دي وظائف المستقبل!",
    "مصادر": "🌐 بتيجي منين؟\nمن السوشيال ميديا، والـ GPS، والساعات الذكية، وحتى عمليات الشراء أونلاين.",
    "فرق": "⚖️ الفرق: البيانات العادية بسيطة وبتتحط في جداول إكسيل، أما الضخمة فهي كميات جبارة وعشوائية ومحتاجة تكنولوجيا متطورة.",
    "خطر": "🛡️ الأمان الرقمي:\nلازم نحمي البيانات دي بالتشفير، ونطبق قوانين (المواطنة الرقمية) عشان نحافظ على خصوصية الناس."
}

# 4. كلمات البحث (keywords) - أضفت كلمات عامية عشان يفهم الطالب
keywords = {
    "تعريف": ["تعريف", "يعني ايه", "ماهي", "ايه هي", "بتاعة ايه"],
    "خصائص": ["خصائص", "مميزات", "v3", "بتتكون من", "صفاتها"],
    "خطوات": ["خطوات", "ازاي", "طريقة", "مراحل"],
    "أهمية": ["أهمية", "اهميه", "فائدة", "لازمتها", "بنستفيد"],
    "الطب": ["طب", "صحة", "دكتور", "علاج"],
    "النقل": ["نقل", "مرور", "عربيات", "زحمة"],
    "وظائف": ["وظيفة", "وظائف", "شغل", "أشتغل", "مستقبل"],
    "مصادر": ["مصدر", "بتيجي منين", "مكانها", "منين"],
    "فرق": ["فرق", "مقارنة", "عادية", "تفرق"],
    "خطر": ["خطر", "أمان", "خصوصية", "سرقة", "اختراق"]
}

# 5. الواجهة الرئيسية
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

# زرار العودة للعبة (تم وضع اللينك الخاص بكِ)
st.sidebar.title("🎮 التحكم")
genially_link = "https://view.genially.com/69c2cab192730eedd4af164e"
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role_class = "user-text" if message["role"] == "user" else "bot-text"
    role_name = "👤 أنت" if message["role"] == "user" else "🤖 الوكيل"
    st.markdown(f'<div class="{role_class}">{role_name}: {message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        if message["type"] == "bar": st.bar_chart(message["chart"])
        else: st.area_chart(message["chart"])

# 6. استقبال الأسئلة
query = st.chat_input("اسألني أي حاجة عن البيانات الضخمة... 🤖")

if query:
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})
    q_lower = query.lower()
    
    response = None
    msg_data = {"role": "assistant"}

    # 1. البحث في المعلومات أولاً (عشان ميتلخبطش مع الرسم البياني)
    found_key = None
    for key, words in keywords.items():
        if any(word in q_lower for word in words):
            found_key = key
            break
    
    if found_key:
        response = knowledge_base[found_key]
    # 2. لو طلب رسم بياني (بكلمات محددة)
    elif any(word in q_lower for word in ["رسم بياني", "شكل بياني", "مخطط"]):
        response = "📊 ده رسم بياني بيوضح إزاي حجم البيانات بيزيد بجنون في العالم:"
        chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        msg_data["chart"] = chart_data
        msg_data["type"] = "bar"
    elif "غير" in q_lower or "شكل تاني" in q_lower:
        response = "✅ غيرت لك الشكل! ده مخطط مساحي نيون يوضح تضخم البيانات:"
        chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        msg_data["chart"] = chart_data
        msg_data["type"] = "area"
    
    if not response:
        response = "معلش يا بطل مش فاهمك، اسألني عن (تعريف، خصائص، وظائف، أو اطلب رسم بياني) وهجاوبك فوراً!"

    msg_data["content"] = response
    st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
    
    if "chart" in msg_data:
        if msg_data["type"] == "bar": st.bar_chart(msg_data["chart"])
        else: st.area_chart(msg_data["chart"])
        
    st.session_state.messages.append(msg_data)
