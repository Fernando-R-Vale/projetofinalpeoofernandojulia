import streamlit as st
import pandas as pd
from views import View

class CursovisitanteUI:
    def main():
        CursovisitanteUI.cursos()
    def cursos():
        universidade = View.universidade_listar()
        universidade = st.selectbox("Selecione uma universidade", universidade)
        
        departamento = View.departamento_listar()
        if len(departamento) == 0:
            st.write("Nenhum departamento cadastrado")
        else:  
            departamento_id = View.departamento_listar()
            departamento_id = st.selectbox("Selecione o departamento", departamento_id)
            
        
        cursos = View.curso_listar()
        dic = []
        for obj in cursos: 
            if cursos.get_id_departamento() == departamento_id.get_id():
                dic.append(obj.__dict__)
        df = pd.DataFrame(dic)
        if len(df) == 0:
            st.write("Nenhum curso cadastrado")
        else: st.dataframe(df)