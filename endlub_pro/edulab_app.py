import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة (تظهر في تبويب المتصفح) - كبرت الأيقونة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم الواجهة النيون المطورة (CSS) - عشان تبقى شبه لعبتك
st.markdown("""
    <style>
    .stApp {
        background-color: #010409; /* أسود أعمق */
    }
    .stMarkdown, p, li {
        color: #ffffff !important;
        font-family: 'Arial';
        font-size: 18px; /* تكبير الخط العام */
    }
    h1 {
        color: #00f2ff !important; /* عنوان نيون أزرق ومتوهج */
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        font-size: 40px !important; /* تكبير العنوان */
    }
    .bot-text {
        color: #00f2ff; /* نص الروبوت نيون أزرق */
        font-weight: bold;
        padding: 20px; /* تكبير الحشو */
        border-right: 6px solid #00f2ff; /* خطوط نيون متوهجة */
        background-color: #091a2a;
        border-radius: 15px;
        margin-bottom: 15px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 0 15px #00f2ff; /* تأثير التوهج */
        font-size: 20px; /* تكبير خط الرد */
    }
    .user-text {
        color: #ffffff;
        font-weight: bold;
        padding: 15px;
        direction: rtl;
        text-align: right;
        border-bottom: 2px solid #30363d;
        margin-bottom: 15px;
        font-size: 18px;
    }
    /* جعل شريط البحث نيون وفي المنتصف */
    .stChatInput {
        direction: rtl;
        border-color: #00f2ff !important;
        box-shadow: 0 0 10px #00f2ff;
    }
    /* تكبير حجم الرسم البياني */
    .vega-embed {
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات التعليمية المطورة (مع إجابات سريعة وواضحة)
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة هي: مجموعات بيانات ضخمة جداً ومعقدة، تعجز الأنظمة التقليدية عن معالجتها أو تحليلها في وقت قصير.",
    "خصائص": "📌 الخصائص الأساسية (3Vs):\n\n1. Volume (الحجم): الكميات المهولة من البيانات.\n2. Velocity (السرعة): سرعة توليد وتدفق البيانات.\n3. Variety (التنوع): اختلاف أنواع البيانات (نصوص، صور، فيديوهات).",
    "خطوات": "👣 خطوات تحليل البيانات الضخمة:\n1. الجمع والفرز.\n2. التخزين والمعالجة.\n3. التحليل والاستنتاج.\n4. اتخاذ القرار.",
    "أهمية": "🌟 الأهمية: تعتبر المحرك الأساسي للعالم الرقمي؛ فهي تساعد في تحويل المعلومات الخام إلى قرارات ذكية.",
    "الطب": "🏥 الرعاية الصحية: تُستخدم في توقع الأوبئة، التشخيص الدقيق للأمراض، وتطوير أدوية جديدة.",
    "النقل": "🚗 النقل والمدن الذكية: تنظيم المرور، تقليل الحوادث، وتحسين مواعيد النقل العام."
}

# 4. واجهة العرض الرئيسية
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)
st.write("أهلاً بك! أنا وكيلك الذكي، جاهز للإجابة على جميع أسئلتك حول عالم البيانات الضخمة المثير. تفضل، اسألني!")

# حفظ حالة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-text">👤 أنت: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-text">🤖 الوكيل الذكي: {message["content"]}</div>', unsafe_allow_html=True)
        # عرض الرسم البياني إذا كان موجوداً
        if "chart_data" in message:
            if message["chart_type"] == "bar":
                st.bar_chart(message["chart_data"], use_container_width=True)
            elif message["chart_type"] == "area":
                st.area_chart(message["chart_data"], use_container_width=True)

# 5. منطقة الإدخال (السيرش المطور)
query = st.chat_input("اكتب سؤالك هنا عن البيانات الضخمة أو اطلب رسم بياني... 🤖📊")

if query:
    # عرض سؤال المستخدم وحفظه
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})

    response = None
    q_lower = query.lower()
    msg_data = {"role": "assistant"}

    # بيانات الرسم البياني (نمو البيانات)
    chart_df = pd.DataFrame({
        'السنة': ['2010', '2015', '2020', '2025'],
        'حجم البيانات (بالزيتابايت)': [2, 15, 45, 175]
    }).set_index('السنة')

    # نظام البحث الذكي الجديد
    if "رسم" in q_lower or "بيان" in q_lower or "أشكال" in q_lower:
        response = "📊 إليك مخطط عمودي يوضح الانفجار الهائل في حجم البيانات عالمياً (الزيتابايت):"
        msg_data["content"] = response
        msg_data["chart_data"] = chart_df
        msg_data["chart_type"] = "bar" # النوع الافتراضي هو عمودي
    elif "غير" in q_lower or "شكل تاني" in q_lower:
        response = "✅ حسناً، إليك نفس البيانات ولكن في مخطط مساحي (Area) نيون يوضح التضخم السريع للبيانات:"
        msg_data["content"] = response
        msg_data["chart_data"] = chart_df
        msg_data["chart_type"] = "area" # النوع البديل هو مخطط مساحي
    elif "تعريف" in q_lower or "بيانات" in q_lower:
        response = knowledge_base["تعريف"]
        msg_data["content"] = response
    elif "خصائص" in q_lower or "مميزات" in q_lower:
        response = knowledge_base["خصائص"]
        msg_data["content"] = response
    elif "خطوات" in q_lower or "التحليل" in q_lower:
        response = knowledge_base["خطوات"]
        msg_data["content"] = response
    else:
        # البحث في بقية الكلمات المفتاحية
        keywords = ["أهمية", "اهميه", "الطب", "النقل"]
        for key in keywords:
            if key in q_lower:
                response = knowledge_base[key.replace("اهميه", "أهمية")]
                msg_data["content"] = response
                break

    if not response:
        response = "عذراً، لم أفهم سؤالك جيداً. جرب أن تسأل عن (تعريف، خصائص، أهمية، خطوات التحليل) أو اطلب رسم بياني."
        msg_data["content"] = response

    # عرض رد الروبوت وحفظه
    st.markdown(f'<div class="bot-text">🤖 الوكيل الذكي: {response}</div>', unsafe_allow_html=True)
    
    # عرض الرسم البياني فوراً في حالة الطلب
    if "chart_data" in msg_data:
        if msg_data["chart_type"] == "bar":
            st.bar_chart(msg_data["chart_data"], use_container_width=True)
        elif msg_data["chart_type"] == "area":
            st.area_chart(msg_data["chart_data"], use_container_width=True)

    st.session_state.messages.append(msg_data)
