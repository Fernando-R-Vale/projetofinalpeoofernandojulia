from mantercursoUI import ManterCursoUI
from manterdepartamentoUI import ManterdepartamentoUI
from manteruniversidadeUI import ManterUniversidadeUI
from loginUI import LoginUI
from cursovisitanteUI import CursovisitanteUI
from departamentovisitanteUI import DepartamentovisitanteUI
from universidadevisitanteUI import UniversidadevisitanteUI
from views import View
import streamlit as st
from manteradmUI import ManterAdminUI

class IndexUI:
      
    def sidebare():
      op = st.sidebar.selectbox("Menu", ["Curso", "Departamento", "Universidade", "Administradores"])
      if op == None:  ManterUniversidadeUI.main()
      if op == "Curso": ManterCursoUI.main()
      if op == "Departamento": ManterdepartamentoUI.main()
      if op == "Universidade": ManterUniversidadeUI.main()
      if op == "Administradores": ManterAdminUI.main()
    def visitante():
      op = st.sidebar.selectbox("Menu", ["Visitante", "Administrador"])
      if op == "Visitante": IndexUI.menu_visitante()
      if op == "Administrador":
        View.Adm()
        LoginUI.main()
    
    def btn_logout():
      if st.sidebar.button("Logout"):
        del st.session_state["adm_email"]
        st.rerun()
    def menu_visitante():
      op = st.sidebar.selectbox("Menu", ["Ver cursos", "Ver departamentos", "Ver universidades"])
      if op == "Ver cursos": CursovisitanteUI.main() 
      if op == "Ver departamentos": DepartamentovisitanteUI.main()
      if op == "Ver universidades": UniversidadevisitanteUI.main()
    def sidebar():
      
      if "adm_email"  in st.session_state:
        IndexUI.sidebare() 
        IndexUI.btn_logout() 
      else:
        IndexUI.visitante()  
         
    def main():
      
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()



