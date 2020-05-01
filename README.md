# PaginationAPI

##TODO

- run prod (with gunicorn, nginx)
- Unit tests
- CI


Link para documentação:
[http://localhost:5000/api/spec.html#!/spec/wine](http://localhost:5000/api/spec.html#!/spec/wine)


Exemplo de consulta:

[http://localhost:5000/wine?page=1&country=Italy&price=16.0&variety=Red%20Blend&points=87&description=subtle](http://localhost:5000/wine?page=1&country=Italy&price=16.0&variety=Red%20Blend&points=87&description=subtle)

- Se quiser aumentar o número de registros por página, basta alterar o `PAGE_SIZE` para o valor desejado