playlist = []

while True:
    print("\n=== Spotify da Sala ===")
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Buscar música")
    print("4 - Remover música")
    print("5 - Informações da playlist")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome da música: ")
        artista = input("Artista: ")

        musica = {
            "nome": nome,
            "artista": artista
        }

        playlist.append(musica)

        print("Música adicionada!")

    elif opcao == "2":

        if len(playlist) == 0:
            print("Playlist vazia.")
        else:
            print("\n=== Playlist ===")

            for i, musica in enumerate(playlist, start=1):
                print(
                    f"{i}. {musica['nome']} - {musica['artista']}"
                )

    elif opcao == "3":

        busca = input("Digite o nome da música: ")

        encontrada = False

        for musica in playlist:

            if busca.lower() in musica["nome"].lower():

                print(
                    f"Encontrada: {musica['nome']} - "
                    f"{musica['artista']}"
                )

                encontrada = True

        if not encontrada:
            print("Música não encontrada.")

    elif opcao == "4":

        nome = input("Qual música deseja remover? ")

        removida = False

        for musica in playlist:

            if musica["nome"].lower() == nome.lower():

                playlist.remove(musica)

                print("Música removida!")

                removida = True

                break

        if not removida:
            print("Música não encontrada.")

    elif opcao == "5":

        print("\n=== Estatísticas ===")

        print(f"Total de músicas: {len(playlist)}")

        artistas = []

        for musica in playlist:

            if musica["artista"] not in artistas:
                artistas.append(musica["artista"])

        print(f"Total de artistas: {len(artistas)}")

    elif opcao == "0":

        print("Até logo!")
        break

    else:

        print("Opção inválida.")