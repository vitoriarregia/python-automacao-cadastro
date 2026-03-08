# python-automacao-cadastro
Bot em Python que utiliza PyAutoGUI e Pandas para automatizar o cadastro de produtos em sistemas web a partir de uma base CSV.


# 🤖 Automação de Cadastro de Produtos (Python RPA)

Este projeto automatiza o fluxo de cadastro de produtos em um sistema web, eliminando o trabalho manual repetitivo. O bot realiza o login, processa uma base de dados externa e preenche cada campo do formulário de forma autônoma.

## 📺 Demonstração em Vídeo
Confira o bot em ação realizando o processo completo:

---

## 🚀 Funcionalidades
* **Login Automatizado:** Acessa o portal da empresa e realiza a autenticação.
* **Integração com Dados:** Lê informações de um arquivo `produtos.csv` usando a biblioteca Pandas.
* **Preenchimento Dinâmico:** Cadastra código, marca, tipo, categoria e valores para cada item da lista.
* **Segurança de Interface:** Inclui comandos de scroll e pausas estratégicas para garantir que o sistema processe as informações.

## 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem base.
* **PyAutoGUI**: Responsável pela automação da interface (cliques e teclado).
* **Pandas**: Utilizado para a manipulação eficiente da base de dados.
* **Time**: Para controle de sincronia entre o bot e o navegador.

## 📋 Pré-requisitos
Para rodar este projeto, você precisará instalar as dependências listadas no arquivo `requisitos.txt`:

```bash
pip install -r requisitos.txt
