import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم الواجهة النيون (CSS)
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
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات (موسعة لتشمل كل طرق الكلام)
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة (Big Data) هي: كميات هائلة من المعلومات اللي بتيجي بسرعة وتنوع كبير، والكمبيوترات العادية مش بتقدر تعالجها لوحدها.",
    "خصائص": "📌 الخصائص الأساسية (3Vs):\n1. الحجم (Volume)\n2. السرعة (Velocity)\n3. التنوع (Variety).",
    "أهمية": "🌟 الأهمية: بتساعدنا نتوقع اللي هيحصل في المستقبل، ونطور الطب، وننظم حركة المرور في المدن الذكية.",
    "وظائف": "👨‍💻 وظائف المستقبل: محلل بيانات، مهندس بيانات ضخمة، أو خبير ذكاء اصطناعي. دي من أعلى الوظائف طلباً!",
    "مصادر": "🌐 بتيجي منين؟ من السوشيال ميديا، الـ GPS، الساعات الذكية، وحتى عمليات الشراء اللي بنعملها أونلاين.",
    "فرق": "⚖️ الفرق: البيانات العادية بسيطة ومنظمة (زي جداول الإكسيل)، أما الضخمة فهي جبارة وعشوائية وتحتاج سيرفرات قوية جداً."
}

# كلمات البحث (أضفت لك كل الاحتمالات اللي ممكن الطالب يكتبها)
search_map = {
    "تعريف": ["تعريف", "ماهي", "ايه هي", "البيانات الضخمة", "يعني ايه", "داتا", "data"],
    "خصائص": ["خصائص", "مميزات", "صفات", "v3", "بتتكون"],
    "أهمية": ["أهمية", "اهميه", "فائدة", "لازمتها", "بنستفيد"],
    "وظائف": ["وظيفة", "وظائف", "شغل", "أشتغل", "مستقبل"],
    "مصادر": ["مصدر", "مصادر", "بتيجي منين", "منين"],
    "فرق": ["فرق", "مقارنة", "عادية", "تفرق"]
}

# 4. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)
st.sidebar.title("🎮 التحكم")
genially_link = "https://view.genially.com/69c2cab192730eedd4af164e"
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة بأمان
for message in st.session_state.messages:
    role_class = "user-text" if message["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        st.bar_chart(message["chart"])

# 5. منطقة السؤال
query = st.chat_input("اسألني عن البيانات الضخمة أو اطلب رسم بياني... 🤖")

if query:
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})
    q_lower = query.lower()
    
    response = None
    msg_data = {"role": "assistant"}
    chart_df = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم (زيتابايت)': [2, 45, 175]}).set_index('السنة')

    # أولاً: التأكد لو الطالب عاوز رسم بياني (بمجرد وجود كلمة رسم أو شكل)
    if any(word in q_lower for word in ["رسم", "شكل", "مخطط", "graph", "chart"]):
        response = "📊 إليك رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت):"
        msg_data["chart"] = chart_df
    else:
        # ثانياً: البحث في المعلومات
        for category, keywords in search_map.items():
            if any(word in q_lower for word in keywords):
                response = knowledge_base[category]
                break
    
    if not response:
        response = "عذراً يا بطل، حاول تسألني بشكل أوضح (مثلاً: ما هي الخصائص؟ أو اطلب رسم بياني)."

    msg_data["content"] = response
    st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
    
    if "chart" in msg_data:
        st.bar_chart(msg_data["chart"])
        
    st.session_state.messages.append(msg_data)
