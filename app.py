import streamlit as st
from datetime import datetime, timedelta

st.title("📅 Calculadora de Prazo Processual")

st.write("Simule prazos processuais com base na data de início e quantidade de dias úteis.")

data_inicial = st.date_input("Data inicial do prazo:")
dias = st.number_input("Número de dias úteis:", min_value=1, max_value=365)

if st.button("Calcular"):
    prazo_final = data_inicial
    dias_restantes = dias
    while dias_restantes > 0:
        prazo_final += timedelta(days=1)
        if prazo_final.weekday() < 5:  # segunda a sexta
            dias_restantes -= 1

    st.success(f"📆 O prazo termina em **{prazo_final.strftime('%d/%m/%Y')}**.")