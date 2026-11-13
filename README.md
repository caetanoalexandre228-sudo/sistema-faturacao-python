# Sistema de Faturação de uma Loja de Produtos Alimentares

Trabalho prático de Engenharia Informática (3.º ano), desenvolvido em Python.

**Autor:** Alexandre Pedro Zage
**Docente:** Atungulu Kabakaba

## O que o programa faz

- Regista clientes (nome, género, idade, gravidez, deficiência e valor das compras)
- Atribui um bónus de 10% quando o total das compras é superior a 100 000 Kz
- Organiza o atendimento em duas filas: prioritária (grávidas, idosos e pessoas com deficiência) e normal
- Emite a fatura de cada cliente atendido

O bónus depende só do valor das compras e a prioridade depende só da condição da pessoa. As duas regras são independentes.

## Como executar

Com o Python 3 instalado, abre o terminal na pasta do projeto e escreve:

```
python meu_codigo.py
```

Se não funcionar, tenta `python3 sistema_faturacao.py`.

## Menu

1. Registar cliente
2. Ver fila de espera
3. Atender próximo cliente
0. Sair

## Ficheiros

- `sistema_faturacao.py`: código-fonte do programa
- `README.md`: este ficheiro
