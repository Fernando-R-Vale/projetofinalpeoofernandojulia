import streamlit as st
import pandas as pd
from views import View
import time
class ManterAdminUI:
  def main():
    st.header("Cadastro de Admin")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterAdminUI.listar()
    with tab2: ManterAdminUI.inserir()
    with tab3: ManterAdminUI.atualizar()
    with tab4: ManterAdminUI.excluir()

  def listar():
    Adm = View.Adm_listar()
    if len(Adm) == 0:
      st.write("Nenhum Adm cadastrado")
    else:
      dic = []
      for obj in Adm: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      df = df.drop('_adm__id', axis=1)
      st.dataframe(df, hide_index=True)
  def inserir():
    email = st.text_input("Informe o email do adm")
    senha = st.text_input("Informe a senha")
    
    
    if st.button("Inserir"):
      View.Adm_inserir(email, senha)
      st.success("Adm inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    Adms = View.Adm_listar()
    if len(Adms) == 0:
      st.write("Nenhum Adm cadastrado")
    else:  
      op = st.selectbox("Atualização de Adms", Adms)
      email = st.text_input("Informe o novo email", op.get_email())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        id = op.get_id()
        View.Adm_atualizar(id, email, senha)
        st.success("Adm atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    Adm = View.Adm_listar()
    if len(Adm) == 0:
      st.write("Nenhum Adm cadastrado")
    else:  
      op = st.selectbox("Exclusão de Adm", Adm)
      if st.button("Excluir"):
        id = op.get_id()
        View.Adm_excluir(id)
        st.success("Adm excluído com sucesso")
        time.sleep(2)
        st.rerun()
