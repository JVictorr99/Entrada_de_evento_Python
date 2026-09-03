         # versao simples
# idade = 18
# autorizacao = True

# if idade >= 18 or autorizacao:
#   print("Pode entar no evento !")
# else:
#   print("Nao esta autorizado no evento! ")


         # versao melhorada
         
         
#idade = int(input("Digite sua idade: "))
#autorizacao = input("Tem autorizacao dos seus pais? ").upper()

#if idade >= 18 or autorizacao == 'sim':
    # print("Pode entrar! no club a uma area para vips! ")
     
     
    # vip = input("Voce e vip? ").lower()
    # ingresso = input("Tem ingresso ? ").lower()
     
     
    # if vip == 'sim' or ingresso == 'sim':
    #   print("Parabens acesso exclusivo liberado!")
    # else:
    #   print("Esta liberado apenas a area comum do evento!")
       
#else:
#    print("Acesso negado")

            # fazendo teste de if dentro de if #

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode entrar!")

    vip = input("Você é vip? ").lower()
    ingresso = input("Tem ingresso? ").lower()

    if vip == "sim" or ingresso == "sim":
        print("Parabéns! Acesso exclusivo liberado!")
    else:
        print("Está liberado apenas para a área comum do evento!")

else:
    autorizacao = input("Tem autorização dos seus pais? ").lower()

    if autorizacao == "sim":
        print("Pode entrar!")

        vip = input("Você é vip? ").lower()
        ingresso = input("Tem ingresso? ").lower()

        if vip == "sim" or ingresso == "sim":
            print("Parabéns! Acesso exclusivo liberado!")
        else:
            print("Está liberado apenas para a área comum do evento!")

    else:
        print("Acesso negado ao evento!")
