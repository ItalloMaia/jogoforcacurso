#!/bin/bash
# run.sh - Executa o Jogo da Forca
# Uso: ./run.sh

echo "Iniciando o Jogo da Forca..."
echo ""

# Verifica se o python3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Erro: python3 não encontrado. Instale o Python 3 antes de continuar."
    exit 1
fi

# Executa o script principal
python3 jogo.py
