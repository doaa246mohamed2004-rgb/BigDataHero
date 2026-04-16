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

# 3. قاعدة البيانات والكلمات المفتاحية
knowledge_base = {
    "تعريف": "💡 البيانات الضخمة هي: مجموعات بيانات ضخمة جداً ومعقدة، البرامج العادية مش بتقدر تتعامل معاها.",
    "خصائص": "📌 الخصائص الأساسية (3Vs): الحجم، السرعة، والتنوع.",
    "أهمية": "🌟 الأهمية: بتساعدنا ناخد قرارات ذكية في الطب والتجارة والتعليم.",
    "وظائف": "👨‍💻 الوظائف: محلل بيانات، مهندس بيانات، أو خبير ذكاء اصطناعي.",
    "مصادر": "🌐 المصادر: السوشيال ميديا، الـ GPS، والساعات الذكية."
}

keywords = {
    "تعريف": ["تعريف", "يعني ايه", "ماهي", "ايه هي"],
    "خصائص": ["خصائص", "مميزات", "v3", "صفاتها"],
    "أهمية": ["أهمية", "اهميه", "فائدة", "لازمتها"],
    "وظائف": ["وظيفة", "وظائف", "شغل", "أشتغل"],
    "مصادر": ["مصدر", "بتيجي منين", "منين"]
}

# 4. الواجهة والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)
st.sidebar.title("🎮 التحكم")
genially_link = "https://view.genially.com/69c2cab192730eedd4af164e"
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة بأمان (بدون KeyError)
for message in st.session_state.messages:
    role_class = "user-text" if message["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        # استخدام get لتجنب الخطأ لو الـ type مش موجود
        if message.get("type") == "area": st.area_chart(message["chart"])
        else: st.bar_chart(message["chart"])

# 5. استقبال الأسئلة ونظام الرد
query = st.chat_input("اسألني أي حاجة أو اطلب رسم بياني... 🤖")

if query:
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})
    q_lower = query.lower()
    
    response = None
    msg_data = {"role": "assistant"}
    chart_df = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')

    # أولاً: التأكد لو الطالب عاوز رسم بياني
    if any(word in q_lower for word in ["رسم بياني", "شكل بياني", "مخطط"]):
        response = "📊 ده رسم بياني بيوضح انفجار حجم البيانات عالمياً:"
        msg_data["chart"] = chart_df
        msg_data["type"] = "bar"
    elif "غير" in q_lower or "شكل تاني" in q_lower:
        response = "✅ غيرت لك الشكل! ده مخطط مساحي نيون:"
        msg_data["chart"] = chart_df
        msg_data["type"] = "area"
    else:
        # ثانياً: البحث في المعلومات
        for key, words in keywords.items():
            if any(word in q_lower for word in words):
                response = knowledge_base[key]
                break
    
    if not response:
        response = "معلش مش فاهمك، اسألني عن (تعريف، خصائص، وظائف) أو اطلب رسم بياني!"

    msg_data["content"] = response
    st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
    
    # عرض الرسم فوراً لو موجود
    if "chart" in msg_data:
        if msg_data["type"] == "area": st.area_chart(msg_data["chart"])
        else: st.bar_chart(msg_data["chart"])
        
    st.session_state.messages.append(msg_data)
