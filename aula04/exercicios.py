from typing import Union

def classificacao_numero(numero: Union[int, float]) -> str:
    if numero < 0.0:
        return "negativo"
    else:
        return "positivo"


def exercicio() -> None:
    """
    Este desafio tem como objetivo calcular o valor bônus recebido por uma pessoa em cima de seu salário mensal.
    É preciso informar o nome, em seguida será solicitado o salário e o bônus percentual a ser calculado.

    A fórmula de cálculo é 1.000,00 + (salário * bônus).

    É possível cancelar a operação pressionando ctrl + c a qualquer momento.
    """
    while True:
        try:
            nome: str = input("Olá, por favor informe seu nome: ").strip()
            if len(nome) == 0:
                raise UserWarning("Você deve informar um nome.")
            elif any(char.isdigit() for char in nome):
                raise UserWarning("O nome não pode conter números ou caracteres especiais.")

            while True:
                try:
                    salario: float = float(input("Informe seu salário mensal (exemplo: 3200.0): ").strip())
                    if classificacao_numero(salario) == "negativo":
                        raise UserWarning("O salário não pode ser um número negativo.")

                    porcentagem_bonus: float = float(input("Agora informe o bônus (entre 0.0 a 100.0): ").strip())
                    if porcentagem_bonus < 0.0 or porcentagem_bonus > 100:
                        raise UserWarning("O bônus deve ser entre 0 e 100.")
                except ValueError:
                    print("Você deve informar um número decimal.")
                except UserWarning as e:
                    print(e)
                else:
                    break

            bonus: float = 1_000 + salario * (porcentagem_bonus / 100)
            print(f"Olá, {nome}. Seu bônus neste ano é de {bonus:.2f}, totalizando {salario + bonus:.2f}.")
        except UserWarning as e:
            print(e)
        except KeyboardInterrupt:
            print("\n", "Saindo...", sep="")
            break
        else:
            break


def exercicio01() -> None:
    numeros: list[int] = [i for i in range(1, 11)]
    # Usando map
    # list(map(lambda numero: print(numero ** 2), numeros))

    # Usando list comprehension
    # [print(numero ** 2) for numero in numeros]

    # Usando for loop tradicional
    for numero in numeros:
        print(numero ** 2)


def exercicio02() -> None:
    linguagens: list[str] = ["Python", "Java", "C++", "JavaScript"]
    # Remove primeira ocorrência de "C++"
    linguagens.remove("C++")
    # Poderiamos usar o método pop() para remover pelo índice
    # pop_index: int = linguagens.index("C++")
    # linguagens.pop(pop_index)

    # Adiciona "Ruby" ao final da lista
    linguagens.append("Ruby")
    # Poderiamos usar o método insert() para adicionar em uma posição específica, por exemplo na mesma posição que "C++" estava
    # linguagens.insert(pop_index, "Ruby")

    print(linguagens)


def exercicio03() -> None:
    livro: dict[str, str | list[dict[str, str]] | int] = {
        "titulo": "Aprendendo Python",
        "autores": [
            {
               "nome": "Mark Lutz",
               "nacionalidade": "Americano",
            },
            # {
            #    "nome": "Segundo Autor",
            #    "nacionalidade": "Brasileiro",
            # },
        ],
        "ano_publicacao": 2010,
    }

    for chave, valor in livro.items():
        if isinstance(valor, list):
            # Mostrando somente o "nome", por ser uma estrutura conhecida. Neste caso prefiro usar esta opção.
            print(f"{chave}:", end=" ")
            sub_valores: list[str] = [sub_valor["nome"] for sub_valor in valor]
            print(*sub_valores, sep=", ")

            # Mostrando dinamicamente as chaves e valores de subitens caso seja list[dict]
            # print(f"{chave}:")
            # for sub_objeto in valor:
            #     if isinstance(sub_objeto, dict):
            #         for sub_chave, sub_valor in sub_objeto.items():
            #             print(f"{sub_chave}: {sub_valor}.")

            # Poderiamos juntar as duas opções, mostrando os sub valores de possíveis list[dict] em uma linha.
            # print(f"{chave}:", end=" ")
            # for sub_objeto in valor:
            #     if isinstance(sub_objeto, dict):
            #         sub_valores: int[Union[str, int]] = [sub_valor for sub_valor in sub_objeto.values()]
            #         print(*sub_valores, sep=", ", end="; ")
            # print()
        else:
            print(f"{chave}: {valor}")


def exercicio04() -> None:
    from re import sub

    # Usando regex para remover números, caracteres especiais e espaços.
    texto: str = sub('[^A-Za-z]', '', input("Informe um texto: "))
    caracteres: dict[str, int] = {}

    for palavra in texto:
        caracteres.update({palavra: caracteres.get(palavra, 0) + 1})

    print(caracteres)


