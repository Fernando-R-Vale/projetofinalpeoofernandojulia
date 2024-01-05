from mantercursoUI import ManterCursoUI
from manterdepartamentoUI import ManterdepartamentoUI
from manteruniversidadeUI import ManterUniversidadeUI
from loginUI import LoginUI
from cursovisitanteUI import CursovisitanteUI
from departamentovisitanteUI import DepartamentovisitanteUI
from universidadevisitanteUI import UniversidadevisitanteUI
from views import View
import streamlit as st

class IndexUI:
      
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Login", "Curso", "Departamento", "Universidade"])
      if op == "Curso": ManterCursoUI.main()
      if op == "Departamento": ManterdepartamentoUI.main()
      if op == "Universidade": ManterUniversidadeUI.main()
      
    def btn_logout():
      if st.sidebar.button("Logout"):
        del st.session_state["cliente_id"]
        st.rerun()
    def menu_cliente():
      op = st.sidebar.selectbox("Menu", ["Ver cursos", "Ver departamentos", "Ver universidades"])
      if op == "Ver cursos": CursovisitanteUI.main()
      if op == "Ver departamentos": DepartamentovisitanteUI.main()
      if op == "Ver universidades": UniversidadevisitanteUI.main()
      if st.sidebar.button("Login"):
        LoginUI.main()
    def sidebar():
      if "cliente_id" not in st.session_state:
        IndexUI.menu_visitante()   
      else:
        IndexUI.menu_admin() 
        IndexUI.btn_logout() 
         
    def main():
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()



