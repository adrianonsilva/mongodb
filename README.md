# MongoDB
- [1. Descrição](#link1)
- [2. Objetivos](#link2)
- [3. Instalação](#link3)
- [4. Conexão/Comandos básicos](#link4)
- [5. Visualização dados](#link5)
- [6. Links](#link6)

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
Instalar o MongoDB em uma máquina virtual Ubuntu na versão 20.04, usando o apt

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

- MongoDB Shell
O MongoDB Shell é a mesma interface terminal usada anteriormente, só que dessa vez usando o prompt de comando do Windows.



<a id="link6"></a>
## 6. Links

MongoDB
https://www.mongodb.com/

MongoDB Shell
https://www.mongodb.com/try/download/shell

MongoDB Compass
https://www.mongodb.com/try/download/compass



Tutorials Point - MongoDB
https://www.tutorialspoint.com/mongodb/index.htm