def exercicio05() -> None:
    lista_compras: list[str] = ["maçã", "banana", "cereja"]
    precos: dict[str, float] = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

    # Usando map
    total: float = sum(map(lambda item: precos.get(item, 0), lista_compras))

    # Usando list comprehension e o método get() de dict, que nos permite definir um valor padrão assim tratando quaisquer inconsistências
    # com presença de item sem correspondente de preço.
    # Caso usarmos acesso por chave precos[item] teriamos que usar try-except para tratar KeyError.
    # total: float = sum(precos.get(item, 0) for item in lista_compras)
    print(f"Total da lista: {total}.")


def exercicio06() -> None:
    emails: list[str] = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

    # Usando set, desta forma a ordem original não é preservada.
    # set_emails: set[str] = set(emails)
    # emails_unicos: list[str] = list(set_emails)

    # Usando set e for loop, mas preservando a ordem original.
    set_emails: set[str] = set()
    emails_unicos: list[str] = list()

    for email in emails:
        if email not in set_emails:
            set_emails.add(email)
            emails_unicos.append(email)

    print(emails_unicos)


def exercicio07() -> None:
    idades: list[int] = [22, 15, 30, 17, 18]

    # Usando list comprehension
    # idades_validas: list[int] = [idade for idade in idades if idade >= 18]
    # print(f"idades maiores que 18:", end=" ")
    # print(*idades_validas, sep=", ")

    # Usando unpack e filter para printar o retorno de uma iteravel já filtrado.
    print(f"idades maiores que 18:", end=" ")
    print(*filter(lambda idade: idade >= 18, idades), sep=", ")


