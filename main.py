# Variáveis globais
end = False

# Aqui iniciamos o nosso programa
def main(): # Recomendável para evitar um possível loop infinito
    global end  # Essa função inclui a global no loop while
    while not end:
        # Irá imprimir a mensagem escrita na tela do usuário
        print("""
Escolha uma entrada:
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão;
0 - Encerrar o programa""")
        
        # Avalia a entrada do usuário. Não é obrigatório tê-lo em seu programa, contudo é recomendável
        try:
            variavel_de_entrada = int(input("Digite a sua escolha: "))  # Semelhante ao 'print', porém é usado para o usuário inserir uma entrada
            print() # Apenas um espaço em branco. Usando apenas para criar um espaço entre uma linha e outra (opcional)
            
            # Compara a entrada do usuário e chama a função solicitada
            if variavel_de_entrada == 1:    # Chama a função 'adição'
                numero_um = float(input("Digite o primeiro número: "))
                numero_dois = float(input("Digite o segundo número: "))
                print(f"A soma entre {numero_um} e {numero_dois} é", numero_um + numero_dois)
                
            elif variavel_de_entrada == 2:  # Chama a função 'subtração'
                numero_um = float(input("Digite o primeiro número: "))
                numero_dois = float(input("Digite o segundo número: "))
                print(f"A subtração de {numero_um} por {numero_dois} é", numero_um - numero_dois)
                
            elif variavel_de_entrada == 3:  # Chama a função 'multiplicação'
                numero_um = float(input("Digite o primeiro número: "))
                numero_dois = float(input("Digite o segundo número: "))
                print(f"A multiplicação de {numero_um} pelo múmero {numero_dois} é", numero_um * numero_dois)
                
            elif variavel_de_entrada == 4:  # Chama a função 'divisão'
                try:
                    numero_um = float(input("Digite o primeiro número: "))
                    numero_dois = float(input("Digite o segundo número: "))
                    print(f"A divisão de {numero_um} pelo número {numero_dois} é", numero_um / numero_dois)
                except ZeroDivisionError:  # Informa o usuário caso ele tente realizar a divisão por 0
                    print("Não é permitido divisões por 0")
            
            elif variavel_de_entrada == 0:  # Chama a função 'encerrar programa'
                print("Programa encerrado...\nPrecione 'ENTER' para fechar a janela")
                input()  # Não obrigatório, porém recomendo usá-lo caso deseje executá-lo no terminal
                end = True # Função
            
            else:   # Exibe uma mensagem ao usuário caso ele insira um número fora do intervalo de 0 a 4
                print("Por favor, insira apenas números dentro do intervalo de 0 a 4")
                
        except ValueError:
            print("Por favor, insira apenas números e evite espaços em branco")
            
main()  # Encerra o loop
