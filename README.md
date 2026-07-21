# 📦 Smart Stock

> Status do Projeto: ⚠️ Em desenvolvimento

O **Smart Stock** é um sistema para gerenciamento e controle de estoque. O foco principal do desenvolvimento no momento está na criação e estruturação das funções da aplicação (como conexão, manipulação e cadastro de produtos no banco de dados) e na integração com a interface do Streamlit.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagens:** Python & SQL (SQL Server)
* **Interface / Dashboard:** Streamlit
* **Gerenciamento de Ambientes:** Virtualenv (`.venv`)

---

## 📁 Estrutura do Projeto

```text
smart_stock/
│
├── data/              # Arquivos e bases de dados locais
├── img/               # Imagens e ativos visuais do projeto
├── notebooks/         # Análises e testes em Jupyter Notebooks
├── scripts/           # Scripts auxiliares e de automação
├── src/               # Código-fonte principal da aplicação
│   ├── streamlit/     # Arquivos de configuração da interface Streamlit
│   ├── app.py         # Arquivo principal da aplicação Streamlit
│   └── funcoes.py     # Funções de lógica de negócio e integração com BD
│
├── .gitignore         # Arquivos ignorados pelo Git
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências e bibliotecas do projeto
```

## 🚀 Como Executar o Projeto

Certifique-se de estar com o ambiente virtual ativo (.venv).

Instale as dependências necessárias:

```
Bash
pip install -r requirements.txt

```
Acesse a pasta do código-fonte e execute a aplicação Streamlit:

```
Bash
cd src
streamlit run app.py
```

## 👤 Autor
Desenvolvido por Igor Cruz.