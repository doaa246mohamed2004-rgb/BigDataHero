import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Big Data Hero 🤖", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- ضع مفتاح الـ Token الخاص بك هنا من Hugging Face ---
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"
client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

# 2. تنسيق الـ CSS المطور (كودك القديم بالكامل)
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
    
    .sidebar-title { color: #FFD700 !important; text-align: center; font-size: 24px !important; font-weight: bold; text-shadow: 0 0 10px rgba(255, 215, 0, 0.6); }
    h1 { color: #00f2ff !important; text-shadow: 0 0 15px #00f2ff; text-align: center; border-bottom: 2px solid #1f6feb; padding-bottom: 10px; font-family: 'Cairo', sans-serif !important; }

    .bot-text { background-color: #0d1a26; border-right: 5px solid #00f2ff; padding: 20px; border-radius: 15px; margin-bottom: 15px; }
    .user-text { background-color: #161b22; border-left: 5px solid #58a6ff; padding: 15px; border-radius: 12px; margin-bottom: 15px; }

    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(45deg, #1f6feb, #388bfd); color: white; font-weight: bold; }
    .game-link { display: block; width: 100%; text-align: center; background: linear-gradient(45deg, #238636, #2ea043); color: white !important; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px; }
    .step-box { border: 2px solid #00f2ff; padding: 15px; border-radius: 12px; margin: 10px 0; background: rgba(0, 242, 255, 0.1); color: #00f2ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة المعرفة (المعلومات التي وضعتِها يدوياً)
kb = {
    "تعريف": "البيانات الضخمة (Big Data) هي 'منجم الذهب' الرقمي؛ هي كميات هائلة من المعلومات اللي بتنتج كل ثانية من موبايلاتنا وحياتنا! 🔍✨",
    "الفرق": "🌟 **مقارنة الأبطال:**\n1. **البيانات العادية:** زي جدول درجاتك، حجمها صغير.\n2. **البيانات الضخمة:** حجمها بالـ 'زيتابايت' ومحتاجة سيرفرات قوية جداً. 🔥",
    "ذكاء": "🤝 **الثنائي الخارق:**\nالبيانات الضخمة هي 'البنزين' والذكاء الاصطناعي هو 'المحرك'. كل ما تدي بيانات أكتر، الـ AI بيبقى أذكى! 🧠🤖",
    "تغيير": "🚀 **كيف غيرت عالمنا؟**\n- **الطب الذكي:** تشخيص الأمراض.\n- **أمانك المالي:** حماية كروت البنك.\n- **مدن المستقبل:** تقليل الزحمة. 🚦",
    "خصائص": "✨ **الخصائص الـ 5 (5Vs):**\n1. Volume (الحجم) | 2. Velocity (السرعة) | 3. Variety (التنوع) | 4. Veracity (الموثوقية) | 5. Value (القيمة) 💎",
    "ترتيب": """⛓️ **مخطط رحلة البيانات الضخمة:**
<div class="step-box">1️⃣ التجميع (Collection) 📥</div>
<div class="step-box">2️⃣ التخزين (Storage) 🗄️</div>
<div class="step-box">3️⃣ المعالجة (Processing) 🧼</div>
<div class="step-box">4️⃣ التحليل (Analysis) 🧠</div>
<div class="step-box">5️⃣ اتخاذ القرار (Action) ✅</div>"""
}

# 4. إدارة حالة الجلسة
if "messages" not in st.session_state: 
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك يا بطل! أنا وكيلك الذكي، اسألني عن أي شيء في عالم البيانات الضخمة. 🤖✨"}]
if "view" not in st.session_state: 
    st.session_state.view = "chat"

# 5. الواجهة الجانبية (كل أزرارك القديمة)
with st.sidebar:
    st.markdown('<p class="sidebar-title">📍 المحطات التعليمية</p>', unsafe_allow_html=True)
    if st.button("🔍 1. البيانات الضخمه"): st.session_state.q_auto = "تعريف"
    if st.button("⚖️ 2. العادية vs الضخمة"): st.session_state.q_auto = "الفرق"
    if st.button("⚡ 3. الخصائص الـ 5"): st.session_state.q_auto = "خصائص"
    if st.button("🤖 4. الذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"
    if st.button("🚀 5. فائدتها"): st.session_state.q_auto = "تغيير"
    if st.button("📈 6. رسم بياني"): st.session_state.q_auto = "رسم"
    st.markdown("---")
    if st.button("⛓️ رحلة البيانات"): st.session_state.q_auto = "ترتيب"
    if st.button("📝 اختبار الأبطال"): st.session_state.view = "quiz"; st.rerun()
    if st.button("🔄 محادثة جديدة"): st.session_state.messages = [{"role": "assistant", "content": "أهلاً بك مجدداً! كيف يمكنني مساعدتك؟"}]; st.session_state.view = "chat"; st.rerun()
    st.markdown('<a href="https://view.genially.com/..." target="_blank" class="game-link">🎮 العودة للمغامرة</a>', unsafe_allow_html=True)

# 6. منطق الرد الذكي (Hybrid AI)
def get_ai_response(prompt):
    q_low = prompt.lower()
    # أولاً: جرب الرد من قاعدة بياناتك (أسرع وأدق لمشروعك)
    for key in kb:
        if key in q_low: return kb[key]
    if "رسم" in q_low: return "إليك الرسم البياني لتطور حجم البيانات عالمياً: 📊📈"

    # ثانياً: إذا لم يجد الإجابة، يسأل Hugging Face (بديل شات جي بي تي)
    try:
        formatted_prompt = f"<|system|>\nأنت مساعد تعليمي ذكي للأطفال اسمه Big Data Hero. تشرح بأسلوب بسيط ومشجع بالعربي وتستخدم الرموز التعبيرية.</s>\n<|user|>\n{prompt}</s>\n<|assistant|>\n"
        response = ""
        for message in client.chat_completion(
            messages=[{"role": "user", "content": formatted_prompt}],
            max_tokens=250,
            stream=True
        ):
            response += message.choices[0].delta.content or ""
        return response
    except:
        return "سؤال ذكي جداً! البيانات الضخمة مذهلة. هل تريد استكشاف المحطات التعليمية؟ 🤖"

# العرض الرئيسي
if st.session_state.view == "quiz":
    st.markdown("<h1>📝 اختبار التحدي</h1>", unsafe_allow_html=True)
    q1 = st.radio("1️⃣ أي خاصية تعبر عن 'تنوع' البيانات (فيديو، نصوص، صوت)؟", ["Volume", "Variety", "Velocity"])
    q2 = st.radio("2️⃣ من هو 'الوقود' الذي يغذي محرك الذكاء الاصطناعي؟", ["البيانات الضخمة", "الكهرباء فقط"])
    if st.button("إرسال الإجابات"):
        if q1 == "Variety" and q2 == "البيانات الضخمة":
            st.balloons(); st.success("عبقري! إجاباتك كاملة وصحيحة 🎯")
        else: st.error("راجع المحطات التعليمية وجرب مرة أخرى!")
    if st.button("العودة للدردشة"): st.session_state.view = "chat"; st.rerun()
else:
    st.markdown("<h1>🤖 الوكيل التعليمي الذكي</h1>", unsafe_allow_html=True)
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)
        if "📊" in m["content"]:
            chart_data = pd.DataFrame({'السنة': [2010, 2015, 2020, 2025], 'حجم البيانات (زيتابايت)': [2, 12, 64, 175]})
            st.area_chart(chart_data.set_index('السنة'))

    u_input = st.chat_input("اسألني عن أي شيء...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.spinner("جاري التفكير..."):
            ans = get_ai_response(query)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
