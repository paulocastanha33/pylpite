# pylpite

# Jogo de Adivinhação de Números [Terminal] em Python

Este é um jogo simples de adivinhação de números, onde o computador gera um número aleatório entre 1 e 100, e o jogador deve adivinhar qual é esse número. O programa informa se o palpite do jogador está muito alto ou muito baixo e conta quantas tentativas foram necessárias até o jogador acertar o número.

## Funcionalidades

1. **Geração de Número Aleatório**:
   - O programa gera um número aleatório entre 1 e 100 utilizando a biblioteca `random`.
   
2. **Interação com o Jogador**:
   - O jogador insere palpites e o programa informa se o número é maior ou menor do que o palpite dado.
   
3. **Contador de Tentativas**:
   - O programa conta quantas tentativas o jogador fez até adivinhar o número corretamente.
   
4. **Mensagem de Finalização**:
   - Quando o jogador acerta o número, o programa exibe uma mensagem parabenizando-o e informando o número de tentativas.

## Como Executar o Jogo

1. Certifique-se de ter o Python instalado no seu sistema. Você pode verificar isso executando o comando:

   ```bash
   python --version

   Faça o download ou clone o repositório com o código do jogo.

2. Execute o arquivo Python diretamente no terminal:

python app.py
O jogo será iniciado e você deverá inserir seus palpites no terminal.

# Requisitos
Python 3.x
Como Funciona o Código
Importar Biblioteca para Gerar Números Aleatórios:

O código utiliza a biblioteca random para gerar um número aleatório entre 1 e 100.
Função adivinhar_numero():

A função principal do jogo, que inicia a lógica de adivinhação e mantém o loop até que o jogador adivinhe o número correto.
Contador de Tentativas:

A variável tentativas mantém o número de tentativas feitas pelo jogador.
Mensagem de Acerto:

Quando o jogador acerta o número, ele recebe uma mensagem de sucesso com o número de tentativas.
Autor
Paulo André Vale Castanha
