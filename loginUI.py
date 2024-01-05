import streamlit as st
import pandas as pd
from views import View
import time

class LoginUI:
  def main():
    st.header("Login")
    LoginUI.inserir()

  def inserir():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      x = View.Adm_login(email, senha)
      if x == True:
        st.success("Login realizado com sucesso")
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a)")
        st.session_state["_adm__id"] = x.get_id()
      else:
        st.error("Usuário ou senha inválido(s)")
      time.sleep(2)
      st.rerun()