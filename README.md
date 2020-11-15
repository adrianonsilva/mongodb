# MongoDB
- [1. Descrição](#link1)
- [2. Objetivos](#link2)
- [3. Instalação](#link3)
- [4. Conexão](#link4)
- [5. Comandos básicos](#link5)
- [6. Visualização dados](#link6)

<a id="link1"></a>
## 1. Descrição
O MongoDB é um banco de dados NoSQL (not only SQL) (não apenas SQL).
Um banco de dados NoSQL permite armazenar dados estruturados e semi-estruturados, sem exigir um schema pré-definido.
Os principais tipos de bancos de dados NoSQL são documentos, chave-valor, colunas, e gráfico. 
O MongoDB armazenas os dados como documentos, similar a objetos Json (JavaScript Object Notation) .
ex: {Last_name: "Jones", First_name: "Mary", Middle_initial: "S"}

<a id="link2"></a>
## 2. Objetivos
- Realizar a Instalação local.
- Realizar a Conexão local e remota.
- Executar comandos básicos usando ferramentas cliente (criação de banco, coleção, inset de dados, etc).
- Visualização dos dados usando ferramentas de BI como Tableau e PowerBI.

<a id="link3"></a>
## 3. Instalação
Instalar o MongoDB em uma máquina virtual Ubuntu na versão 20.04, usando o apt

Abra um terminal e execute os comandos
sudo apt-get update
![Screenshot](/images/img01.jpg)
Em seguida
sudo apt-get install mongodb-server
![Screenshot](/images/img02.jpg)
Após a instalçao, editar o arquivo mongodb.conf, para permitir a conexão de qualuquer host
sudo nano /etc/mongodb.conf
![Screenshot](/images/img03.jpg)
![Screenshot](/images/img04.jpg)
Salve o arquivo
Verifique o status do serviço
sudo service mongodb status
![Screenshot](/images/img05.jpg)