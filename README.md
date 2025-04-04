# 🚀 Desafio de Nivelamento – Intuitive Care

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
4. **Desenvolver uma API REST com Flask**, capaz de acessar dados em um arquivo CSV.
5. **Construir uma interface web em Vue.js** para exibir os dados consultados pela API de forma clara e interativa para o usuário.

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



---

## 🚀 Como Executar o Projeto

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

---

## 🔎 Funcionalidades Implementadas

- 🔍 Busca por registros via interface (consumindo o CSV ou banco)
- 📊 Visualização dos dados estruturados
- 📥 Extração de informações via scraping automatizado
- 🔄 Atualização e ingestão de dados no PostgreSQL
- 🔐 Arquitetura separada por camadas (scraper, API, frontend)

---

## 💬 Considerações Finais

Esse desafio foi uma excelente oportunidade de aplicar conhecimentos práticos em todo o ciclo de desenvolvimento de uma aplicação fullstack orientada a dados. As etapas de scraping, limpeza, persistência, API e exibição foram fundamentais para consolidar a integração entre backend e frontend com foco em dados reais.

---
