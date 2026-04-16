import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="Big Data Hero 🤖📊", layout="centered")

# 2. تصميم نيون احترافي (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    .stMarkdown, p, li { color: #ffffff !important; font-family: 'Arial'; font-size: 18px; line-height: 1.6; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; font-size: 40px !important; text-align: center; }
    .bot-text {
        color: #00f2ff; font-weight: bold; padding: 20px; border-right: 6px solid #00f2ff;
        background-color: #091a2a; border-radius: 15px; margin-bottom: 15px;
        direction: rtl; text-align: right; box-shadow: 0 0 15px #00f2ff;
    }
    .user-text {
        color: #ffffff; font-weight: bold; padding: 15px; direction: rtl;
        text-align: right; border-bottom: 2px solid #30363d; margin-bottom: 15px;
    }
    .stChatInput { direction: rtl; }
    /* تنسيق الجداول */
    table { width: 100%; border-collapse: collapse; color: white; background: #0d1117; }
    th, td { border: 1px solid #30363d; padding: 10px; text-align: center; }
    th { background-color: #00f2ff; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات التعليمية الشاملة
kb = {
    "تعريف": "🔍 **ما هي البيانات الضخمة؟**\n\nهي مجموعات بيانات ضخمة جداً ومعقدة، تتولد بسرعة هائلة من مصادر مختلفة (زي السوشيال ميديا والحساسات). ضخمة لدرجة إن الأدوات التقليدية مش بتقدر تخزنها أو تعالجها بسهولة.",
    "خصائص": "⚡ **خصائص الـ 5V's:**\n\n1. **الحجم (Volume):** كميات بالبيتابايت.\n2. **السرعة (Velocity):** تدفق فوري للبيانات.\n3. **التنوع (Variety):** نصوص، صور، وفيديوهات.\n4. **الموثوقية (Veracity):** دقة وجودة البيانات.\n5. **القيمة (Value):** الفائدة اللي بنطلع بيها بعد التحليل.",
    "فرق": """⚖️ **الفرق بين البيانات العادية والضخمة:**

| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | صغيرة (جيجابايت) | ضخمة (بيتابايت فأكثر) |
| **التخزين** | خادم واحد | موزعة على عدة خوادم |
| **النوع** | مهيكلة (جداول) | غير مهيكلة (فيديو، صوت) |
| **الأدوات** | Excel / SQL | Hadoop / Spark |""",
    "أهمية": "🌟 **ليه هي مهمة؟**\n\nبساعدنا في اتخاذ **قرارات ذكية** بناءً على حقائق، و**التنبؤ بالمستقبل** (زي الأزمات أو الطقس)، و**تحسين الكفاءة** وتقليل التكاليف.",
    "استخدامات": "🌍 **استخدامات في حياتنا:**\n\n- **الرعاية الصحية:** توقع الأوبئة.\n- **التجارة:** ترشيح المنتجات (أمازون ونون).\n- **المدن الذكية:** تنظيم المرور.\n- **الترفيه:** اقتراحات يوتيوب ونتفليكس.",
    "تعليم": "🎓 **البيانات الضخمة في التعليم:**\n\n1. **التعلم الشخصي:** محتوى يناسب قدرات كل طالب.\n2. **تحسين النتائج:** مساعدة الطلاب المعرضين للرسوب مبكراً.\n3. **تطوير المناهج:** اكتشاف الأجزاء الصعبة وتعديلها.",
    "وظائف": "💼 **وظائف المجال:**\n\n- محلل بيانات (Data Analyst).\n- عالم بيانات (Data Scientist).\n- مهندس بيانات ضخمة (Big Data Engineer).\n- إخصائي ذكاء أعمال (BI Developer).",
    "تعلم": "🚀 **منصات للتعلم:**\n\n- **Coursera & EdX:** كورسات من Google و MIT.\n- **Udacity:** لشهادات النانو دجري.\n- **Kaggle:** للتطبيق العملي والمنافسة.\n- **Datacamp:** لتعلم Python و R.",
    "استفادة": "💡 **هتستفيد إيه؟**\n\nتطوير تفكيرك التحليلي، التعامل مع أحدث تكنولوجيا في العالم، وفتح فرص عمل عالمية ومشاريع ابتكارية."
}

# خريطة الكلمات المفتاحية (البحث المرن)
search_map = {
    "تعريف": ["تعريف", "يعني ايه", "ماهي", "البيانات الضخمة", "ايه هي"],
    "خصائص": ["خصائص", "مميزات", "v5", "صفات", "عناصر"],
    "فرق": ["فرق", "مقارنة", "تفرق", "عادية", "جدول"],
    "أهمية": ["أهمية", "اهميه", "فائدة", "لازمتها"],
    "استخدامات": ["استخدام", "تطبيقات", "حياتنا", "أمازون", "نتفليكس"],
    "تعليم": ["تعليم", "مدرسة", "طالب", "منهج"],
    "وظائف": ["شغل", "وظيفة", "وظائف", "أشتغل"],
    "تعلم": ["اتعلم", "منصات", "مواقع", "كورس", "دورة"],
    "استفادة": ["استفادة", "هستفيد", "مهارات"]
}

# 4. العنوان الجانبي (Sidebar) - الأزرار التفاعلية
st.sidebar.title("🎮 لوحة التحكم")
genially_link = "https://view.genially.com/69c2cab192730eedd4af164e"
st.sidebar.link_button("🔙 العودة إلى اللعبة", genially_link)

st.sidebar.subheader("📌 الوصول السريع")
if st.sidebar.button("💡 ما هي البيانات الضخمة؟"): st.session_state.btn_query = "تعريف"
if st.sidebar.button("⚖️ الفرق بين أنواع البيانات"): st.session_state.btn_query = "فرق"
if st.sidebar.button("🎓 البيانات في التعليم"): st.session_state.btn_query = "تعليم"
if st.sidebar.button("📊 اطلب رسم بياني"): st.session_state.btn_query = "رسم"

# 5. الواجهة الرئيسية
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    role_class = "user-text" if message["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)
    if "chart" in message:
        st.bar_chart(message["chart"])

# معالجة السؤال (سواء من الشات أو الأزرار)
user_input = st.chat_input("اسألني أي حاجة عن البيانات الضخمة... 🤖")
query = user_input or st.session_state.get('btn_query')
if 'btn_query' in st.session_state: del st.session_state['btn_query']

if query:
    # إضافة سؤال المستخدم
    st.markdown(f'<div class="user-text">👤 أنت: {query}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": query})
    
    q_lower = query.lower()
    response = None
    msg_data = {"role": "assistant"}

    # 1. فحص طلب الرسم البياني
    if any(word in q_lower for word in ["رسم", "شكل", "مخطط", "بياني"]):
        response = "📊 إليك رسم بياني يوضح الانفجار الهائل في حجم البيانات عالمياً (بالزيتابايت):"
        chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        msg_data["chart"] = chart_data
    else:
        # 2. البحث الذكي في قاعدة البيانات
        for category, words in search_map.items():
            if any(word in q_lower for word in words):
                response = kb[category]
                break
    
    if not response:
        response = "معلش يا بطل مش فاهم سؤالك، اسألني عن (التعريف، الخصائص، الوظائف، أو الفرق بين البيانات) وهجاوبك فوراً!"

    # عرض رد الوكيل
    msg_data["content"] = response
    st.markdown(f'<div class="bot-text">🤖 الوكيل: {response}</div>', unsafe_allow_html=True)
    if "chart" in msg_data:
        st.bar_chart(msg_data["chart"])
        
    st.session_state.messages.append(msg_data)
