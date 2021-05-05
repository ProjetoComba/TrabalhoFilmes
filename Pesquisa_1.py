import Busca_Nome

def pesquisaMovie(nome, root, HashTableMovies, HashTableMediaCount):
    achados = []

    tupla = (Busca_Nome.find_prefix(root, nome))

    if tupla[0] == True:
        Busca_Nome.acha_o_resto(tupla[1], achados)

    achados = sorted(set(achados))

    for id in achados:
        print(f"{id}, {' , '.join(map(str, HashTableMovies[id]))} , {' , '.join(map(str, HashTableMediaCount[id]))}")
