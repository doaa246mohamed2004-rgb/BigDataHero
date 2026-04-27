import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Big Data Hero 🤖", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- ضع مفتاح الـ Token الخاص بك هنا مباشرة ليعمل الشات ---
# انسخي التوكن من حسابك في Hugging Face وضعيها بين القوسين
HF_TOKEN = "ضع_التوكن_الخاص_بك_هنا_hf_..." 

client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

# 2. تنسيق الـ CSS (كل تنسيقاتك القديمة والألوان)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    .stApp { background: linear-gradient(135deg, #010409 0%, #0d1117 100%) !important; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; }
    [data-testid="stChatInput"] { background-color: #161b22 !important; border-radius: 15px; border: 1px solid #30363d !important; }
    [data-testid="stChatInput"] textarea { color: #ffffff !important; background-color: #0d1117 !important; }
    [data-testid="stChatInput"] textarea::placeholder { color: rgba(255, 255, 255, 0.8) !important; }

    footer {display: none !important;}
    header {visibility: hidden;}

    .stMarkdown, p, li, label, .stSelectbox, .stRadio, div { 
        color: #FFFFFF !important; font-family: 'Cairo', sans-serif !important; font-size: 20px !important; direction: rtl; text-align: right; 
    }
    
    .sidebar-title { color: #FFD700 !important; text-align: center; font-size: 24px !important; font-weight: bold; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 15px #00f2ff; text-align: center; border-bottom: 2px solid #1f6feb; padding-bottom: 10px; }

    .bot-text { background-color: #0d1a26; border-right: 5px solid #00f2ff; padding: 20px; border-radius: 15px; margin-bottom: 15px; }
    .user-text { background-color: #161b22; border-left: 5px solid #58a6ff; padding: 15px; border-radius: 12px; margin-bottom: 15px; }

    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(45deg, #1f6feb, #388bfd); color: white; font-weight: bold; }
    .step-box { border: 2px solid #00f2ff; padding: 15px; border-radius: 12px; margin: 10px 0; background: rgba(0, 242, 255, 0.1); color: #00f2ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة المعرفة (المعلومات اليدوية)
kb = {
    "تعريف": "البيانات الضخمة (Big Data) هي 'منجم الذهب' الرقمي؛ هي كميات هائلة من المعلومات! 🔍✨",
    "الفرق": "🌟 **مقارنة الأبطال:**\n1. **البيانات العادية:** زي جدول درجاتك.\n2. **البيانات الضخمة:** حجمها بالـ 'زيتابايت'. 🔥",
    "ذكاء": "🤝 **الثنائي الخارق:** البيانات الضخمة هي 'البنزين' والذكاء الاصطناعي هو 'المحرك'. 🧠🤖",
    "خصائص": "✨ **الخصائص الـ 5 (5Vs):** Volume, Velocity, Variety, Veracity, Value 💎",
    "ترتيب": """⛓️ **مخطط رحلة البيانات الضخمة:**
<div class="step-box">1️⃣ التجميع | 2️⃣ التخزين | 3️⃣ المعالجة | 4️⃣ التحليل | 5️⃣ القرار ✅</div>"""
}

# 4. إدارة حالة الجلسة
if "messages" not in st.session_state: 
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك يا بطل! أنا وكيلك الذكي، اسألني عن أي شيء. 🤖✨"}]
if "view" not in st.session_state: 
    st.session_state.view = "chat"

# 5. القائمة الجانبية
with st.sidebar:
    st.markdown('<p class="sidebar-title">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    if st.button("🔍 1. البيانات الضخمه"): st.session_state.q_auto = "تعريف"
    if st.button("⚡ 3. الخصائص الـ 5"): st.session_state.q_auto = "خصائص"
    if st.button("⛓️ رحلة البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبار الأبطال"): st.session_state.view = "quiz"; st.rerun()
    if st.button("🔄 محادثة جديدة"): 
        st.session_state.messages = [{"role": "assistant", "content": "أهلاً بك مجدداً!"}]
        st.session_state.view = "chat"; st.rerun()

# 6. دالة الرد الذكي (تتصل بـ Hugging Face)
def get_ai_response(prompt):
    q_low = prompt.lower()
    for key in kb:
        if key in q_low: return kb[key]

    try:
        formatted_prompt = f"<|system|>\nأنت مساعد تعليمي ذكي للأطفال اسمه Big Data Hero. تجيب بالعربي ببساطة.</s>\n<|user|>\n{prompt}</s>\n<|assistant|>\n"
        response = ""
        for message in client.chat_completion(messages=[{"role": "user", "content": formatted_prompt}], max_tokens=200, stream=True):
            response += message.choices[0].delta.content or ""
        return response
    except:
        return "سؤال رائع! هل تريد معرفة المزيد عن عالم البيانات؟ 🤖"

# --- العرض الرئيسي ---
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار التحدي</h1>", unsafe_allow_html=True)
    q1 = st.radio("أي خاصية تعبر عن 'تنوع' البيانات؟", ["Volume", "Variety", "Velocity"])
    if st.button("إرسال الإجابات"):
        if q1 == "Variety": st.balloons(); st.success("ممتاز!")
    if st.button("العودة"): st.session_state.view = "chat"; st.rerun()
else:
    st.markdown("<h1>🤖 الوكيل التعليمي الذكي</h1>", unsafe_allow_html=True)
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اسألني عن أي شيء...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.spinner("جاري التفكير..."):
            ans = get_ai_response(query)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
