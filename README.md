Aqui está um **README profissional e pronto para GitHub**, baseado no padrão de projetos de sistema bancário em Python com POO (como os desafios comuns da DIO, que envolvem operações como depósito, saque e extrato ([DIO][1])).

Você pode copiar e colar direto no seu repositório 👉 Desafio_Python_POO

---

# 💰 Sistema Bancário com POO em Python

Projeto desenvolvido com o objetivo de aplicar os conceitos de **Programação Orientada a Objetos (POO)** em Python, simulando um sistema bancário simples via terminal.

---

## 🚀 Funcionalidades

* ✅ Criar usuário
* ✅ Criar conta bancária
* ✅ Realizar depósitos
* ✅ Realizar saques com regras (limite e quantidade)
* ✅ Exibir extrato
* ✅ Listar contas cadastradas

---

## 🧠 Conceitos Aplicados

Este projeto foi construído com foco em boas práticas de desenvolvimento utilizando:

* 🔹 **Encapsulamento**
* 🔹 **Herança**
* 🔹 **Polimorfismo**
* 🔹 **Abstração**
* 🔹 Organização em classes e métodos

---

## 🏗️ Estrutura do Projeto

```bash
📁 Desafio_Python_POO
│
├── main.py              # Arquivo principal (execução)
├── classes/             # Classes do sistema
│   ├── cliente.py
│   ├── conta.py
│   ├── transacoes.py
│
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.8+

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/abdieldeathayde/Desafio_Python_POO.git
```

2. Acesse a pasta:

```bash
cd Desafio_Python_POO
```

3. Execute o projeto:

```bash
python main.py
```

---

## 💻 Exemplo de Uso

```bash
=============== MENU ================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo usuário
[0] Sair
====================================
```

---

## 📌 Regras de Negócio

* O sistema permite **até 3 saques por dia**
* Existe um **limite máximo por saque**
* O extrato mostra todas as movimentações
* Não é possível sacar valores maiores que o saldo

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte de estudos em Python para:

* Praticar lógica de programação
* Aplicar conceitos de POO na prática
* Simular um sistema real (banco)
* Evoluir para projetos mais complexos

---

## 📈 Melhorias Futuras

* 🔄 Interface gráfica (GUI)
* 🌐 API REST com Flask ou FastAPI
* 🗄️ Integração com banco de dados
* 🔐 Sistema de autenticação

---

## 👨‍💻 Autor

**Abdiel de Athayde**

* 💼 Desenvolvedor Backend Java
* 🎓 Estudante de Análise e Desenvolvimento de Sistemas
* 🔗 LinkedIn: [https://www.linkedin.com/in/abdieldeathayde](https://www.linkedin.com/in/abdieldeathayde)

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

[1]: https://www.dio.me/articles/desafio-sistema-bancario-otimizado-com-python?utm_source=chatgpt.com "Desafio Sistema Bancário Otimizado Com Python | Valdemar Taborda | GitHub | Git | Python | DIO"
