import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import funcoes as fn


# Configuradno titulo da página do streamlit
st.set_page_config(
    page_title="Smart Stock",
    page_icon="📦",
    layout="wide"
)

# Mudando de estilo para os gráficos
sns.set_theme(style="whitegrid")

# Imprtar dados aqui 
# Gerar DF com o vw_envio
# df = pd.read_csv("")

# Sidebar
st.sidebar.title("Filtros Globais")
st.sidebar.markdown("Use os filtros abaixo para segmentar a visão geral:")

# Título tela inicial
st.title("📦 Smart Stock")
st.markdown("""
Este é o primeiro esboço da tela do Smart Stock, uma aplicação web para controle de estoque.
""")

# Definindo abas no dashboards
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📍 Visão Geral " ,
    "📦 Controle de Estoque ",
    "💰 Vendas ",
    "🏢 Cadastro de Lojas ",
    "🏷️ Cadastro de Produtos"
])

with tab1:
    st.header("📍 Visão Geral")
    st.markdown("""
    Nesta seção, você encontrará uma visão geral do monitoramento logístico, incluindo métricas-chave e gráficos que fornecem insights sobre o desempenho das operações logísticas.
    """)
    
    col1, col2, col3 = st.columns(3)


with tab4:

    st.header("🏢 Cadastro de Lojas")
    st.markdown("""
    Nesta seção, você pode cadastrar novas lojas e gerenciar as informações das lojas existentes.
    """)

    with st.form("cadastro_loja"):

        nome_loja = st.text_input("Nome da Loja")

        dono_loja = st.text_input("Nome do Dono da Loja")

        categorias_loja = [
            "Supermercado", "Farmácia", "Depósito de Bebidas", "Restaurante",
            "Pizzaria", "Hamburgueria", "Padaria", "Pet Shop", "Açougue",
            "Hortifruti", "Loja de Roupas", "Calçados", "Cosméticos e Perfumaria",
            "Eletrônicos e Informática", "Eletrodomésticos", "Material de Construção",
            "Papelaria e Escritório", "Livraria", "Brinquedos", "Artigos Esportivos",
            "Ótica", "Joalheria e Semijoias", "Móveis e Decoração", "Loja de Variedades",
            "Suplementos Alimentares", "Auto Peças", "Sorveteria e Doceria",
            "Cafeteria", "Chocolataria", "Floricultura"
        ]

        categoria_loja = st.selectbox(
            "Categoria da Loja",
            categorias_loja
        )

        tipo_loja = st.selectbox(
            "Tipo de Loja",
            ["Física", "Online"]
        )

        cep_loja = ""

        if tipo_loja == "Física":
            cep_loja = st.text_input(
                "CEP da Loja",
                max_chars=9,
                help="Digite apenas o CEP."
            )

        submit = st.form_submit_button("Cadastrar Loja")

        if submit:

            if nome_loja.strip() == "":
                st.error("Informe o nome da loja.")

            elif dono_loja.strip() == "":
                st.error("Informe o dono da loja.")

            elif tipo_loja == "Física" and cep_loja.strip() == "":
                st.error("Informe o CEP da loja.")

            else:

                dados_loja = {

                    "Nome da Loja": nome_loja,
                    "Dono da Loja": dono_loja,
                    "Categoria da Loja": categoria_loja,
                    "Tipo de Loja": tipo_loja,
                    "CEP da Loja": cep_loja

                }

                sucesso, mensagem = fn.cria_loja(dados_loja)

                if sucesso:
                    st.success(mensagem)

                else:
                    st.error(mensagem)

with tab5:
    st.header("🏷️ Cadastro de Produtos")
    st.markdown("""
    Nesta seção, você pode cadastrar novos produtos e gerenciar as informações dos produtos existentes.
    """)

    with st.form("cadastro_produto"):

        nome_produto = st.text_input("Nome do Produto")

        sucesso, lojas = fn.consulta_lojas()

        # Valida se a consulta deu certo E se veio alguma loja na lista
        if sucesso and lojas:
            loja_selecionada = st.selectbox(
                "Loja do Produto",
                options=lojas,
                format_func=lambda loja: loja["nome_loja"]
            )
            # O selectbox retorna o dicionário selecionado
            id_loja = loja_selecionada["id_loja"] if loja_selecionada else None
        else:
            if not sucesso:
                st.error(f"Erro ao buscar lojas: {lojas}")
            else:
                st.warning("Nenhuma loja cadastrada no sistema.")
            id_loja = None

        quantidade_ideal = st.number_input(
            "Quantidade Ideal do Produto",
            min_value=1,
            step=1
        )

        quantidade_atual = st.number_input(
            "Quantidade Atual do Produto",
            min_value=0,
            step=1
        )

        submit_produto = st.form_submit_button("Cadastrar Produto")

        if submit_produto:
            # 1. Verifica se o nome do produto não está vazio (strip remove espaços acidentais)
            if not nome_produto.strip():
                st.error("Insira o nome do produto.")

            # 2. Verifica se uma loja válida foi carregada e selecionada
            elif id_loja is None:
                st.error("Selecione uma loja válida antes de cadastrar.")

            else:
                dados_produto = {
                    "Produto": nome_produto.strip(),
                    "ID loja": id_loja,
                    "Quantidade ideal": quantidade_ideal,
                    "Quantidade atual": quantidade_atual
                }

                sucesso, mensagem = fn.cadastra_produto(dados_produto)
                
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)