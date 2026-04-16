import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم الواجهة النيون المطورة (CSS)
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
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات التعليمية الشاملة
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة هي: مجموعات بيانات ضخمة جداً ومعقدة، تعجز الأنظمة التقليدية عن معالجتها.",
    "خصائص": "📌 الخصائص الأساسية (3Vs):\n\n1. Volume (الحجم)\n2. Velocity (السرعة)\n3. Variety (التنوع).",
    "خطوات": "👣 خطوات التحليل: 1. الجمع، 2. التخزين، 3. المعالجة، 4. الاستنتاج.",
    "أهمية": "🌟 الأهمية: تساعد في تحويل المعلومات الخام إلى قرارات ذكية وتوقعات مستقبلية.",
    "الطب": "🏥 الرعاية الصحية: تُستخدم في توقع الأوبئة والتشخيص الدقيق للأمراض.",
    "النقل": "🚗 النقل: تحسين حركة المرور وإدارة أنظمة النقل الذكي.",
    "وظائف": "👨‍💻 الوظائف: محلل بيانات، مهندس بيانات ضخمة، أو خبير ذكاء اصطناعي.",
    "مصادر": "🌐 المصادر: السوشيال ميديا، سجلات GPS، والمستشعرات الذكية.",
    "فرق": "⚖️ الفرق: البيانات العادية منظمة وسهلة، أما الضخمة فهي عشوائية وتحتاج تقنيات خاصة.",
    "خطر": "🛡️ الأمان: يجب حماية البيانات بالتشفير واتباع قوانين المواطنة الرقمية."
}

# 4. الواجهة الرئيسية
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

# إضافة زرار العودة في الجنب
st.sidebar.title("🎮 التحكم")
genially_link = "https://view.genially.com/your-link" # ضعي رابط لعبتك هنا
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

# حفظ وعرض الرسائل
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    div_class = "user-text" if message["role"] == "user" else "bot-text"
    icon = "👤 أنت" if message["role"] == "user" else "🤖 الوكيل"
    st.markdown(f'<div class="{div_class}">{icon}: {message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        st.bar_chart(message["chart"])

# 5. نظام البحث والرد
query = st.chat_input("اكتب سؤالك هنا... 🤖")

if query:
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})
    
    response = None
    q_lower = query.lower()
    
    # الرد على الرسم البياني
    if any(word in q_lower for word in ["رسم", "بيان", "شكل"]):
        response = "📊 إليك رسم بياني يوضح نمو البيانات عالمياً:"
        chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'حجم البيانات': [2, 45, 175]}).set_index('السنة')
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
        st.bar_chart(chart_data)
        st.session_state.messages.append({"role": "assistant", "content": response, "chart": chart_data})
    else:
        # البحث في قاعدة البيانات
        for key in knowledge_base:
            if key in q_lower:
                response = knowledge_base[key]
                break
        
        if not response:
            response = "عذراً، اسألني عن (تعريف، خصائص، وظائف، مصادر، أهمية) أو اطلب رسم بياني."
            
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
