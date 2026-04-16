import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="Big Data Hero 🤖", layout="centered")

# 2. تصميم الواجهة (CSS) لتشبه شكل تطبيقك النيون
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
    }
    .stMarkdown, p, h1, h2, h3, li {
        color: #ffffff !important;
        font-family: 'Arial';
    }
    .bot-text {
        color: #00f2ff;
        font-weight: bold;
        padding: 15px;
        border-right: 4px solid #00f2ff;
        background-color: #161b22;
        border-radius: 10px;
        margin-bottom: 10px;
        direction: rtl;
        text-align: right;
    }
    .user-text {
        color: #ffffff;
        font-weight: bold;
        padding: 10px;
        direction: rtl;
        text-align: right;
        border-bottom: 1px solid #30363d;
        margin-bottom: 10px;
    }
    .stChatInput {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات التعليمية المطورة
knowledge_base = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات كبيرة جداً ومعقدة لدرجة إن البرامج العادية مش بتقدر تتعامل معاها.",
    "بيانات": "البيانات الضخمة هي مجموعات بيانات كبيرة جداً ومعقدة لدرجة إن البرامج العادية مش بتقدر تتعامل معاها.",
    "خصائص": "📌 خصائص البيانات الضخمة (3Vs):\n\n1. الحجم (Volume): كمية البيانات المهولة.\n2. السرعة (Velocity): سرعة توليد وتدفق البيانات.\n3. التنوع (Variety): اختلاف أنواع البيانات (صور، نصوص، فيديوهات).",
    "أهمية": "🌟 أهمية البيانات الضخمة:\nتعتبر المحرك الأساسي للعالم الرقمي؛ فهي تساعد في تحويل المعلومات الخام إلى قرارات ذكية، وتوقع المستقبل، وتحسين جودة الحياة في مجالات الطب والأمن والتعليم.",
    "الطب": "🏥 الرعاية الصحية: تُستخدم في توقع الأوبئة، التشخيص الدقيق للأمراض، وتطوير أدوية جديدة بسرعة.",
    "النقل": "🚗 النقل والمدن الذكية: تنظيم المرور، تقليل الحوادث، وتحسين مواعيد النقل العام.",
    "التجارة": "🛍️ التجارة والتسويق: أنظمة التوصية الذكية وتحليل سلوك المستهلك لتقديم عروض مخصصة.",
    "الأمن": "🛡️ الأمن الرقمي: كشف سرقة البطاقات البنكية وحماية الأنظمة من الاختراق السيبراني.",
    "التعليم": "📚 التعليم: توفير تعلم شخصي لكل طالب وتحسين المناهج بناءً على مستوى الاستيعاب.",
    "خطوات": "خطوات التحليل هي: 1. جمع البيانات، 2. فرز البيانات، 3. المعالجة، 4. الاستنتاج."
}

options_menu = "📌 الخيارات المتاحة: (تعريف، خصائص، أهمية، الطب، النقل، التجارة، الأمن، التعليم، خطوات التحليل، أو اطلب رسم بياني)"

# 4. واجهة العرض الرئيسية
st.title("🤖 الوكيل الذكي - Big Data Hero")
st.write("مرحبا انا وكيلك الذكى اتفضل اسالنى اى سؤال")

# حفظ حالة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    class_name = "user-text" if message["role"] == "user" else "bot-text"
    role_icon = "👤 أنت" if message["role"] == "user" else "🤖 الوكيل الذكي"
    st.markdown(f'<div class="{class_name}">{role_icon}: {message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        st.bar_chart(message["chart"])

# 5. منطقة الإدخال (السيرش)
query = st.chat_input("اكتب سؤالك هنا... 🤖")

if query:
    # عرض سؤال المستخدم وحفظه
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})

    response = None
    q_lower = query.lower()
    chart_to_show = None

    # نظام البحث الذكي
    if "رسم" in q_lower or "بيان" in q_lower or "شكل" in q_lower:
        response = "📊 إليك رسم بياني يوضح الارتفاع الجنوني في حجم البيانات عالمياً (بالزيتابايت):"
        chart_to_show = pd.DataFrame({
            'السنة': ['2010', '2015', '2020', '2025'],
            'حجم البيانات': [2, 15, 45, 175]
        }).set_index('السنة')
    elif "خصائص" in q_lower or "مميزات" in q_lower:
        response = knowledge_base["خصائص"]
    elif "أهمية" in q_lower or "اهميه" in q_lower:
        response = knowledge_base["أهمية"]
    else:
        keywords = ["تعريف", "بيانات", "الطب", "النقل", "التجارة", "الأمن", "التعليم", "خطوات"]
        for key in keywords:
            if key in q_lower:
                response = knowledge_base[key]
                break

    if not response:
        response = f"عذراً، لم أفهم سؤالك جيداً. {options_menu}"

    # عرض رد الروبوت وحفظه
    st.markdown(f'<div class="bot-text">🤖 الوكيل الذكي: {response}</div>', unsafe_allow_html=True)

    msg_data = {"role": "assistant", "content": response}
    if chart_to_show is not None:
        st.bar_chart(chart_to_show)
        msg_data["chart"] = chart_data = chart_to_show

    st.session_state.messages.append(msg_data)