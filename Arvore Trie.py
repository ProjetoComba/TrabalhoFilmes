from typing import Tuple


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str, movieid=0):
        self.char = char
        self.children = []
        self.movieid = 0
        self.word_finished = False
        self.counter = 1


def add(root, word: str, movieid: int):

    node = root
    for char in word:
        print("char in word :", char)
        found_in_child = False

        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child

                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)

            node = new_node

    node.movieid = movieid # Adiciona o campo movieID no ultimo caracter adicionado na arvore trie
    node.word_finished = True


def find_prefix(root, prefix: str):

    node = root

    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True

        for child in node.children:
            if child.char == char:

                char_not_found = False

                node = child
                break

        if char_not_found:
            return False, 0


    return True, node


def acha_o_resto (node, achados):

    for child in node.children:
        if (child.counter == 1) and (child.word_finished == True):
            break
        if (child.counter != 0 ):
            aux = acha_o_resto(child, achados)
            if aux != None:
                achados.append(aux)
    return child.movieid


if __name__ == "__main__":
    root = TrieNode('*')
    tupla = ()
    achados= []
    add(root, 'Star Wars: Episode V', 1196)
    add(root, "Star Wars: Episode IV", 260)

    add(root, 'loucura', 2222)
    add(root, 'loucurada 2', 2220)

    tupla =(find_prefix(root, 'loucu'))
    if tupla[0] == True:
        acha_o_resto(tupla[1], achados)

    print(achados)
