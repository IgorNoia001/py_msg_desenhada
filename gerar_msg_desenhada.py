def desenhar_mensagem(mensagem):
    linhas = []
    
    # Tamanho da "caixa" para cada letra
    largura_letra = 7
    altura_letra = 7

    # Mapeamento básico de letras para o "formato" com espaços
    letras = {
        '|': [
            "###########",
            "###########",
            "###########",
            "###########",
            "###########",
            "###########",
            "###########"
        ],
        'A': [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ######### ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## "
        ],
        'B': [
            " #######   ",
            " ##     ## ",
            " ##     ## ",
            " #######   ",
            " ##     ## ",
            " ##     ## ",
            " #######   "
        ],
        'C': [
            "  #######  ",
            " ##        ",
            " ##        ",
            " ##        ",
            " ##        ",
            " ##        ",
            "  #######  "
        ],
        'D': [
            " #######   ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " #######   "
        ],
        'E': [
            " ######## ",
            " ##       ",
            " ##       ",
            " #######  ",
            " ##       ",
            " ##       ",
            " ######## "
        ],
        'F': [
            " ######## ",
            " ##       ",
            " ##       ",
            " #######  ",
            " ##       ",
            " ##       ",
            " ##       "
        ],
        'G': [
            "  ####### ",
            " ##       ",
            " ##       ",
            " ##   ####",
            " ##     ##",
            " ##     ##",
            "  ####### "
        ],
        'H': [
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " #########",
            " ##     ##",
            " ##     ##",
            " ##     ##"
        ],
        'I': [
            "  ####### ",
            "     ##   ",
            "     ##   ",
            "     ##   ",
            "     ##   ",
            "     ##   ",
            "  ####### "
        ],
        'J': [
            "      ### ",
            "       ## ",
            "       ## ",
            "       ## ",
            " ##    ## ",
            " ##    ## ",
            "  ######  "
        ],
        'K': [
            " ##    ## ",
            " ##   ##  ",
            " ## ##    ",
            " ####     ",
            " ## ##    ",
            " ##   ##  ",
            " ##    ## "
        ],
        'L': [
            " ##       ",
            " ##       ",
            " ##       ",
            " ##       ",
            " ##       ",
            " ##       ",
            " ######## "
        ],
        'M': [
            " ##     ##",
            " ###   ###",
            " ## # # ##",
            " ##  #  ##",
            " ##     ##",
            " ##     ##",
            " ##     ##"
        ],
        'N': [
            " ##     ##",
            " ###    ##",
            " ## #   ##",
            " ##  #  ##",
            " ##   # ##",
            " ##    ###",
            " ##     ##"
        ],
        'O': [
            "  ####### ",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            "  ####### "
        ],
        'P': [
            " #######  ",
            " ##     ##",
            " ##     ##",
            " #######  ",
            " ##       ",
            " ##       ",
            " ##       "
        ],
        'Q': [
            "  ####### ",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##   # ##",
            " ##    ###",
            "  ####### "
        ],
        'R': [
            " #######  ",
            " ##     ##",
            " ##     ##",
            " #######  ",
            " ##   ##  ",
            " ##    ## ",
            " ##     ##"
        ],
        'S': [
            "  ####### ",
            " ##       ",
            " ##       ",
            "  ####### ",
            "       ## ",
            "       ## ",
            " #######  "
        ],
        'T': [
            " #########",
            "    ##    ",
            "    ##    ",
            "    ##    ",
            "    ##    ",
            "    ##    ",
            "    ##    "
        ],
        'U': [
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            "  ####### "
        ],
        'V': [
            " ##     ##",
            " ##     ##",
            " ##     ##",
            " ##     ##",
            "  ##   ## ",
            "   ## ##  ",
            "    ###   "
        ],
        'W': [
            " ##     ##",
            " ##     ##",
            " ##  #  ##",
            " ##  #  ##",
            " ## # # ##",
            " ###   ###",
            " ##     ##"
        ],
        'X': [
            " ##     ##",
            "  ##   ## ",
            "   ## ##  ",
            "    ###   ",
            "   ## ##  ",
            "  ##   ## ",
            " ##     ##"
        ],
        'Y': [
            " ##     ##",
            "  ##   ## ",
            "   ## ##  ",
            "    ###   ",
            "     ##   ",
            "     ##   ",
            "     ##   "
        ],
        'Z': [
            " ######## ",
            "      ##  ",
            "     ##   ",
            "    ##    ",
            "   ##     ",
            "  ##      ",
            " ######## "
        ],
        ' ': [
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "          "
        ]
    }

    
    # Mapeamento de caracteres especiais
    caracteres_especiais = {
        '$<3%': [
            "  ##    ##  ",
            " ####  #### ",
            "############",
            "  ########  ",
            "   ######   ",
            "    ####    ",
            "     ##     "
        ],
        '$$%': [  # Novo caractere especial: cifrão
            "   ######  ",
            " ##  ##  ##",
            " ##  ##    ",
            "  #######  ",
            "     ##  ## ",
            " ##  ##  ##",
            "   ######  "
        ],
        # Adicione mais caracteres especiais aqui
    }

    
    # Construção das linhas da mensagem
    for linha in range(altura_letra):
        linha_texto = ""
        i = 0
        while i < len(mensagem):
            if mensagem[i] == '$':  # Verifica se o caractere de início de código está presente
                # Procura pelo final do código
                codigo_fim = mensagem.find('%', i)
                if codigo_fim != -1:  # Se encontrou o final do código
                    codigo = mensagem[i:codigo_fim + 1]
                    if codigo in caracteres_especiais:
                        linha_texto += caracteres_especiais[codigo][linha] + "  "  # Adiciona o caractere especial
                        i = codigo_fim + 1  # Move o índice para depois do código
                        continue
            
            char = mensagem[i].upper()
            if char in letras:
                linha_texto += letras[char][linha] + "  "  # Espaço entre letras
            else:
                linha_texto += "#" * largura_letra + "  "  # Caractere não mapeado
            i += 1  # Avança para o próximo caractere
        linhas.append(linha_texto)

    # Determina o comprimento da linha mais longa
    largura_texto = max(len(linha_texto)-2 for linha_texto in linhas)

    # Exibir as duas linhas superiores de #
    print("#" * largura_texto)
    print("#" * largura_texto)

    # Exibir a mensagem formatada
    for linha in linhas:
        print(linha)

    # Exibir as duas linhas inferiores de #
    print("#" * largura_texto)
    print("#" * largura_texto)

# Mensagem de entrada
mensagem = input("Digite a mensagem: ")
desenhar_mensagem(mensagem)