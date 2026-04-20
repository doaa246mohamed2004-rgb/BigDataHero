import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة (تحسين المساحة لـ Genially)
st.set_page_config(page_title="Big Data Hero", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #010409; }
    /* تحسين الخطوط للمساحات الصغيرة */
    .stMarkdown, p, li { color: #c9d1d9 !important; font-family: 'Arial'; font-size: 14px; direction: rtl; text-align: right; }
    h1 { color: #00f2ff !important; text-shadow: 0 0 5px #00f2ff; font-size: 20px !important; text-align: center; }
    
    /* تنسيق الأزرار لتكون أصغر وتناسب العرض الضيق */
    .stButton>button { 
        width: 100%; border-radius: 8px; background-color: #1f6feb; 
        color: white; height: 2.5em; font-size: 12px !important; 
        margin-bottom: 5px; border: 1px solid #58a6ff;
    }
    
    /* تحسين فقاعات الدردشة */
    .bot-text { background-color: #0d1a26; color: #00f2ff; border-right: 3px solid #00f2ff; padding: 10px; border-radius: 10px; margin-bottom: 10px; font-size: 13px; }
    .user-text { background-color: #161b22; color: #ffffff; border-left: 3px solid #58a6ff; padding: 8px; border-radius: 10px; margin-bottom: 10px; font-size: 13px; }
    
    #MainMenu, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات (تم التأكد من المفاتيح لتجنب KeyError)
kb = {
    "تعريف": "البيانات الضخمة هي مجموعات بيانات هائلة ومعقدة جداً، بنحتاج طرق ذكية لمعالجتها واستخراج الفائدة منها. 🔍",
    "الفرق": "البيانات العادية حجمها صغير وتتخزن في جهاز واحد، أما الضخمة حجمها عملاق وتتوزع على آلاف الأجهزة (سيرفرات). ⚖️",
    "ذكاء": "العلاقة قوية! البيانات هي 'الغذاء' للذكاء الاصطناعي؛ كل ما زادت البيانات، زادت قدرة الـ AI على التعلم واتخاذ قرارات أدق. 🤖",
    "تسهيل": "بتسهل حياتنا عن طريق: توقع الأمراض، تقليل الزحمة في الخرائط، وحماية حساباتنا البنكية من السرقة فوراً! 🚀",
    "مجالات": "تستخدم في: الطب (تشخيص دقيق)، التعليم (تعلم مخصص)، التجارة (اقتراح ما تحبه)، والمرور. 🌍",
    "ترتيب": "دورة حياة البيانات: 1.التجميع 📥 -> 2.التخزين 🗄️ -> 3.المعالجة 🧼 -> 4.التحليل 🧠 -> 5.التنفيذ ✅"
}

# 3. إدارة الجلسة
if "messages" not in st.session_state: st.session_state.messages = []

# 4. التصميم (استخدام Columns بدلاً من Sidebar لتحسين الرؤية في Genially)
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<h1>المحطات 📍</h1>', unsafe_allow_html=True)
    if st.button("🔍 ما هي؟"): st.session_state.q_auto = "تعريف"
    if st.button("⚖️ الفرق"): st.session_state.q_auto = "الفرق"
    if st.button("🤖 والذكاء الاصطناعي"): st.session_state.q_auto = "ذكاء"
    if st.button("🚀 تسهيل الحياة"): st.session_state.q_auto = "تسهيل"
    if st.button("🌍 المجالات"): st.session_state.q_auto = "مجالات"
    if st.button("📈 النمو"): st.session_state.q_auto = "رسم"
    if st.button("💬 مسح المحادثة"): st.session_state.messages = []

with col2:
    st.markdown('<h1>🤖 الوكيل الذكي</h1>', unsafe_allow_html=True)
    
    # عرض الرسائل
    for m in st.session_state.messages:
        role_class = "user-text" if m["role"] == "user" else "bot-text"
        st.markdown(f'<div class="{role_class}">{m["content"]}</div>', unsafe_allow_html=True)

    u_input = st.chat_input("اسألني أي شيء...")
    query = u_input or st.session_state.get("q_auto")

    if query:
        ans = None
        q_low = query.lower()
        
        # منطق الرد المرن لتجنب KeyError
        if "تعريف" in q_low or "ما هي" in q_low: ans = kb.get("تعريف")
        elif "فرق" in q_low or "مقارنة" in q_low: ans = kb.get("الفرق")
        elif "ذكاء" in q_low or "ai" in q_low: ans = kb.get("ذكاء")
        elif "تسهل" in q_low or "تغير" in q_low: ans = kb.get("تسهيل")
        elif "مجالات" in q_low: ans = kb.get("مجالات")
        elif "ترتيب" in q_low or "خطوات" in q_low: ans = kb.get("ترتيب")
        elif "رسم" in q_low: ans = "حجم البيانات يتضاعف كل عامين، ومن المتوقع وصوله لـ 175 زيتابايت بحلول 2025! 📈"
        
        if not ans:
            ans = "أنا هنا لمساعدتك في فهم عوالم البيانات الضخمة! جرب اختيار موضوع من القائمة."

        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "assistant", "content": ans})
        if "q_auto" in st.session_state: del st.session_state["q_auto"]
        st.rerun()
