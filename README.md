![Header](https://github.com/user-attachments/assets/0e5667fd-0729-45f2-9cb2-c264dcbc0489)

<a href="https://miro.com/app/board/uXjVIOQp9eM=/?share_link_id=792001140927">
   <img src="https://github.com/user-attachments/assets/d260dd3d-941f-4662-83e6-09d29804a40e" width="300" >
</a>



<a href="">
   <img src="https://github.com/user-attachments/assets/8038ac21-fdf6-4516-b28c-0191b1993a8e" width="300" >
</a>


---
Este repositório contém a solução desenvolvida para o desafio técnico, com o objetivo de demonstrar habilidades em:

- Web scraping com Python 🕷️  
- Transformação e limpeza de dados 🧹  
- Criação e manipulação de banco de dados PostgreSQL 🗃️  
- Desenvolvimento de API com Flask 🔌  
- Criação de uma interface web com Vue.js 🌐  

---

## 🧩 Descrição do Projeto

O desafio teve como objetivo o desenvolvimento de uma aplicação completa capaz de:

1. **Extrair dados da web** utilizando técnicas de web scraping com Python.
2. **Transformar e organizar os dados** extraídos para uso estruturado.
3. **Persistir os dados em um banco de dados relacional (PostgreSQL)**, criando as tabelas e estruturas necessárias.
4. **Elaborar queries analíticas com SQL** para gerar informações relevantes e sumarizadas com base nos dados disponíveis.
5. **Desenvolver uma API REST com Flask**, capaz de acessar dados em um arquivo CSV.
6. **Construir uma interface web em Vue.js** para exibir os dados consultados pela API de forma clara e interativa para o usuário.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.10+**
- **Flask** (API REST)
- **BeautifulSoup / Requests** (Web Scraping)
- **Pandas** (Transformação de dados)
- **SQLAlchemy** (ORM para PostgreSQL)
- **PostgreSQL 10+**

### Frontend
- **Vue.js 3**
- **Axios** (Consumo da API)
- **Vite** (Empacotamento)

---

## 📁 Estrutura do Projeto

Cada uma das pastas contem os desafios divididos em partes seguindo as diretivas do desafio, com os códigos.
Para entender melhor cada parte do cédigo, de maneira visual, aconselho entrar no link do miro, apresentado no inicio.

---

<!---## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/desafio-nivelamento.git
cd desafio-nivelamento
```

### 2. Instalar dependências do backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 3. Iniciar a API Flask
```bash
python app.py
```

### 3. Rodar o frontend
```bash
cd ../frontend
npm install
npm run dev
```

--->

## 🔎 Funcionalidades Implementadas

- 🔍 Busca por registros via interface (consumindo o CSV ou banco)
- 📊 Visualização dos dados estruturados
- 📥 Extração de informações via scraping automatizado
- 🔄 Atualização e ingestão de dados no PostgreSQL
- 🔐 Arquitetura separada por camadas (scraper, API, frontend)

