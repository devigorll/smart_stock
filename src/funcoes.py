import pyodbc
import requests


# Conectando ao banco 
def conecta_banco():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=smartstock_db;"
            "Trusted_Connection=yes;"
        )
        return conn

    except pyodbc.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None



# busca cep
def buscar_endereco_por_cep(cep):

    cep = "".join(filter(str.isdigit, str(cep)))

    if len(cep) != 8:
        return {"erro": "O CEP deve conter exatamente 8 dígitos."}

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:

        # Faz a requisição para a API e espera no máximo por 5 segundos
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            return {"erro": "Não foi possível consultar o CEP."}

        dados = resposta.json()

        if "erro" in dados:
            return {"erro": "CEP não encontrado."}

        return {
            "estado": dados["uf"],
            "cidade": dados["localidade"],
            "bairro": dados["bairro"]
        }

    except requests.RequestException as e:
        return {"erro": str(e)}




# criando uma nova loja
def cria_loja(dados_loja):

    if dados_loja["Tipo de Loja"] == "Física":

        endereco = buscar_endereco_por_cep(dados_loja["CEP da Loja"])

        if "erro" in endereco:
            return False, endereco["erro"]

        dados_loja["Estado da Loja"] = endereco["estado"]
        dados_loja["Cidade da Loja"] = endereco["cidade"]
        dados_loja["Bairro da Loja"] = endereco["bairro"]

    else:

        dados_loja["Estado da Loja"] = None
        dados_loja["Cidade da Loja"] = None
        dados_loja["Bairro da Loja"] = None
        dados_loja["CEP da Loja"] = None

    conn = conecta_banco()

    if conn is None:
        return False, "Não foi possível conectar ao banco."

    cursor = None

    try:

        cursor = conn.cursor()

        query = """
        INSERT INTO loja
        (
            nome_loja,
            tipo_loja,
            estado,
            cidade,
            bairro,
            cep,
            categoria_loja,
            dono_loja
        )

        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?
        )
        """

        valores = (

            dados_loja["Nome da Loja"],
            dados_loja["Tipo de Loja"],
            dados_loja["Estado da Loja"],
            dados_loja["Cidade da Loja"],
            dados_loja["Bairro da Loja"],
            dados_loja["CEP da Loja"],
            dados_loja["Categoria da Loja"],
            dados_loja["Dono da Loja"]

        )

        cursor.execute(query, valores)

        conn.commit()

        return True, "Loja cadastrada com sucesso!"

    except pyodbc.Error as e:

        return False, f"Erro ao cadastrar loja:\n{e}"

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# consulta lojas
def consulta_lojas():
    conn = conecta_banco()

    if conn is None:
        return False, "Não foi possível conectar ao banco."

    cursor = None

    try:

        cursor = conn.cursor()

        query = """
        SELECT
            id_loja,
            nome_loja
        FROM loja
        """

        cursor.execute(query)

        resultado = cursor.fetchall()

        lojas = []

        for row in resultado:
            lojas.append({
                "id_loja": row[0],
                "nome_loja": row[1]
            })

        return True, lojas

    except pyodbc.Error as e:

        return False, f"Erro ao consultar lojas:\n{e}"

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()



def cadastra_produto(dados_produto):
    conn = conecta_banco()

    if conn is None:
        return False, "Não foi posível se conectar ao banco de dados."
    
    cursor = None
    
    try:

        cursor = conn.cursor()

        query = """
        INSERT INTO produtos
        (
            nome_produto,
            id_loja,
            quantidade_ideal,
            quantidade_real
        )

        VALUES
        (
            ?, ?, ?, ?
        )
        """

        valores = (

            dados_produto["Produto"],
            dados_produto["ID loja"],
            dados_produto["Quantidade ideal"],
            dados_produto["Quantidade atual"]

        )

        cursor.execute(query, valores)

        conn.commit()

        return True, "Produto cadastrado com sucesso!"
    
    except pyodbc.Error as e:

                return False, f"Erro ao cadastrar produto:\n{e}"
    
    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()
        


