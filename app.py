import streamlit as st
import joblib
import numpy as np
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import StackingClassifier
import warnings


warnings.filterwarnings("ignore")

# Load the trained model
model = joblib.load("./stacked_model.joblib")  # Replace with actual model filename

st.title("🔍 AI-Driven Malware Prediction 🛡️")

# Display column names used in training
st.subheader("🚀 Features Used in Model:")
columns = [
    '🔋 modify battery statistics',
    '🔑 access to passwords for Google accounts',
    '📲 monitor and control all application launching',
    '🌐 view network state',
    '📞 make/receive Internet calls',
    '🔒 interact with a device admin',
    '🗺️ modify the Google services map',
    '📱 App',
    '⚙️ modify secure system settings',
    '📦 move application resources',
    '🗑️ delete applications',
    '🧹 delete all application cache data',
    '📺 change screen orientation',
    '📂 reorder running applications',
    '🖥️ access SurfaceFlinger',
    '🖼️ bind to a wallpaper',
    '📁 access the cache filesystem',
    '📖 read Google settings',
    '📴 disable or modify status bar',
    '✍️ write instant messages',
    '📜 expand/collapse status bar',
    '📝 write contact data',
    '🛂 act as an account authenticator',
    '💾 modify/delete USB storage contents',
    '🛡️ interact with a device admin',
    '🗑️ delete other applications caches',
    '🗑️ delete other applications data',
    '🛠️ test hardware',
    '🔊 change your audio settings',
    '🔗 create Bluetooth connections',
    '📡 receive data from Internet',
    '📶 control Near Field Communication',
    '🔧 modify Google settings',
    '📞 directly call any phone numbers',
    '🖼️ read frame buffer',
    '🔧 modify Google settings',
    '🔄 write sync settings',
    '❌ permanently disable device',
    '🔄 modify global system settings',
    '🚀 make application always run',
    '⏩ modify global animation speed',
    '🗑️ delete applications',
    '🌍 full Internet access',
    '🔑 view configured accounts',
    '🔪 kill background processes'
]
st.write(" | ".join(columns))

# Input fields
app_name = st.text_input("📌 Enter App Name", key="app_name")
binary_data = st.text_area("📊 Enter Binary Data (comma-separated)", key="binary_data")

# Prediction function
def predict_malware(binary_input):
    try:
        input_data = np.array([list(map(int, binary_input.split(',')))])
        prediction = model.predict(input_data)[0]
        return prediction
    except Exception as e:
        return f"❌ Error: {e}"

# Predict button
if st.button("🔍 Predict"):
    if binary_data:
        prediction = predict_malware(binary_data)
        if prediction == 1:
            st.markdown('<div style="background-color:#FFB6C1;padding:10px;border-radius:5px;">🚨 Malware Detected! ⚠️</div>', unsafe_allow_html=True)
        elif prediction == 0:
            st.markdown('<div style="background-color:#90EE90;padding:10px;border-radius:5px;">✅ App is Safe 🛡️</div>', unsafe_allow_html=True)
        else:
            st.write(prediction)
    else:
        st.warning("⚠️ Please enter binary data.")

# Clear button to reset inputs and outputs
def clear_inputs():
    st.session_state["app_name"] = ""
    st.session_state["binary_data"] = ""

st.button("🧹 Clear All", on_click=clear_inputs)

