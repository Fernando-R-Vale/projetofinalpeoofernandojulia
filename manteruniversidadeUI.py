import streamlit as st
import pandas as pd
from views import View
import time

class ManterUniversidadeUI:
  def main():
    st.header("Cadastro de universidade")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterUniversidadeUI.listar()
    with tab2: ManterUniversidadeUI.inserir()
    with tab3: ManterUniversidadeUI.atualizar()
    with tab4: ManterUniversidadeUI.excluir()

  def listar():
    universidade = View.universidade_listar()
    if len(universidade) == 0:
      st.write("Nenhum universidade cadastrado")
    else:
      dic = []
      for obj in universidade: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    local = st.text_input("Informe o local")
    telefone = st.text_input("Informe o telefone")
    if st.button("Inserir"):
      View.universidade_inserir(nome, local, telefone)
      st.success("universidade inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    universidade = View.universidade_listar()
    if len(universidade) == 0:
      st.write("Nenhum universidade cadastrado")
    else:
      op = st.selectbox("Atualização de universidade", universidade)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      local = st.text_input("Informe o novo local", op.get_local())
      telefone = st.text_input("Informe o novo telefone", op.get_telefone())
    
      if st.button("Atualizar"):
        id = op.get_id()
        View.universidade_atualizar(id, nome, local, telefone)
        st.success("universidade atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    universidade = View.universidade_listar()
    if len(universidade) == 0:
      st.write("Nenhum universidade cadastrado")
    else:
      op = st.selectbox("Exclusão de universidade", universidade)
      if st.button("Excluir"):
        id = op.get_id()
        View.universidade_excluir(id)
        st.success("universidade excluído com sucesso")
        time.sleep(2)
        st.rerun()
