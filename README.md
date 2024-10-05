# API de Gerenciamento de Veículos

Esta é uma API simples para gerenciar informações sobre veículos, construída com Flask e PostgreSQL. A API permite adicionar, visualizar, atualizar e excluir registros de veículos.

## Tecnologias Utilizadas

- Python 3.10
- Flask
- PostgreSQL
- Docker

## Requisitos
- Python3
- Flask
- PostgreSQL
- Docker

#### Configuração do Banco de Dados
Para configurar o banco de dados PostgreSQL, siga estas etapas:

**Crie um banco de dados PostgreSQL:**

Nome do banco de dados: ```nome_do_banco```
Usuário: ```postgres```
Senha: ```postgress```



## Como Executar o Projeto

### Usando Docker

1. **Certifique-se de ter o Docker e o Docker Compose instalados.**
2. **Navegue até o diretório do projeto:**
   ```bash
   cd /veiculos-api
   ```

3. **Execute o seguinte comando para construir e iniciar os containers:**
   ```bash
   sudo docker-compose up --build
   ```

A API estará disponível em `http://127.0.0.1:5000`.

## Endpoints da API

A API fornece os seguintes endpoints para gerenciar veículos:

### 1. Obter todos os veículos

```http
GET /vehicles
```
Este endpoint retorna uma lista de todos os veículos registrados na base de dados.

**Exemplo de resposta:**
```
{
    "vehicles": [
        {
            "id": 1,
            "make": "Fabrica",
            "model": "Modelo X",
            "year": 2020
        },
        {
            "id": 2,
            "make": "Fabrica",
            "model": "Modelo Y",
            "year": 2021
        }
    ]
}
```
### 2. Adicionar um novo veículo
```http
POST /vehicles
```
Este endpoint permite adicionar um novo veículo. O corpo da requisição deve conter os seguintes campos:

```make```: Marca do veículo
```model```: Modelo do veículo
```year```: Ano do veículo

**Exemplo de corpo da requisição:**
```
{
    "make": "Fabrica",
    "model": "Modelo Z",
    "year": 2022
}
```
**Exemplo de resposta:**
```
{
    "id": 3
}
```

### 3. Atualizar informações de um veículo
```http
PUT /vehicles/<int:id>
```
susbtítua o ```<int:id>``` para o número de um index.

Este endpoint atualiza as informações de um veículo existente. O id do veículo deve ser passado na URL, e o corpo da requisição pode conter os campos a serem atualizados.

**Exemplo de corpo da requisição:**
```
{
    "make": "Nova Fabrica",
    "model": "Modelo Atualizado",
    "year": 2023
}
```

**Exemplo de resposta:**
```
{
    "message": "Vehicle updated"
}
```

### 4. Deletar um veículo
```http
DELETE /vehicles/<int:id>
```
susbtítua o ```<int:id>``` para o número de um index.
Este endpoint remove um veículo da base de dados. O id do veículo deve ser passado na URL.

**Exemplo de resposta:**
```
{
    "message": "Vehicle deleted"
}
```

