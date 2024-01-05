import streamlit as st
import pandas as pd
from views import View
import time
from departamentovisitanteUI import DepartamentovisitanteUI
class ManterdepartamentoUI:
  def main():
    st.header("Cadastro de departamento")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterdepartamentoUI.listar()
    with tab2: ManterdepartamentoUI.inserir()
    with tab3: ManterdepartamentoUI.atualizar()
    with tab4: ManterdepartamentoUI.excluir()

  def listar():
    # O porque está explicado no mantercursoUI
    DepartamentovisitanteUI.main()
  def inserir():
    nome = st.text_input("Informe o nome do departamento")
    telefone = st.text_input("Informe o telefone")
    id_universidade =  View.universidade_listar()
    oid = st.selectbox("Selecione a universidade", id_universidade)
    
    if st.button("Inserir"):
      View.departamento_inserir(nome, oid.get_id(), telefone)
      st.success("departamento inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    departamento = View.departamento_listar()
    if len(departamento) == 0:
      st.write("Nenhum departamento cadastrado")
    
    else:  
      op = st.selectbox("Atualização de departamento", departamento)
      
      nome = st.text_input("Informe o novo nome", op.get_nome())
      universidade = View.universidade_listar()
      universidade_atual = View.universidade_listar_id(op.get_id())
      
      if universidade_atual is not None:
        universidade = st.selectbox("Selecione a nova universidade", universidade, universidade.index(universidade_atual))
      else:  
        universidade = st.selectbox("Selecione a nova universidade", universidade)
      
      
      telefone = st.text_input("Informe o telefone", op.get_telefone())
      
      
      if st.button("Atualizar"):
        id = op.get_id()
        View.departamento_atualizar(id, nome, universidade.get_id(), telefone)
        st.success("departamento atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    departamento = View.departamento_listar()
    if len(departamento) == 0:
      st.write("Nenhum departamento cadastrado")
    else:  
      op = st.selectbox("Exclusão de departamento", departamento)
      if st.button("Excluir"):
        id = op.get_id()
        View.departamento_excluir(id)
        st.success("departamento excluído com sucesso")
        time.sleep(2)
        st.rerun()
