import streamlit as st
import pandas as pd
from views import View
import time

class ManterCursoUI:
  def main():
    st.header("Cadastro de Cursos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterCursoUI.listar()
    with tab2: ManterCursoUI.inserir()
    with tab3: ManterCursoUI.atualizar()
    with tab4: ManterCursoUI.excluir()

  def listar():
    cursos = View.curso_listar()
    if len(cursos) == 0:
      st.write("Nenhum curso cadastrado")
    else:  
      dic = []
      for obj in cursos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome do curso")
    professores = st.text_input("Informe o nome do professor responsável")
    vagas = st.text_input("Informe o numero de vagas")
    nivel = st.text_input("Informe o nível")
    departamento_id = View.departamento_listar()
    departamento_id = st.selectbox("Selecione o departamento", departamento_id)
    if st.button("Inserir"):
      View.curso_inserir(nome, professores, int(vagas), nivel, departamento_id)
      st.success("Curso inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    cursos = View.curso_listar()
    if len(cursos) == 0:
      st.write("Nenhum curso cadastrado")
    else:  
      op = st.selectbox("Atualização de Cursos", cursos)
      prof = st.text_input("Informe o novo professor", op.get_professores())
      vagas = st.text_input("Informe as vagas", op.get_vagas())
      nivel = st.text_input("Informe o nível", op.get_nivel())
      departamento = View.departamento_listar()
      departamento_atual = View.departamento_listar_id(op.get_id_departamento())
      if departamento_atual is not None:
        departamento = st.selectbox("Selecione o novo departamento", departamento, departamento.index(departamento_atual))
      else:  
        departamento = st.selectbox("Selecione o novo departamento", departamento)
      if st.button("Atualizar"):
        id = op.get_id()
        View.curso_atualizar(id, prof, int(vagas), nivel, departamento)
        st.success("Curso atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    curso = View.curso_listar()
    if len(curso) == 0:
      st.write("Nenhum Curso cadastrado")
    else:  
      op = st.selectbox("Exclusão de curso", curso)
      if st.button("Excluir"):
        id = op.get_id()
        View.curso_excluir(id)
        st.success("Curso excluído com sucesso")
        time.sleep(2)
        st.rerun()
