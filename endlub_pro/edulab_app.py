import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم الواجهة النيون المطورة (CSS) - متناسب تماماً مع ثيم لعبتك
st.markdown("""
    <style>
    .stApp {
        background-color: #010409; 
    }
    .stMarkdown, p, li {
        color: #ffffff !important;
        font-family: 'Arial';
        font-size: 19px;
    }
    h1 {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        font-size: 45px !important;
        text-align: center;
    }
    .bot-text {
        color: #00f2ff;
        font-weight: bold;
        padding: 20px;
        border-right: 6px solid #00f2ff;
        background-color: #091a2a;
        border-radius: 15px;
        margin-bottom: 15px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 0 15px #00f2ff;
    }
    .user-text {
        color: #ffffff;
        font-weight: bold;
        padding: 15px;
        direction: rtl;
        text-align: right;
        border-bottom: 2px solid #30363d;
        margin-bottom: 15px;
    }
    .stChatInput {
        direction: rtl;
        border-color: #00f2ff !important;
    }
    /* تحسين شكل الأزرار في الجنب */
    .stButton>button {
        width: 100%;
        background-color: #00f2ff;
        color: black;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات التعليمية الشاملة (القديم + الجديد)
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة هي: مجموعات بيانات ضخمة جداً ومعقدة، تعجز الأنظمة التقليدية عن معالجتها أو تحليلها في وقت قصير.",
    "خصائص": "📌 الخصائص الأساسية (3Vs):\n\n1. Volume (الحجم): الكميات المهولة من البيانات.\n2. Velocity (السرعة): سرعة توليد وتدفق البيانات.\n3. Variety (التنوع): اختلاف أنواع البيانات (نصوص، صور، فيديوهات).",
    "خطوات": "👣 خطوات تحليل البيانات الضخمة:\n1. الجمع والفرز.\n2. التخزين والمعالجة.\n3. التحليل والاستنتاج.\n4. اتخاذ القرار المستند إلى البيانات.",
    "أهمية": "🌟 الأهمية: تعتبر المحرك الأساسي للعالم الرقمي؛ فهي تساعد في تحويل المعلومات الخام إلى قرارات ذكية وتوقعات مستقبلية دقيقة.",
    "الطب": "🏥 الرعاية الصحية: تُستخدم في توقع الأوبئة قبل انتشارها، التشخيص الدقيق للأمراض، وتطوير أدوية مخصصة بناءً على الجينات.",
    "النقل": "🚗 النقل والمدن الذكية: تحسين حركة المرور، تقليل الحوادث، وإدارة أنظمة النقل الذاتي القيادة.",
    "وظائف": "👨‍💻 المستقبل الوظيفي:\nيمكنك العمل كـ (محلل بيانات)، (مهندس بيانات ضخمة)، أو (خبير ذكاء اصطناعي). الوظائف المطلوبة جداً وبرواتب مجزية!",
    "مصادر": "🌐 من أين تأتي؟\nمن السوشيال ميديا، سجلات GPS، مستشعرات المصانع، الساعات الذكية، وحتى عمليات الشراء عبر الإنترنت.",
    "فرق": "⚖️ الفرق بينها وبين البيانات العادية:\nالبيانات العادية منظمة وسهلة التخزين في جداول بسيطة، أما الضخمة فهي عشوائية (صوت، فيديو) وتحتاج تقنيات مثل Hadoop لمعالجتها.",
    "خطر": "🛡️ الأمان الرقمي:\nالبيانات الضخمة تحتاج حماية فائقة؛ لأن تسريبها يهدد الخصوصية. نستخدم التشفير والمواطنة الرقمية لحمايتها من الاختراق."
}

# 4. واجهة العرض الرئيسية
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)
st.sidebar.title("🎮 التحكم بالوكيل")
st.sidebar.info("أنا وكيل ذكي صممته دعاء لمساعدتك في فهم البيانات الضخمة داخل رحلتك التعليمية.")

# إضافة زرار العودة للعبة في الجنب (تغيير الرابط برابط لعبتك)
st.sidebar.markdown("---")
genially_link = "حطي_رابط_جينالي_هنا"
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

# حفظ حالة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-text">👤 أنت: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-text">🤖 الوكيل الذكي: {message["content"]}</div>', unsafe_allow_html=True)
        if "chart_data" in message:
            if message["chart_type"] == "bar":
                st.bar_chart(message["chart_data"])
            elif message["chart_type"] == "area":
                st.area_chart(message["chart_data"])

# 5. منطقة الإدخال (السيرش)
query = st.chat_input("اكتب سؤالك هنا (مثلاً: ما هي الخصائص؟ أو اطلب رسم بياني)... 🤖")

if query:
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})

    response = None
    q_lower = query.lower()
    msg_data = {"role": "assistant"}

    # بيانات الرسم البياني
    chart_df = pd.DataFrame({
        'السنة': ['2010', '2015', '2020', '2025'],
        'حجم البيانات (Zettabytes)': [2, 15, 45, 175]
    }).set_index('السنة')

    # نظام الرد الذكي المحدث
    if "رسم" in q_lower or "بيان" in q_lower or "أشكال" in q_lower:
        response = "📊 إليك مخطط عمودي يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت):"
        msg_data["chart_data"] = chart_df
        msg_data["chart_type"] = "bar"
    elif "غير" in q_lower or "شكل تاني" in q_lower or "مساحي" in q_lower:
        response = "✅ تم تغيير الشكل! إليك المخطط المساحي النيون الذي يوضح تضاعف البيانات:"
        msg_data["chart_data"] = chart_df
        msg_data["chart_type"] = "area"
    else:
        # البحث في قاعدة البيانات
        keywords = {
            "تعريف": ["تعريف", "معنى", "ماهي"],
            "خصائص": ["خصائص", "مميزات", "v3"],
            "خطوات": ["خطوات", "مراحل", "كيف"],
            "أهمية": ["أهمية", "اهميه", "فائدة"],
            "الطب": ["طب", "صحة", "مستشفى"],
            "النقل": ["نقل", "مرور", "سيارات"],
            "وظائف": ["وظيفة", "وظائف", "شغل", "أعمل"],
            "مصادر": ["
