# MongoDB
- [1. Descrição](#link1)
- [2. Objetivos](#link2)
- [3. Instalação](#link3)
- [4. Conexão/Comandos básicos](#link4)
- [5. Programação](#link5)
- [6. Visualização dados](#link6)
- [7. Links](#link7)

<a id="link1"></a>
## 1. Descrição
O MongoDB é um banco de dados NoSQL (not only SQL) (não apenas SQL).

Um banco de dados NoSQL permite armazenar dados estruturados e semi-estruturados, sem exigir um schema pré-definido.

Os principais tipos de bancos de dados NoSQL são documentos, chave-valor, colunas, e gráfico. 

O MongoDB armazenas os dados como documentos, similar a objetos Json (JavaScript Object Notation) .

ex: {Last_name: "Jones", First_name: "Mary", Middle_initial: "S"}

Comparativo entre um banco relacional e o MongoDB (documentos)

| Banco Relacional | MongoDB |
| ----------- | ----------- |
| Database | Database |
| Tabela | Coleção |
| Registro| Documento |
| Coluna | Campo |
| Join | Documentos Embutidos |
| Chave Primária | _id criado pelo MongoDB |


![Screenshot](/images/img00.jpg)

<a id="link2"></a>
## 2. Objetivos
- Realizar a Instalação local.
- Realizar a Conexão local e remota.
- Executar comandos básicos usando ferramentas cliente (criação de banco, coleção, insert de dados, etc).
- Visualização dos dados usando ferramentas de BI como Tableau e PowerBI.

<a id="link3"></a>
## 3. Instalação

É possível utilizar o MongoDB de várias formas, dependendo da necessidade:

- Local (on-premise)
- Cloud MongoDB Atlas
- database-as-a-service (Microsoft Azure, AWS, Google Cloud Platform)

Para facilitar o MongoDB será instalado em uma máquina virtual Ubuntu na versão 20.04, usando o apt

Abra um terminal e execute o comando
sudo apt-get update
![Screenshot](/images/img01.jpg)

Em seguida
sudo apt-get install mongodb-server
![Screenshot](/images/img02.jpg)

Após a instalaçao, editar o arquivo mongodb.conf, para permitir a conexão de qualquer host

sudo nano /etc/mongodb.conf

![Screenshot](/images/img03.jpg)
![Screenshot](/images/img04.jpg)

Salve o arquivo e Verifique o status do serviço
sudo service mongodb status
![Screenshot](/images/img05.jpg)


<a id="link4"></a>
## 4. Conexão/Comandos básicos

Após a instalação vamos conectar no servidor e realizar alguns comandos básicos.
Obs: em um ambiente de produção devemos nos preocupar com a segurança (criação de usuários, permissões, etc), 
mas como o objetivo aqui é navegar pela ferramenta e realizar testes básicos, vamos simplificar.

# Conexão Local

No terminal do servidor digite: mongo

![Screenshot](/images/img06.jpg)

Você estará conectado no servidor local

Listar os databases do servidor : show dbs

![Screenshot](/images/img07.jpg)

Criar um database: use dbteste

![Screenshot](/images/img08.jpg)

Note que o banco criado não aparece na lista de databases, para isso ocorrer é necessário
incluir pelo menos um documento.

Para verificar qual banco está selecionado use: db

![Screenshot](/images/img09.jpg)

Vamos inserir um documento dentro da coleção nomes: db.nomes.insert({"nome":"Exemplo mongodb"})

![Screenshot](/images/img10.jpg)

Agora ao executar o comando show dbs, o database dbteste aparece

![Screenshot](/images/img11.jpg)

Para verificar as coleções use: show collections

![Screenshot](/images/img12.jpg)

No exempo anterior, fizemos o insert de um documento e ao mesmo tempo criando uma coleção (nomes)

Agora, vamos primeiro criar uma coleção e depois realizar o insert: 

db.createCollection('pais')

db.pais.insert({"nome":"Brasil"})

![Screenshot](/images/img13.jpg)

Para realizar consultas utilize o comando find: db.pais.find()

![Screenshot](/images/img14.jpg)

Para realizar uma consulta específica utilize find com parâmetros: db.pais.find({'nome':'Brasil'})

![Screenshot](/images/img15.jpg)

Para obter ajuda utilize o help

![Screenshot](/images/img16.jpg)

![Screenshot](/images/img17.jpg)

Para limpar a tela:

cls
Ctrl+l

# Conexão Remota

Para realizar a conexão remota vamos utilizar uma máquina Windows e instalar 
duas ferramentas client, o MongoDB Shell e MongoDB Compass.

Dessa forma após a instalação vamos acessar o servidor remoto MongoDB (Ubuntu), apartir da máquina Windows.

Os links para instação estão no final do documento

## MongoDB Shell

O MongoDB Shell é a mesma interface terminal usada anteriormente, só que dessa vez apartir 
do prompt de comando do Windows.

No ambiente de teste usado, o servidor MongoDB possui o IP 192.168.1.100, e a porta 27017, como 
não foi configurado usuário, poderemos conectar com o comando: mongosh.exe --host 192.168.1.100:27017

![Screenshot](/images/img18.jpg)

Realizando assim os mesmos comandos executados anteriormente.

## MongoDB Compass

O MongoDB Compass é uma ferramenta gráfica que permite acessar de forma mais intuitiva o servidor

Utilizando a string de conexão: mongodb://192.168.1.100:27017

![Screenshot](/images/img19.jpg)

![Screenshot](/images/img20.jpg)

![Screenshot](/images/img21.jpg)

![Screenshot](/images/img22.jpg)

![Screenshot](/images/img23.jpg)

![Screenshot](/images/img24.jpg)

![Screenshot](/images/img25.jpg)

![Screenshot](/images/img26.jpg)

Através da console, é possível:

- Visualizar informações do servidor
- Visualizar os databases
- Visualizar os documentos
- Realizar consultas
- Criar databases, coleções, adicionar dados
 
Essas são apenas alguns exemplos dos comandos no MongoDB, dando uma breve introdução do ambiente e conceitos.


<a id="link5"></a>
## 5. Programação

Alem da execução de comandos na console, podemos utilizar uma linguagem de programação, para construir aplicações
de forma a termos uma solução automatizada.

Ex: C, C++, C#, .Net, Go, Java, Node.js, Pearl, PHP, Python, Ruby, Scala

## Python

A seguir um exemplo usando Python, onde é exibido no terminal a coleção pais:

![Screenshot](/images/img27.jpg)

![Screenshot](/images/img28.jpg)

Outro exemplo, seria uma aplicação que conecta no Twitter, captura tweets e salva no MongoDB.


<a id="link6"></a>
## 6. Visualização dados

Uma vez que o dados estejam carregados no database, podemos criar visualizações
que permitam aos usuários realizar a tomada de decisão.

- MongoDB Charts
- Ferramentas BI (Tableau, MicroStrategy, Qlik, PowerBI)
- Customizadas (Python e suas bibliotecas: Pandas, Matplotlib, etc)

## MongoDB Charts

MongoDB Charts é uma ferramenta de visualização de dados integrada à plataforma de dados em 
nuvem MongoDB. É a melhor maneira de criar, compartilhar e incorporar visualizações de dados 
MongoDB.

![Screenshot](/images/img29.jpg)

![Screenshot](/images/img30.jpg)

![Screenshot](/images/img31.jpg)

![Screenshot](/images/img32.jpg)

## Ferramentas BI

Para utilizar ferramentas como Tableau, MicroStrategy, Qlik, PowerBI, é necessário instalar o
BI Connector no servidor local e um ODBC na máquina cliente.

Realizar o download do MongoDB Connector for BI
https://www.mongodb.com/try/download/bi-connector
selecione a versão do servidor. (nesse teste vamos usar a versão ubuntu 18.04)

tar -xvzf mongodb-bi-linux-x86_64-ubuntu1804-v2.14.0.tgz

![Screenshot](/images/img33.jpg)

cd mongodb-bi-linux-x86_64-ubuntu1804-v2.14.0

Install o programa

sudo install -m755 bin/mongo* /usr/local/bin/

Vamos realizar o download de um sample de dados para teste

wget http://media.mongodb.org/zips.json

mongoimport --db dbteste --collection zips --file "/home/hduser/downloads/zips.json"

![Screenshot](/images/img34.jpg)

![Screenshot](/images/img35.jpg)

![Screenshot](/images/img36.jpg)

Start no BI Connector

mongosqld --addr 0.0.0.0

![Screenshot](/images/img37.jpg)

Na máquina cliente vamos configurar o ODBC, utilizar o Unicode driver.

![Screenshot](/images/img38.jpg)

![Screenshot](/images/img39.jpg)

![Screenshot](/images/img40.jpg)

![Screenshot](/images/img41.jpg)

![Screenshot](/images/img42.jpg)

Abrindo o PowerBI

![Screenshot](/images/img43.jpg)

![Screenshot](/images/img44.jpg)

![Screenshot](/images/img45.jpg)

![Screenshot](/images/img46.jpg)

![Screenshot](/images/img47.jpg)

![Screenshot](/images/img48.jpg)

![Screenshot](/images/arq.jpg)

<a id="link7"></a>
## 7. Links

MongoDB
https://www.mongodb.com/

MongoDB Shell
https://www.mongodb.com/try/download/shell

MongoDB Compass
https://www.mongodb.com/try/download/compass

MongoDB Atlas
https://www.mongodb.com/cloud/atlas

Tipos de Databases NoSQL
https://www.guru99.com/nosql-tutorial.html

Tutorials Point - MongoDB
https://www.tutorialspoint.com/mongodb/index.htm
