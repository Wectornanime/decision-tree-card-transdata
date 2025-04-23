# decision-tree-card-transdata

<!-- PROJECT SHIELDS -->
<div align="center">
  <img src="https://img.shields.io/github/contributors/wectornanime/decision-tree-card-transdata.svg?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/wectornanime/decision-tree-card-transdata.svg?style=for-the-badge" />
  <img src="https://img.shields.io/github/v/release/wectornanime/decision-tree-card-transdata?style=for-the-badge" />
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumario</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto-">Sobre o projeto</a>
      <ul>
        <li><a href="#análise-e-treinamento-de-modelos">Análise e treinamento de modelos</a></li>
        <li><a href="#api">API</a></li>
        <li><a href="#frontend">Frontend</a></li>
      </ul>
    </li>
    <li>
      <a href="#como-rodar-o-projeto-️">Como rodar o projeto</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#deploy-da-aplicação-dash">Deploy da aplicação</a></li>
    <li><a href="#desenvolvedorescontribuintes-octocat">Desenvolvedores/Contribuintes</a></li>
    <li><a href="#licença-️">Licença</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Sobre o projeto 📝
Este projeto tem como objetivo detectar possíveis fraudes em transações de cartão de crédito utilizando técnicas de aprendizagem de máquina. Através de um modelo de predição treinado com dados de um [dataset do kaggle](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud), o sistema é capaz de classificar se uma transação é legítima ou fraudulenta com base em suas características.

A aplicação está dividida em três momentos:
<br>✔️ [Análise e treinamento de modelos](#análise-e-treinamento-de-modelos)
<br>✔️ [API para o uso do modelo preditivo](#api)
<br>✔️ [Frontend para consumo da API](#frontend)


### Análise e treinamento de modelos
Aqui foi realizado o carregamento, a análise e o tratamento dos dados usando o pandas, foi escolho 4 modelos de classificação, _Random Forest_, _Tree Classifier_, _KNN_ e _Nave Bayes_, que interagiram com a base de dados afim de obter o modelo com a melhor performance, nesse cenário o _Random Forest_ se saiu melhor, e foi então exportado como modelo usando o joblib.

### API
Foi feito uma API Restful usando python para usar o modelo exportado para fazer as predições, a API foi feita usando o _FastApi_, os dados enviados para fazer predições foram armazenadas no _Firestore Database_ do _Firebase_.

### Frontend
A plicação conta com um frontend feito em react para consumir a API, através de um formulário simples separado em partes, além de um dashboard para visualizar os dados.


<!-- GETTING STARTED -->
## Como rodar o projeto 🕹️
### Pré-requisitos
✔️ **Treinamento e API:** Para rodar o notebook do jupyter do treinamento dos modelos e a API, será preciso ter o [Python](https://www.python.org/) instalado na máquina.
<br>✔️ **Front:** Para rodar o frontend da aplicação, será preciso ter o [NodeJs](https://nodejs.org/en) instalado na máquina.

### Instalação
1. Faça o clone do repositório:
```sh
git clone https://github.com/Wectornanime/decision-tree-card-transdata.git
```
1. Firebase:
    1. Entre no site do Firebase: [`https://console.firebase.google.com/`](https://console.firebase.google.com/).
    1. Crie um projeto ou abra um já criado.
    1. Certifique-se que o banco de dados `Firestore` já foi criado.
    1. Gere uma chave da aplicação:
        1. `Configurações do projeto` > `Contas de serviço` > `Gerar nova chave privada`
            1. Será gerado um json
    1. Adicione a chave ao `.env`
        1. Na raiz do projeto deve haver um `.env` com o seguinte conteúdo:
            ```
            MODEL_FILE_ID=#id do google drive do arquivo do modelo
            FIREBASE_CREDENCIAL_JSON=#credenciais do firebase em formato json em linha unica
            ```
1. API (Na raiz do projeto):
    1. Instale as dependências da API:
        ```sh
        pip install -r requirements.txt
        ```
    1. Execute o backend (em modo de desenvolvimento):
        ```sh
        fastapi dev api/main.py
        ```
        1. Será aberto um serviço do fastapi na porta `8000`
    1. Adicione o host da API no `.env` do front:
        1. No diretório `client/` deve haver um `.env` com o seguinte conteúdo:
            ```
            VITE_API_URL=#url do servidor backend
            ```
1. Front (No diretório `client/` da aplicação):
    1. Instale as dependências do front:
        ```sh
        npm install
        ```
    1. Execute o frontend (em modo de desenvolvimento):
        ```sh
        npm run dev
        ```
        1. Será aberto um serviço do vite na porta `5173`


<!-- DEPLOY APPLICATION -->
## Deploy da aplicação :dash:
🔗Swagger: [https://decision-tree-card-transdata.onrender.com/docs](https://decision-tree-card-transdata.onrender.com/docs)
<br>🔗Fontend: [https://fraudedeteccao.netlify.app/](https://fraudedeteccao.netlify.app/)

<!-- DEVELOPERS -->
## Desenvolvedores/Contribuintes :octocat:

| [<img src="https://github.com/liad4ntas.png" width=115><br><sub>Anna Cecilia</sub>](https://github.com/liad4ntas) | [<img src="https://github.com/heldhma.png" width=115><br><sub>Heldhma Luiza</sub>](https://github.com/heldhma) | [<img src="https://github.com/heijsilva.png" width=115><br><sub>João Vitor Silva</sub>](https://github.com/heijsilva) | [<img src="https://github.com/MariliaCarv.png" width=115><br><sub>Marília Carvalho</sub>](https://github.com/wectornanime) | [<img src="https://github.com/wectornanime.png" width=115><br><sub>Wectornanime Felipe</sub>](https://github.com/wectornanime) |
| :---: | :---: | :---: | :---: | :---: |

## Licença ⚖️

The [MIT License](LICENSE) (MIT)

Copyright :copyright: 2025 - decision-tree-card-transdata
