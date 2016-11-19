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
- Endereço: http://localhost:8000/ws/login/
- Método: POST, DELETE

Exemplo:

Entrada:
```
Header: Content-Type: application/json
Body: vazio ou qualquer
```
Saída
```
{"status":"sucesso"}

