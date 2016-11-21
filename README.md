# Brasil - Agendae


## Sobre o projeto

O projeto Agendaê é um sistema de agendamento de recursos acadêmicos desenvolvido no contexto da matédia de Engenharia de Software  *(EEL873)*, ministrada pelo professor Guilherme Horta Travassos na Universidade Federal do Rio de Janeiro em 2016.2.

Ao longo do curso foram levantados diversos requisitos e estabelecidas inumeras restrições e alterações. Todo essetrabalho culminou no conteúdo desse repositório, que em sua totalidade contém a implementação prática do projeto suas minúcias de especificação na aba Wiki.

## Como utilizar

### Requisitos Técnicos

As seguintes tecnologias são necessárias para o bom funcionamento do sistema:

- Python 3

Todas as outras dependências e bibliotecas externas já estão acopladas nesse repositório e não necessitam de maior atenção do usuário. O sistema de base de dados utilizado foi o `sqlite3` fornecido pelo próprio Django.

#### Inicializando o ambiente

- Faça download o clone o repositório para um diretório dentro de sua preferência. Em caso de download do arquivo .zip não se esqueça de extrair os aqruivos.
- Utillizando o terminal, navegue até o diretório que você extraiu esse repositório e digite o seguinte comando:
```
source env/bin/activate

```

### Inicializando o servidor

Para usuários do sistema operacional Linux, basta navegar até o diretório que foi extraido o repositório e digitar o comando a seguir no terminal de controle.

```
python3 manage.py runserver
```

- Acesse a aplicação em `http://127.0.0.1:8000/` ou `localhost:8000/`
- Utilize o usuário **admin** e a senha **admin** para se autenticar no sistema.



## Responsáveis

- [Caio Riqueza](https://github.com/caiocrr)
- [Lucas Rolim](https://github.com/lucaslrolim)
- [Pedro Boueke](https://github.com/pboueke)
- [Vinícius Alves](https://github.com/vinicius-alves)
