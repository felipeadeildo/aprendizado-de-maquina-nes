# 📘 NES Machine Learning Exercises

Este repositório contém as soluções das listas de exercícios do curso de Machine Learning do NES, baseado no livro **Learning from Data** de Abu Mostafa. Cada exercício foi implementado e estruturado para facilitar a execução e a análise, seguindo as melhores "boas práticas" de desenvolvimento.

## 📝 Descrição

O objetivo deste repositório é oferecer soluções detalhadas para as listas de exercícios do curso de Machine Learning. O código foi escrito em Python e pode ser executado diretamente da linha de comando, permitindo repetir as execuções com diferentes configurações para fins de estudo e experimentação.

## 📂 Estrutura do Repositório

A estrutura atual do repositório é a seguinte:

```
├── constants.py          // 📌 Arquivo de constantes
├── LICENSE               // 📜 Licença
├── linear_regression.py  // 📉 Algoritmo de Regressão Linear
├── listaK                // 📚 Lista K de exercícios (classroom)
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── ...
│   └── exercicioN.py
├── main.py               // 🚀 Script principal para execução dos exercícios
├── perceptron.py         // 🤖 Algoritmo Perceptron
├── README.md
└── utils.py              // 🛠️ Utilitários usando Python built-in functions.
```

### 📋 Exercícios (atualmente)

- **Lista 2:**
  - `exercicio6.py`: Implementação do exercício 6 (hw1)
  - `exercicio7.py`: Implementação do exercício 7 (hw1)
  - `exercicio8.py`: Implementação do exercício 8 (hw1)
  - `exercicio8_2.py`: Implementação do exercício 8 (hw2)
  - `exercicio9.py`: Implementação do exercício 9 (hw2)

## 🛠️ Instruções de Execução

Para executar qualquer exercício, utilize o script `main.py`. Você pode especificar qual lista e exercício deseja rodar, além de outras opções adicionais.

### ⚙️ Exemplos de Comandos

1. **Executar um exercício específico:**

   ```bash
   python main.py --list 2 --exercise 6
   ```

   Isso executará o exercício 6 da lista 2.

2. **Executar um exercício com múltiplas repetições:**

   ```bash
   python main.py --list 2 --exercise 7 --repetitions 5
   ```

   Isso executará o exercício 7 da lista 2 cinco vezes.

3. **Executar um exercício limpando a tela antes de cada execução:**

   ```bash
   python main.py --list 2 --exercise 8 --clear
   ```

   Isso executará o exercício 8 da lista 2, limpando a tela antes de cada execução.

## 🔍 Como Funciona

1. **Parâmetros:**

   - `--list` (`-l`): Número da lista de exercícios (obrigatório).
   - `--exercise` (`-e`): Número do exercício na lista (obrigatório).
   - `--repetitions` (`-r`): Quantidade de vezes que o exercício deve ser executado (opcional, padrão: 1).
   - `--clear` (`-c`): Limpa a tela antes de cada execução (opcional).

2. **Fluxo de Execução:**
   - O script `main.py` processa os argumentos da linha de comando.
   - O módulo do exercício especificado é importado dinamicamente.
   - O exercício é executado o número de vezes especificado, com as instruções sendo exibidas antes de cada execução.

## ✍️ Autor

Desenvolvido por **Felipe Adeildo**.

- [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/felipeadeildo)
- [![Telegram](https://img.shields.io/badge/-Telegram-2CA5E0?style=for-the-badge&logo=Telegram&logoColor=white)](https://t.me/felipeadeildo)
- [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@felipeadeildo)

Sinta-se à vontade para entrar em contato ou acompanhar meus outros projetos!
