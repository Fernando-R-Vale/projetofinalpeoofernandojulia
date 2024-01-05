import streamlit as st
import pandas as pd
from views import View

class UniversidadevisitanteUI:
    def main():
        UniversidadevisitanteUI.listar()
    
    def listar():
        universidade = View.universidade_listar()
        if len(universidade) == 0:
            st.write("Nenhum universidade cadastrado")
        else:
            dic = []
            for obj in universidade: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)