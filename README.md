# PaginationAPI
**Descrição:** Este projeto tem como objetivo fornecer uma API que retorne dados paginados de um dataset de vinhos

## Instruções de como instalar e rodar o projeto
 
- Para poder fazer a instalação das dependências do projeto, certifique-se que os pacotes 
[Docker](https://www.docker.com/) (versão 17.05 ou mais recente) e [Docker Compose](https://docs.docker.com/compose/) 
estejam instalados em sua máquina.
- Certifique-se de que não há nenhum serviço rodando na porta 5000, pois é nessa porta que o serviço executará.
- Execute o seguinte comando para instalar e executar o projeto na sua máquina:
```
make build
```
**ou** 
```
docker-compose up -d --build api_pagination
```
- Após rodar esse comando, o projeto já estará sendo executado em sua máquina em 
modo de desenvolvimento. Abra [http://localhost:5000/wine?page=1](http://localhost:5000/wine?page=1) 
para ver a aplicação rodando.
- Nesse repositório foi disponibilizado um banco `wine.db`, 
no qual já está populado com os dados do arquivo `winemag-data-130k-v2.csv`, disponível neste [link](https://www.kaggle.com/zynicide/wine-reviews).
Portanto, com a execução do projeto já é possível fazer as consultas e filtros dos dados. 
Há um tutorial detalhado para isso, de nome "Instruções de como retornar/filtrar os dados pela API".  
E as informações de como esse banco foi populado podem ser encontrados no tópico de "Comandos/informações adicionais".
- Caso precise parar a aplicação, rode:
```
make stop
```
- Uma vez que a aplicação foi interrompida com o comando acima, para rodá-la novamente, basta executar:
```
make up
```
 
**Obs.:** Essas instruções são para sistemas operacionais com distribuições de base Unix e Linux.


## Instruções de como retornar/filtrar os dados pela API
- Para facilitar o entendimento do funcionamento dos filtros e retorno dos dados da API, 
foi feita uma documentação dela com o [Swagger](https://swagger.io/).
- Para acessá-la, certifique-se que a aplicação está rodando e abra o 
seguinte endereço: [http://localhost:5000/api/spec.html#!/spec/wine](http://localhost:5000/api/spec.html#!/spec/wine)
- Nessa API, foi disponibilizado uma "View" para retorno dos dados de forma paginada, 
que pode ser encontrada no arquivo `src/wine.py`.
- O número de registros retornados por página é definido pela variável `PAGE_SIZE`, 
que pode ser alterado no arquivo `config.py`.  
- O caminho de url para essa view é `/wine`.
- O método para retornar os dados é o `GET`.
- Essa view aceita os filtros via passagem de parâmetros (query params) na url.
- Os filtros disponíveis são os campos "country", "description", "points", "price" e "variety".
- O único parâmetro obrigatório é o número da página (page), que começa com 1 e vai até o limite de página dos dados.
- A api retorna os dados de vinho na chave `data` do json retornado. Também é retornado as seguintes chaves: 
  - `current_page`: número da página atual
  - `has_next_page`: booleano que informa se há uma próxima página de dados
  - `has_prev_page`: booleano que informa se há uma página anterior de dados
  - `num_pages`: número de total de páginas disponíveis para esses dados
  - `url_next_page`: url para a próxima de dados, caso haja uma próxima página de dados.
- Para um exemplo de retorno dos dados pela API, abra:
[http://localhost:5000/wine?page=1&country=Italy&price=16.0&variety=Red%20Blend&points=87&description=subtle](http://localhost:5000/wine?page=1&country=Italy&price=16.0&variety=Red%20Blend&points=87&description=subtle) 

  


## Comandos/informações adicionais

- Neste projeto, foi disponibilizado um teste de funcionalidade simples de retorno dos dados. 
O teste está disponível no arquivo `test_flask.py`. Caso queira executá-lo, 
certifique-se que a aplicação está rodando e execute o comando:
```
make test
```
- Foi disponibilizado, também, o modo produção do projeto para rodar com o `Gunicorn` e o `Nginx`. 
A razão da escolha dessas tecnologias está descrita no tópico "Arquitetura". 
Para rodar o projeto em modo produção, antes certique-se que não há nenhum serviço sendo executado na porta 81 e rode o comando: 
```
make build-prod
```
- Após a execução do comando logo acima, abra [http://localhost:81/wine?page=1](http://localhost:81/wine?page=1) 
para ver a aplicação executando em modo produção, porém sem SSL.
- Com os tópicos descritos acima, foi possível fazer uma simples rotina de CI (Continuous Integration), 
disponível no arquivo `.github/workflows/ci.yml`. Ele instala e executa o projeto nos modo de desenvolvimento e produção 
e roda os testes, toda vez que é feito um "push" na "branch" `master` ou é feito um "pull request" nessa mesma "branch".
- O banco `wine.db` disponibilizado neste repositório, foi populado com o script `populate_db.py`. 
Caso queira rodar esse script, adicione o arquivo `winemag-data-130k-v2.csv` 
([link para download](https://www.kaggle.com/zynicide/wine-reviews)) no diretório `data/`. 
Este arquivo não foi mantido no repositório para que ele não ficasse pesado.  

## Arquitetura 
**Este tópico visa sugerir uma possível arquitetura para essa aplicação.** 


A seguir há uma imagem com a arquitetura e, 
logo após, tópicos onde é explicado cada uma das tecnologias escolhidas.


- Docker:
    A escolha dessa tecnologia é por além de simplificar a metodologia DevOps,
    ela possibilita uma economia de recursos e velocidade por ter imagens bastante simplificados 
    dos sistemas operacionais. E principalmente por ser escalável, pois como a aplicação seria utilizada por 
    vários usuários simultaneamente, ela obrigatoriamente precisa ser escalável para uma boa e eficiente 
    experiência de usuário.
    
- Nginx:
    Por ser um servidor web muito utilizado, bastante eficiente e prático nas suas operações de servidor e acessos 
    simultâneos  com balanceamento de carga HTTP, ele serviria de uma forma bastante eficiente como o balanceador e 
    reverse proxy para a aplicação. O que proporcionaria mais velocidade e escabilidade. Dessa forma, 
    os múltiplos acessos simultâneos dos usuários chegariam nele primeiro para que ele fosse a porta de entrada e 
    aceitasse/barrasse cada uma das requisições e caso fosse aceita, a redicionaria para o Gunicorn.
    
- Gunicorn:
     Como o python por si só não é um servidor WSGI (Web Server Gateway Interface) próprio e eficiente para acessos 
     simultâneos, é preciso encontrar soluções que desempenhem de tal maneira. O Gunicorn é um dos vários servidores 
     WSGI disponíveis no mercado, porém ele se destaca por ser estável, utilizado pelas maiores aplicações Web feitas 
     em python (como o Instagram) e, principalmente, por permitir a comunicação com multiplos servidores web e por lidar
     com múltiplos acessos simultaneios, permitindo que você configure o número de threads utilizados para cada 
     requisição e o número de processos simultâneos que serão executados.
     
- Flask:
    Por ser uma framework em python que se destaca pela praticidade, facilidade, liberdade e por ter uma grande comunidade, 
    ele foi escolhido para servir a API. Ele poderia muito bem ser trocado pelo Django, que possue uma liberdade um pouco 
    menor que o Flask, porém tem uma robustez maior. A escolha entre essas duas frameworks pode ser mais assertiva quando
    se tem uma clara definição do projeto e seus requisitos a ser desenvolvido, além dos desenvolvedores que atuaram nele.  
       
