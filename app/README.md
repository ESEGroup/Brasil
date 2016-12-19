#Serviços REST

##Geral
Para o mozilla aconselho a extensão [restclient](https://addons.mozilla.org/pt-br/firefox/addon/restclient/)


##Login
Recebe usuário e senha, e caso autenticado, devolve um token para o acesso
- Endereço: http://localhost:8000/ws/login/
- Método: POST

Exemplo:

Entrada:
```
Header: Content-Type: application/json
Body: {"username":"usertest","password":"m1m2m3m4"}
```
Saída
```
{"token": "6f1483b1dd4983620ef17a588de1d0e83dcf236f"}
```
Saída (Exceção)
```
{"non_field_errors":["Impossível fazer login com as credenciais fornecidas."]}
```
    
##Template 
Deve ser usado para qualquer requisição após o login
- Endereço: http://localhost:8000/ws/{{ nome }}/
- Métodos: Variados, sempre há pelo menos POST

Entrada:
```
Header: Content-Type: application/json
Header: Authorization: Token 0135ba7654e857b61832705002e5a2ad9e76423e
```
Saída (Exceção)
```
{"non_field_errors":["Unexpected error:" + stacktrace]}

```

##Logout
Recebe token de um usuário e o renova internamente
- Endereço: http://localhost:8000/ws/logout/
- Método: POST, DELETE

Exemplo:

Entrada:
```
Body: vazio ou qualquer
```
Saída
```
{"status":"sucesso"}
```
##Cadastro de Usuários
Cadastro para Funcionários, Administradores e SuperAdministradores
- Endereços:http://localhost:8000/ws/cadastro/funcionario/
            http://localhost:8000/ws/cadastro/administrador/
            http://localhost:8000/ws/cadastro/superadministrador/

- Método: POST, GET

URLs diferentes para níveis de acesso diferentes definidos pelo token
Exemplo:

Entrada:
```
Body: {"username":"any", "email":"somethind@mail.com", "first_name" : " ", "last_name" : " ", "registro" : "58", "departamento" : "CT"}
```
Saída
```
{"status":"sucesso"}
```
##Atualização de Usuários
Atualização de informações para Funcionários, Administradores e SuperAdministradores
- Endereço: http://localhost:8000/ws/update/funcionario/
            http://localhost:8000/ws/update/administrador/
            http://localhost:8000/ws/update/superadministrador/
- Método: POST, GET

URLs diferentes para níveis de acesso diferentes definidos pelo token
Exemplo:

Entrada:
```
Body: {"pk":"6","username":"any", "password":"pass","email":"somethind@mail.com", "first_name" : " ", "last_name" : " ", "registro" : "58", "departamento" : "CT"}
```
Saída
```
{"status":"sucesso"}
```

##Deleção de Usuários
Torna Funcionários, Administradores ou SuperAdministradores inativos
- Endereço: http://localhost:8000/ws/delete/funcionario/
            http://localhost:8000/ws/delete/administrador/
            http://localhost:8000/ws/delete/superadministrador/
- Método: POST, GET

URLs diferentes para níveis de acesso diferentes definidos pelo token
Exemplo:

Entrada:
```
Body: {"pk":"6","username":"any", "password":"pass","email":"somethind@mail.com", "first_name" : " ", "last_name" : " ", "registro" : "58", "departamento" : "CT"}
```
Saída
```
{"status":"sucesso"}
```

##Cadastro de Agendamentos
Cadastro para Agendamentos
- Endereço: http://localhost:8000/ws/cadastro/agendamento/
- Método: POST, GET

Exemplo:

Entrada:
```
{"username":"usertest", "patrimonio":"777474","inicio":"2006-10-25 14:30:59","periodo":"7"}
```
Saída
```
{"status":"sucesso","PrimaryKey":"6"}
```

##Deleção de Agendamentos
Cadastro para Agendamentos
- Endereço: http://localhost:8000/ws/cadastro/agendamento/
- Método: POST, GET

Exemplo:

Entrada:
```
{"pk":"6","username":"usertest", "patrimonio":"777474","inicio":"2006-10-25 14:30:59","periodo":"7"}
```
Saída
```
{"status":"sucesso"}
```