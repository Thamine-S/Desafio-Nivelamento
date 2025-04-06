<script setup>
import { ref } from "vue";
import axios from "axios";

const termo = ref("");
const operadoras = ref([]);

const buscar = async () => {
  if (!termo.value) return;
  
  try {
    const response = await axios.get(`http://127.0.0.1:5000/buscar?q=${termo.value}`);
    operadoras.value = response.data;
  } catch (error) {
    console.error("Erro na requisição", error);
  }
};
</script>

<template>
  <div class="container">
    <h1>Buscar</h1>
    <input v-model="termo" placeholder="Digite o nome da operadora"/>
    <button @click="buscar"><ion-icon name="search-outline"></ion-icon></button>

    <ul v-if="operadoras.length">
  <li v-for="(op, index) in operadoras" :key="index">
    <strong class="title">{{ op.Razao_Social || 'Nome não disponível' }}</strong>  <br>
    - Nome Fantasia: {{ op.Nome_Fantasia || 'Nome Fantasia não disponível' }} <br>
    - Modalidade: {{ op.Modalidade || 'Modalidade não disponível' }} <br>
    - Endereço:  {{ op.Logradouro || 'Logradouro não disponível' }} - n° {{ op.Numero || 'Número não disponível' }} - Bairro {{ op.Bairro || 'Bairro não disponível' }} <br>
    - Cidade: {{ op.Cidade || 'Cidade não disponível' }} <br>
    - Telefone: (+{{ op.DDD || 'DDD não disponível' }}) {{ op.Telefone || 'Telefone não disponível' }} <br>
    - Email: {{ op.Endereco_eletronico || 'Email não disponível' }} <br>
  </li>

</ul>

  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap');

body{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(5, 1fr);
    gap: 8px;
}

.container {
  margin-top: 100px;
  grid-column: span 2 / span 2;
    grid-row: span 3 / span 3;
    grid-column-start: 3;
  text-align: center;
}

.container h1 {
  margin: 100px;
  font-size: 50px;
  font-family: "Orbitron", sans-serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}


input {
  margin-bottom: 50px;
  border: none;
  padding: 8px;
  margin-right: 5px;
}
button {
  margin-bottom: 50px;
  border: none;
  padding: 8px;
  cursor: pointer;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background-color: rgb(226, 226, 226);
  border-radius: 20px;
  margin: 10px 0;
  color: black;
}
.title{
  margin: 10px;
  font-size: medium;
  font-weight: 700;
}

ion-icon {
  color: rgb(0, 0, 0);
}

</style>

