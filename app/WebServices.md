#Serviços REST

##Login
Recebe usuário e senha, e caso autenticado, devolve um token para o acesso
Endereço: http://localhost:8000/ws/login/
Método: POST

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
    


