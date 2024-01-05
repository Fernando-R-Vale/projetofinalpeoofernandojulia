import streamlit as st
import pandas as pd
from views import View

class DepartamentovisitanteUI():
    def main():
        DepartamentovisitanteUI.listar()
    def listar():
        universidade = View.universidade_listar()
        universidade = st.selectbox("Selecione uma universidade", universidade)
        
        departamento = View.departamento_listar()
        dic = []
        for obj in departamento: 
            if universidade.get_id() == obj.get_id_universidade():
                dic.append(obj.__dict__)
        df = pd.DataFrame(dic)
        if len(df) == 0:
            st.write("Nenhum departamento cadastrado")
        else: st.dataframe(df)