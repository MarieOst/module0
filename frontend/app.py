import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.title("Mon premier chat !")
st.page_title = "Mon premier chat !"

text = st.text_input("Chat", placeholder="Ma question du jour...")

if text and st.button("Envoyer un message"):
    try:
        response = requests.post(f"{API_BASE_URL}/chat", json={"text": text}, timeout=2.0)
        if response.status_code == 200:
            st.success("Message envoyé avec succès !")
        else:
            st.error("Erreur lors de l'envoi du message.")
    except requests.exceptions.RequestException:
        st.error("Impossible de se connecter à l'API FastAPI.")

with st.sidebar:
    st.subheader("Sidebar")
    st.write("Ma super sidebar")
    st.header("État de l'Infrastructure")
    try:
        health_resp = requests.get(f"{API_BASE_URL}/health", timeout=2.0)
        if health_resp.status_code == 200:
            st.success("🟢 API FastAPI en ligne")
        else:
            st.warning("🟠 API en état dégradé")
    except requests.exceptions.RequestException:
        st.error("🔴 API FastAPI inaccessible")