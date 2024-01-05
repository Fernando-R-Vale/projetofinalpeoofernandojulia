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
            s = []
            for x in departamento:
                if x.get_id_universidade() == universidade.get_id():
                    s.append(x)
            departamento_id = st.selectbox("Selecione o departamento", s)
            
        
        cursos = View.curso_listar()
        dic = []
        for obj in cursos: 
            if obj.get_departamento() == departamento_id.get_id():
                dic.append(obj.__dict__)
        df = pd.DataFrame(dic)
        if len(df) == 0:
            st.write("Nenhum curso cadastrado")

        else: 
            df = df.drop('_curso__id', axis=1)
            df = df.drop('_curso__departamento', axis=1)
            st.dataframe(df, hide_index=True)