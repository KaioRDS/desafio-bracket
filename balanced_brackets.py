
from array import array
from cgitb import text
from itertools import count


def isBalanced(brackets):

    array_open = [];
    #transformando string em array
    array_string = list(brackets)
    open = ["(", "[", "{"]
    array_sociativo = {")":"(", "}":"{","]":"["}

    #percorrendo todos as letras
    for p in array_string:
        #inserir no array vazio os caracteres caso for de abrir
        if p in open:
            array_open.append(p)
        #apagando caracteres se for de fechar
        elif array_open and array_sociativo[p] == array_open[-1]:
            array_open.pop();
        # retornando No caso o caracter abra e não feche
        else:
            return "NO";
    
    return "YES"


if (__name__ == '__main__'):

    print("informe a quantidade de brakets que será inputado");
    # pega a quantidade de brakets que será validado pela função isBalanced
    t = int(input().strip());

    results = []
    for t_itr in range(t):
        print("Agora informe o brakets " , t_itr + 1);
        brackets = input();
        results.append(isBalanced(brackets));

    print(*results, sep='\n')