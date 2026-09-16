# 📁 05: Encapsulamento e Polimorfismo na Orientação a Objetos

Este módulo consolida o ecossistema de gerenciamento de imóveis, aplicando conceitos de proteção de dados (Encapsulamento) e reescrita de comportamentos dinâmicos (Polimorfismo).

## 🧠 Conceitos Chave da Aula

*   **Encapsulamento:** É a técnica de esconder os detalhes internos de um objeto para protegê-lo de alterações indevidas. No código, os atributos foram protegidos com o prefixo `_` (como `_nome`) e o acesso a eles foi controlado de forma segura utilizando os decoradores `@property` (para leitura) e `.setter` (para alteração).
*   **Polimorfismo:** É a capacidade de classes filhas diferentes responderem ao mesmo método de formas diferentes. No código, isso é demonstrado no método `calcularImposto()`. Enquanto a casa usa o imposto padrão de 2%, o imóvel comercial reescreve esse comportamento para calcular o imposto dinamicamente baseado na UF (`DF`, `SP`, `RJ`).

## 🚀 Arquivos da Aula

*   **`imoveis.py`**: Código que integra todas as regras de negócios da aula, contendo a estrutura com classes abstratas, herança múltipla, controle de acesso a atributos e regras polimórficas por estado.

---
*Estudos desenvolvidos durante as aulas de fundamentos de programação.*