def bubble_sort(pessoas: list[dict[str, Union[str, int]]]) -> None:
    n: int = len(pessoas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pessoas[j]["nome"].lower() > pessoas[j + 1]["nome"].lower():
                pessoas[j], pessoas[j + 1] = pessoas[j + 1], pessoas[j]


def selection_sort(pessoas: list[dict[str, Union[str, int]]]) -> None:
    n: int = len(pessoas)
    for i in range(n):
        min_idx: int = i
        for j in range(i + 1, n):
            if pessoas[j]["nome"].lower() < pessoas[min_idx]["nome"].lower():
                min_idx = j
        pessoas[i], pessoas[min_idx] = pessoas[min_idx], pessoas[i]


def insertion_sort(pessoas: list[dict[str, Union[str, int]]]) -> None:
    n: int = len(pessoas)
    for i in range(1, n):
        key: dict[str, Union[str, int]] = pessoas[i]
        j: int = i - 1
        while j >= 0 and pessoas[j]["nome"].lower() > key["nome"].lower():
            pessoas[j + 1] = pessoas[j]
            j -= 1
        pessoas[j + 1] = key


def merge_sort(pessoas: list[dict[str, Union[str, int]]]) -> list[dict[str, Union[str, int]]]:
    if len(pessoas) <= 1:
        return pessoas

    mid: int = len(pessoas) // 2
    left: list[dict[str, Union[str, int]]] = merge_sort(pessoas[:mid])
    right: list[dict[str, Union[str, int]]] = merge_sort(pessoas[mid:])

    return merge(left, right)


def merge(left: list[dict[str, Union[str, int]]], right: list[dict[str, Union[str, int]]]) -> list[dict[str, Union[str, int]]]:
    sorted_list: list = []
    while left and right:
        if left[0]["nome"].lower() <= right[0]["nome"].lower():
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list.extend(left or right)
    return sorted_list


def exercicio08() -> None:
    pessoas: list[dict[str, Union[str, int]]] = [
        {"nome": "Carol", "idade": 30},
        {"nome": "Bob", "idade": 25},
        {"nome": "Alice", "idade": 20},
        {"nome": "Bruno", "idade": 20},
        {"nome": "Thyene", "idade": 20},
        {"nome": "Lenize", "idade": 20},
        {"nome": "Lauren", "idade": 20},
    ]

    # Usando método sort de list, o qual modifica a lista original.
    # pessoas.sort(key=lambda pessoa: pessoa["nome"].lower(), reverse=False)
    # print(pessoas)

    # Usando sorted, assim preservando a lista original mas gerando uma nova lista.
    pessoas_por_nome: list[dict[str, Union[str, int]]] = sorted(pessoas, key=lambda pessoa: pessoa["nome"].lower(), reverse=False)
    print(pessoas_por_nome)

    # Usando bubble sort, este algoritimo itera sobre o tamanho da lista original
    # e para cada posição, faz uma nova iteração de 0 até a penúltima posição
    # isto por que o algoritimo em si irá trocar o elemento na posição atual pelo próximo.
    # Este algoritimo não é eficiente para listas grandes, uma vez que irá comparar cada elemento com cada um dos demais elementos. 
    # Portanto O(n²) salvo no acaso da lista já estar na ordem correta O(n).
    # bubble_sort(pessoas)
    # print(pessoas)

    # Usando selection sort, este algoritimo itera sobre o tamanho da lista original, define a posição com o menor elemento (ou maior, caso seja uma ordem decrescente)
    # e para cada posição, faz uma nova iteração da próxima posição até o tamanho máximo da lista
    # a nova iteração irá comparar o elemento da posição com aquele definido como menor, subistuitindo o menor indice.
    # ao fim da iteração a posição atual recebe o elemento da posição com menor elemento, e a posição do menor indice irá receber o elemento atual.
    # Este algoritimo irá comparar cada elemento com cada um dos demais elementos, portanto O(n²)
    # selection_sort(pessoas)
    # print(pessoas)

    # Usando insertion sort, este algoritimo itera sobre um range do tamanho da lista original iniciando do segundo (posição 1) elemento da lista.
    # vai definir o elemento atual e o indice anterior (j), então irá iterar com base no valor do indice anterior de forma descrescente
    # verificando a ordenação dos elementos, onde caso o elmento anterior seja maior que o atual ele é inserido na posição j + 1 e subtraindo j para a iteração descresente prosseguir.
    # ao fim, antes de iterar a próxima posição da lista o elemento atual é inserido na posição j + 1.
    # Este algoritmo ira comparar todos os elementos com cada um dos elementos da lista, portanto O(n²) com exceção de a lista já estar corretamente ordenada.
    # insertion_sort(pessoas)
    # print(pessoas)

    # Usando merge sort, este algoritmo ira dividir a lista ao meio quantas vezes forem necessário até que retorne somente um elemento para cada lado
    # sendo esquerda da posição 0 até o meio e direito do meio até o fim da lista.
    # Ao retornar um elemento para cada 'lado' será feita a união de ambos já aplicando a ordenação desejada.
    # A união consiste de uma iteração enquanto houverem elementos na esquerda e na direita, 
    # realizando a comparação de ordem desejada e removendo o item de um lado adicionando a uma nova lista.
    # Assim o processo irá iniciar de uma lista com n elementos, dividi-la de forma recursiva até que retorne um conjunto de dois itens já ordenados.
    # complexidade O(n log n)
    # pessoas_ordenadas = merge_sort(pessoas=pessoas)
    # print(pessoas_ordenadas)


def exercicio09() -> None:
    numeros: list[int] = [10, 20, 30, 40, 50]
    media: int = sum(numeros) / len(numeros)

    # from statistics import mean
    # media: int = mean(numeros)

    print(f"A média é: {media}.")


def exercicio10() -> None:
    valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares: list[int] = list(filter(lambda n: n % 2 == 0, valores))
    impares: list[int] = list(filter(lambda n: n % 2 == 1, valores))

    print(f"Pares: {pares} / Impares: {impares}")


def exercicio11() -> None:
    produtos: list[dict[str, Union[int, str]]] = [
        {"id": 1, "nome": "Teclado", "preço": 100},
        {"id": 2, "nome": "Mouse", "preço": 80},
        {"id": 3, "nome": "Monitor", "preço": 300}
    ]

    for produto in produtos:
        if produto.get('id') == 2:
            produto.update({'preço': 100})

    print(produtos)


def exercicio12() -> None:
    dicionario1: dict[str, int] = {"a": 1, "b": 2}
    dicionario2: dict[str, int] = {"c": 3, "d": 4}

    # lista_de_dicionarios: list[dict] = [
    #     dicionario1,
    #     dicionario2
    # ]

    # novo_dicionario: dict[str, int] = {}
    # for dicionario in lista_de_dicionarios:
    #     novo_dicionario.update(dicionario)

    # novo_dicionario: dict[str, int] = {k: v for d in lista_de_dicionarios for k, v in d.items()}

    # novo_dicionario: dict[str, int] = {**dicionario1, **dicionario2}
    novo_dicionario: dict[str, int] = dicionario1 | dicionario2
    # novo_dicionario: dict[str, int] = dicionario1.copy()
    # novo_dicionario.update(dicionario2)

    print(novo_dicionario)


def exercicio13() -> None:
    estoque: dict[str, int] = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

    estoque_positivo: dict[str, int] = {
        produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0
    }

    print(estoque_positivo)

    # print(dict(filter(lambda item: item[1] > 0, estoque.items())))


def exercicio14() -> None:
    dicionario: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    chaves: list[str] = list(dicionario.keys())
    valores: list[int] = list(dicionario.values())

    # chaves: list[str] = []
    # valores: list[int] = []
    # for chave in dicionario:
    #     chaves.append(chave)
    #     valores.append(dicionario[chave])

    print(f"Chaves: {chaves}, Valores: {valores}.")


def exercicio15() -> None:
    from re import sub
    # Usando regex para remover números, caracteres especiais e espaços.
    texto: str = sub('[^A-Za-z]', '', "engenharia de dados")
    caracteres: dict[str, int] = {}

    for caractere in texto:
        caracteres.update({caractere: caracteres.get(caractere, 0) + 1})

    print(caracteres)


def exercicio16(numeros: list[int | float]) -> None:
    try:
        soma: int | float = sum(numeros)
        print(f"A soma é {soma}.")
    except TypeError:
        print(f"Deve ser informada uma lista de números, exemplo: `[1,2,3]`.")


def exercicio17(numero: int) -> bool:
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Exemplo usando recursividade
# def inverte(texto: str) -> str:
#     if len(texto) == 0:
#         return texto
#     return inverte(texto[1:]) + texto[0]


def exercicio18(texto: str) -> None:
    inverso: str = ""
    for char in texto:
        inverso = char + inverso
    print(inverso)


def exercicio19(lista: list[int], numero: int) -> None:
    pares: list = []
    visto: set = set()

    for num in lista:
        complemento: int = abs(numero - num)
        if complemento in visto:
            pares.append((num, complemento))
        visto.add(num)

    print(pares)


def merge_sort20(pessoas: list[str]) -> list[str]:
    if len(pessoas) <= 1:
        return pessoas

    mid: int = len(pessoas) // 2
    left: list[str] = merge_sort20(pessoas[:mid])
    right: list[str] = merge_sort20(pessoas[mid:])

    return merge20(left, right)


def merge20(left: list[str], right: list[str]) -> list[str]:
    sorted_list: list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list.extend(left or right)
    return sorted_list


def exercicio20(dicionario: dict) -> None:
    keys: list[str] = list(dicionario.keys())
    print(merge_sort20(keys))
    # print sorted keys


# Desafio. Refatorar nosso código usando Dicionário, Type Hint e Funcões.
def classificacao_numero(numero: Union[int, float]) -> str:
    """Classifica um número como positivo ou negativo."""
    if numero < 0.0:
        return "negativo"
    else:
        return "positivo"


def obter_nome() -> str:
    """Solicita e valida o nome do usuário."""
    while True:
        nome: str = input("Olá, por favor informe seu nome: ").strip()
        if len(nome) == 0:
            raise UserWarning("Você deve informar um nome.")
        elif any(char.isdigit() for char in nome):
            raise UserWarning("O nome não pode conter números ou caracteres especiais.")
        else:
            return nome


def obter_salario() -> float:
    """Solicita e valida o salário mensal do usuário."""
    while True:
        try:
            salario: float = float(input("Informe seu salário mensal (exemplo: 3200.0): ").strip())
            if classificacao_numero(salario) == "negativo":
                raise UserWarning("O salário não pode ser um número negativo.")
        except ValueError as e:
            print("Você deve informar um número decimal.")
        else:
            return salario


def obter_bonus() -> float:
    """Solicita e valida a porcentagem do bônus."""
    while True:
        try:
            porcentagem_bonus: float = float(input("Agora informe o bônus (entre 0.0 a 100.0): ").strip())
            if porcentagem_bonus < 0.0 or porcentagem_bonus > 100:
                raise UserWarning("O bônus deve ser entre 0 e 100.")
        except ValueError:
            print("Você deve informar um valor decimal.")
        else:
            return porcentagem_bonus


def calcular_bonus(salario: float, porcentagem_bonus: float) -> float:
    """Calcula o bônus com base no salário e na porcentagem fornecida."""
    return 1_000 + salario * (porcentagem_bonus / 100)


def desafio() -> None:
    """
    Este desafio tem como objetivo calcular o valor bônus recebido por uma pessoa em cima de seu salário mensal.
    É preciso informar o nome, em seguida será solicitado o salário e o bônus percentual a ser calculado.

    A fórmula de cálculo é 1.000,00 + (salário * bônus).

    É possível cancelar a operação pressionando ctrl + c a qualquer momento.
    """
    while True:
        try:
            dados_usuario: dict[str, str | float] = {
                "nome": obter_nome(),
                "salario": obter_salario(),
                "bonus": obter_bonus(),
            }

            valor_bonus: float = calcular_bonus(dados_usuario["salario"], dados_usuario["bonus"])
            total: float = dados_usuario["salario"] + valor_bonus

            print(
                f"Olá, {dados_usuario['nome']}. Seu bônus neste ano é de {valor_bonus:.2f}, "
                f"totalizando {total:.2f}."
            )
        except UserWarning as e:
            print(e)
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        else:
            break


if __name__ == '__main__':
    desafio()
