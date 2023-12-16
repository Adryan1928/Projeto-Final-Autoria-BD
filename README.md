# Projeto-Final-Autoria-BD
 Esse é um repositório para o projeto final da matéria de Autoria Web e Banco de Dados

## ⚙ Executando a aplicação
### 📦 Requerimentos
Primeiramente, crie um ambiente virtual em seu terminal usando o seguinte comando e rode `venv\Scripts\activate` caso o ambiente virtual não esteja ativado.
```
python -m venv venv`
```
Após isso, é necessário instalar os pacotes que vamos utilizar na aplicação. Execute: 
```
pip install -r requirements.txt
```

### 🛠 Configurando o ambiente local
Antes de executar a aplicação, você precisa configurar suas variáveis de ambiente, que devem ser armazenadas em um arquivo `.env` na raiz do seu projeto (você deve criá-lo e colocar as variáveis declaradas em `.env.template`). Aqui está como o conteúdo do seu arquivo `.env` deve parecer:
```properties
SECRET_KEY=sua-chave-secreta
FLASK_APP=main.py
FLASK_ENV=development
FLASK_DEBUG=true
```

Para gerar sua própria chave secreta, você pode usar o módulo `secrets` do Python. Abra um terminal e execute o seguinte comando:

```python
python -c "import secrets; print(secrets.token_hex(24))"
```
Agora só substituir sua-chave-secreta pelo valor gerado.

### 🌶 Ligando servidor Flask
Por fim, basta acionar o servidor Flask pelo comando abaixo e acessar a aplicação pelo localhost.
```
flask run
```