USE MASTER;
G

CREATE DATABASE smartstock_db;
GO

USE smartstock_db;
GO

-- 1. TABELA DONO LOJA 
CREATE TABLE dono_loja (
	id_dono_loja INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(50) NOT NULL,

	CONSTRAINT PK_Dono_loja PRIMARY KEY (id_dono_loja)
)

-- 2. TABELA CATEGORIA LOJA 
CREATE TABLE categoria_loja (
	id_categoria_loja INT IDENTITY(1,1) NOT NULL,
	categoria_loja VARCHAR(30) NOT NULL,

	CONSTRAINT PK_Categoria_loja PRIMARY KEY (id_categoria_loja)
)

-- 3. TABELA CATEGORIA PRODUTO 
CREATE TABLE categoria_produto (
	id_categoria_produto INT IDENTITY(1,1) NOT NULL,
	nome_categoria_produto VARCHAR(30) NOT NULL,
	id_categoria_loja INT NOT NULL,

	CONSTRAINT PK_Categoria_produto PRIMARY KEY (id_categoria_produto),
	CONSTRAINT FK_Categoria_loja FOREIGN KEY (id_categoria_loja) REFERENCES categoria_loja(id_categoria_loja)
)

-- 4. TABELA LOJA
CREATE TABLE loja (
	id_loja INT IDENTITY(1,1) NOT NULL,
	nome_loja VARCHAR(30) NOT NULL,
	id_categoria_loja INT NOT NULL,
	id_dono_loja INT NOT NULL, 

	-- FÍSICA OU ONLINE
	tipo_loja VARCHAR(10),
	
	estado CHAR(2) NULL,
	cidade VARCHAR(30) NULL,
	bairro VARCHAR(30) NULL,
	cep CHAR(8) NULL,

	CONSTRAINT PK_Loja PRIMARY KEY (id_loja),
	CONSTRAINT FK_Dono_loja FOREIGN KEY (id_dono_loja) REFERENCES dono_loja(id_dono_loja),
	CONSTRAINT FK_Categoria_loja_na_loja FOREIGN KEY (id_categoria_loja) REFERENCES categoria_loja(id_categoria_loja)
)

-- 5. TABELA PRODUTOS 
CREATE TABLE produtos (
	id_produto INT IDENTITY(1,1) NOT NULL,
	nome_produto VARCHAR(50) NOT NULL,
	id_loja INT NOT NULL,
	id_categoria_produto INT NOT NULL,

	quantidade_ideal INT NOT NULL,
	quantidade_real INT NOT NULL,

	CONSTRAINT PK_Produto PRIMARY KEY (id_produto),
	CONSTRAINT FK_Loja FOREIGN KEY (id_loja) REFERENCES loja(id_loja),
	CONSTRAINT FK_Categoria_produto_no_produto FOREIGN KEY (id_categoria_produto) REFERENCES categoria_produto(id_categoria_produto)
)

-- 6. TABELA CLIENTES
CREATE TABLE clientes (
	id_cliente INT IDENTITY(1,1) NOT NULL,
	nome_cliente VARCHAR(50) NOT NULL,
	
	estado CHAR(2) NULL,
	cidade VARCHAR(30) NULL,
	bairro VARCHAR(30) NULL,
	cep CHAR(8) NULL,

	CONSTRAINT PK_Clientes PRIMARY KEY (id_cliente)
)

-- 7. TABELA VENDAS
CREATE TABLE vendas (
	id_venda INT IDENTITY(1,1) NOT NULL,
	id_loja INT NOT NULL,
	id_produto INT NOT NULL,
	id_cliente INT NOT NULL,
	
	quantidade INT NOT NULL,

	CONSTRAINT PK_Vendas PRIMARY KEY (id_venda),
	CONSTRAINT FK_Loja_na_venda FOREIGN KEY (id_loja) REFERENCES loja(id_loja),
	CONSTRAINT FK_Produto_na_venda FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
	CONSTRAINT FK_Cliente_na_venda FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)

