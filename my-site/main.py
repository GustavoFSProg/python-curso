import streamlit as st

from PIL import Image
import os
# import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/curso-python)")


# @st.cache_data
# def carregar_dados():
#     tabela = pd.read_csv("resultados.csv")
#     return tabela

with st.container():
    st.write("Este é meu primeiro site com Python!")
    # st.write("---")
    # qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    # num_dias = int(qtde_dias.replace("D", ""))
    # dados = carregar_dados()
    # dados = dados[-num_dias:]
    # st.area_chart(dados, x="Data", y="Contratos")


# Solicita o caminho da imagem ao usuário
path = ("comida1.jpg")

# Verifica se o arquivo existe
if os.path.isfile(path):
    # Abre a imagem
    img = Image.open(path)
    # Agora você pode trabalhar com a imagem
else:
    print("Arquivo não encontrado. Por favor, tente novamente.")

img

# def click

st.button("Reset",'reset',help="ajuda sobre o botao", type="primary")

# if st.button('Clique Aqui'):
#     st.write('Clicou!')

# else:
#     st.write('Reset')

#     st.write(st.session_state)
