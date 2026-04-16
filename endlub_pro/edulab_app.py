import streamlit as st
import pandas as pd
import random

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
    .quiz-box {
        background-color: #161b22; border: 2px solid #00f2ff; padding: 20px;
        border-radius: 15px; margin-top: 10px; direction: rtl;
    }
    .stButton>button { width: 100%; background-color: #00f2ff; color: black; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. قاعدة البيانات المحسنة
kb = {
    "تعريف": "🔍 **ما هي البيانات الضخمة؟**\n\nهي مجموعات بيانات ضخمة جداً ومعقدة، تتولد بسرعة هائلة من مصادر مختلفة. ضخمة لدرجة إن الأدوات التقليدية مش بتقدر تخزنها أو تعالجها بسهولة.",
    "خصائص": "⚡ **خصائص الـ 5V's:**\n\n1. **الحجم (Volume):** كميات هائلة.\n2. **السرعة (Velocity):** تدفق فوري.\n3. **التنوع (Variety):** صور، نصوص، فيديو.\n4. **الموثوقية (Veracity):** دقة البيانات.\n5. **القيمة (Value):** الفائدة المستخرجة.",
    "فرق": """⚖️ **الفرق بين البيانات العادية والضخمة:**
| وجه المقارنة | البيانات العادية | البيانات الضخمة |
| :--- | :--- | :--- |
| **الحجم** | صغيرة (جيجابايت) | ضخمة (بيتابايت) |
| **التخزين** | خادم واحد | موزعة |
| **النوع** | منظمة (جداول) | عشوائية (فيديو/صوت) |""",
    "تعليم": "🎓 **في التعليم:** تساعد في (التعلم الشخصي) لكل طالب، (تحسين النتائج) وتوقع الطلاب المتعثرين، و(تطوير المناهج) بناءً على تفاعل الطلاب.",
    "roadmap": """🗺️ **خارطة طريق تعلم البيانات الضخمة:**
1. **الأساسيات:** تعلم لغة البرمجة **Python** لأنها لغة البيانات الأولى.
2. **قواعد البيانات:** تعلم لغة **SQL** للتعامل مع البيانات المنظمة.
3. **التحليل:** تعلم مكتبات مثل Pandas و NumPy.
4. **أدوات الضخمة:** ابدأ في تعلم **Hadoop** و **Apache Spark**.
5. **الذكاء الاصطناعي:** تعلم كيفية بناء نماذج تنبؤية.""",
}

# نظام الأسئلة (Quiz)
quiz_data = [
    {"q": "أي من الـ 5V's تعبر عن سرعة إنتاج البيانات؟", "a": ["Velocity", "Volume", "Value"], "correct": "Velocity"},
    {"q": "أداة مشهورة لمعالجة البيانات الضخمة:", "a": ["Hadoop", "Excel", "Word"], "correct": "Hadoop"},
    {"q": "البيانات غير المهيكلة تشمل:", "a": ["الفيديوهات والصور", "جداول الإكسيل", "البيانات المنظمة"], "correct": "الفيديوهات والصور"}
]

# 4. العنوان والتحكم
st.markdown("<h1>🤖 الوكيل الذكي - Big Data Hero</h1>", unsafe_allow_html=True)

# معلومة "هل تعلم" عند البداية
if "first_run" not in st.session_state:
    st.info("💡 **هل تعلم؟** أن 90% من بيانات العالم تم إنتاجها في آخر سنتين فقط! هذا هو سحر البيانات الضخمة.")
    st.session_state.first_run = True

st.sidebar.title("🎮 لوحة التحكم")
st.sidebar.link_button("🔙 العودة إلى اللعبة", "https://view.genially.com/69c2cab192730eedd4af164e")

st.sidebar.subheader("📌 اختصارات سريعة")
if st.sidebar.button("💡 ما هي البيانات الضخمة؟"): st.session_state.query = "تعريف"
if st.sidebar.button("⚖️ المقارنة"): st.session_state.query = "فرق"
if st.sidebar.button("🎓 البيانات في التعليم"): st.session_state.query = "تعليم"
if st.sidebar.button("🗺️ كيف أبدأ التعلم؟"): st.session_state.query = "roadmap"
if st.sidebar.button("📝 اختبر معلوماتك"): st.session_state.query = "quiz"

# 5. عرض المحادثة
if "messages" not in st.session_state: st.session_state.messages = []

for msg in st.session_state.messages:
    cls = "user-text" if msg["role"] == "user" else "bot-text"
    st.markdown(f'<div class="{cls}">{msg["content"]}</div>', unsafe_allow_html=True)

# 6. معالجة الإدخال
user_input = st.chat_input("اسألني عن أي شيء أو اطلب اختبار... 🤖")
final_query = user_input or st.session_state.get("query")
if "query" in st.session_state: del st.session_state["query"]

if final_query:
    if final_query != "quiz":
        st.markdown(f'<div class="user-text">👤 أنت: {final_query}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": final_query})

    # منطق الردود
    if final_query == "quiz":
        q = random.choice(quiz_data)
        st.session_state.current_q = q
        st.markdown(f'<div class="bot-text">📝 **اختبار سريع:** {q["q"]}</div>', unsafe_allow_html=True)
        ans = st.radio("اختر الإجابة الصحيحة:", q["a"], key="quiz_radio")
        if st.button("تأكيد الإجابة"):
            if ans == q["correct"]:
                st.success("✅ إجابة رائعة يا بطل! أنت الآن Big Data Hero!")
                st.balloons()
            else:
                st.error(f"❌ للأسف، الإجابة الصحيحة هي: {q['correct']}")
    
    elif "roadmap" in final_query or "أبدأ" in final_query:
        resp = kb["roadmap"]
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {resp}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": resp})

    elif any(word in final_query for word in ["رسم", "بيان", "مخطط"]):
        resp = "📊 إليك مخطط يوضح نمو البيانات العالمي:"
        chart_data = pd.DataFrame({'السنة': ['2010', '2020', '2025'], 'الحجم': [2, 45, 175]}).set_index('السنة')
        st.markdown(f'<div class="bot-text">🤖 الوكيل: {resp}</div>', unsafe_allow_html=True)
        st.bar_chart(chart_data)
        st.session_state.messages.append({"role": "assistant", "content": resp})
    
    else:
        # البحث في الـ KB
        found = False
        for k in kb:
            if k in final_query:
                resp = kb[k]
                st.markdown(f'<div class="bot-text">🤖 الوكيل: {resp}</div>', unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": resp})
                found = True; break
        if not found:
            resp = "لم أفهمك تماماً، جرب الاختصارات في القائمة الجانبية أو اطلب (اختبار)."
            st.markdown(f'<div class="bot-text">🤖 الوكيل: {resp}</div>', unsafe_allow_html=True)
