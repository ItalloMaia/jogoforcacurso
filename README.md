# 🎮 Jogo da Forca - Edição Cultura Nortista

Um jogo da forca simples, feito em Python, rodando direto no terminal. As palavras são todas ligadas à cultura do Pará e do Maranhão (Círio, Carimbó, Tacacá, Belém, São Luís, entre outras).

## 📁 Estrutura do projeto

```
jogo-forca/
├── jogo.py      # Código principal do jogo (Python)
├── run.sh       # Script para executar o jogo facilmente
└── README.md    # Este arquivo
```

---

## ▶️ Como executar o arquivo .sh

O arquivo `run.sh` foi criado para facilitar a execução do jogo sem precisar digitar o comando Python toda vez.

### Passo 1 - Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/jogo-forca.git
cd jogo-forca
```

### Passo 2 - Dar permissão de execução ao script (necessário apenas uma vez)

```bash
chmod +x run.sh
```

### Passo 3 - Executar

```bash
./run.sh
```

Se tudo estiver certo, o jogo vai iniciar direto no terminal.

> **Observação:** é necessário ter o **Python 3** instalado na máquina. O próprio script `run.sh` verifica isso e avisa caso não encontre o Python.

### Alternativa (rodar sem o .sh)

Caso prefira, também é possível rodar direto com:

```bash
python3 jogo.py
```

---

## 🧠 Explicação do código Python (`jogo.py`)

O jogo é dividido em algumas partes principais:

### 1. `ESTAGIOS`
Uma lista com 7 desenhos em ASCII art representando o "boneco da forca" sendo montado aos poucos. O índice da lista corresponde à quantidade de erros do jogador (0 erros = forca vazia, 6 erros = boneco completo = derrota).

### 2. `PALAVRAS`
Uma lista de tuplas no formato `(palavra, dica)`. Cada tupla contém a palavra a ser adivinhada e uma dica relacionada à cultura nortista. Isso facilita adicionar novas palavras no futuro: basta acrescentar uma nova tupla na lista.

### 3. `escolher_palavra()`
Sorteia aleatoriamente uma das tuplas da lista `PALAVRAS`, usando `random.choice()`.

### 4. `mostrar_palavra(palavra, letras_corretas)`
Monta a exibição da palavra na tela, mostrando as letras já acertadas e substituindo por `_` as letras ainda não descobertas.

### 5. `jogar()`
É a função principal, que controla o **loop do jogo**:
- Escolhe a palavra e mostra a dica;
- Exibe o estado atual da forca e da palavra;
- Recebe a letra digitada pelo jogador;
- Valida a entrada (precisa ser uma única letra);
- Verifica se a letra está na palavra:
  - Se sim, adiciona ao conjunto de `letras_corretas`;
  - Se não, adiciona ao conjunto de `letras_erradas` e soma um erro;
- Repete até o jogador **acertar toda a palavra** (vitória) ou **errar 6 vezes** (derrota - `while...else`);
- Ao final, pergunta se o jogador quer jogar novamente (chamando `jogar()` de novo, de forma recursiva).

### 6. Bloco final
```python
if __name__ == "__main__":
    jogar()
```
Garante que a função `jogar()` só é executada quando o arquivo é rodado diretamente (e não quando é importado por outro script).

---

## 🚀 Próximos passos (ideias de melhoria)

- Adicionar um placar de vitórias/derrotas;
- Permitir escolher o tema das palavras (Pará, Maranhão, geral);
- Colorir a saída do terminal (usando a lib `colorama`);
- Criar um modo multiplayer (um jogador escolhe a palavra para o outro).

---

## 📄 Licença

Este projeto é livre para uso, estudo e modificação.
