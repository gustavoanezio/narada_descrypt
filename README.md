# 🔐 Simples Criptografia em Python

Este projeto implementa um esquema de criptografia e descriptografia utilizando manipulação binária e codificação Base64. O processo envolve operações simples, como inversão de bits, reversão da sequência e aplicação de um vetor fixo de XOR. Ele fez parte do processo seletivo para estágio da empresa de infosec Tempest.

O código em narada.py serve para realizar a criptografia e em desc_narada.py para reverter.
Todos os créditos para a Tempest pelo Narada, eu apenas realizei a reversão da criptografia.

## Como Funciona?

### 🔒 Processo de Criptografia

A criptografia segue os seguintes passos:

Converter a string em binário ➝ Cada caractere da string original é convertido em sua representação binária de 8 bits.

Inverter os bits ➝ Cada 0 vira 1 e vice-versa.

Reverter a string binária ➝ A sequência dos bits é invertida.

Aplicar XOR com um vetor fixo ➝ Uma operação XOR é aplicada entre a string binária e um vetor fixo predefinido para adicionar segurança.

Converter o binário resultante para Base64 ➝ O resultado é codificado em Base64 para facilitar o armazenamento e a transmissão.

### 🔓 Processo de Descriptografia

A descriptografia reverte as operações da criptografia na ordem inversa:

Converter Base64 para binário ➝ A string criptografada é decodificada de Base64 para binário.

Desfazer o XOR ➝ O mesmo vetor fixo é aplicado novamente para recuperar os dados originais.

Reverter a inversão da string ➝ A sequência dos bits é restaurada.

Reverter a inversão dos bits ➝ Os bits são invertidos novamente para recuperar o texto binário original.

Converter binário para string ➝ O texto binário é convertido de volta para caracteres legíveis.

## 🛠️ Como Executar?

Clone este repositório:
```
git clone https://github.com/gustavoanezio/narada_decrypt.git
```
Navegue até o diretório do projeto:
```
cd seu-repositorio/
```
Execute o script:

```python3 narada.py``` para executar o software de criptografia ou
```python3 desc_narada.py``` para o processo de reversão.

Insira a string criptografada em Base64 quando solicitado.

O script irá criptografar ou descriptografar e exibir o texto.

## ⚠️ Observação

Este método de criptografia é didático e não deve ser usado para segurança real, pois um atacante pode reverter facilmente as operações. Para aplicações seguras, recomenda-se o uso de algoritmos robustos, como AES ou RSA.
