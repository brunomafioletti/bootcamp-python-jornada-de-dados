from curses.textpad import Textbox
from typing import Any, Callable, Union


def request_user_input(f) -> Callable[..., Any | None]:
    def active_loop(*args, **kwargs) -> None:
        while True:
            try:
                return f(*args, **kwargs)
            except ValueError as e:
                print(e)
            except ZeroDivisionError:
                print("Não é possível dividir por zero, tente novamente.")
            except UserWarning as e:
                print(e)
            except KeyboardInterrupt:
                print("\n", "Saindo...", sep="")
                break
            # Poderiamos remover este else e forçar o usuário a pressionar ctrl + c para sair.
            # Mas acho melhor sair da função caso não ocorra nenhuma exceção.
            else:
                break

    return active_loop


@request_user_input
def exercicio01() -> None:
    try:
        quantidade: int = int(input("Digite a quantidade: "))
        preco: float = float(input("Digite o preço: "))
    except ValueError:
        raise ValueError("Digite um número inteiro para a quantidade e um número decimal para o preço.")
    else:
        print(f"Os dados são {'válidos' if valida_quantidade_preco(quantidade=quantidade, preco=preco) else 'inválidos'}.")


def valida_quantidade_preco(quantidade: int, preco: float) -> bool:
    if quantidade > 0 and preco > 0.0:
        return True
    return False


@request_user_input
def exercicio02() -> None:
    from re import sub

    try:
        temp_input: str = sub('[^0-9.]', '', input("Informe a temperatura em Celsius: "))
        temp_celsius: float = float(temp_input)
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        print(f"A temperatura {temp_celsius}°C é classificada como {classifica_temperatura(temp_celsius)}.")


def classifica_temperatura(temperatura: float) -> None:
    if temperatura < 18:
        return "Baixa"
    elif temperatura <= 26:
        return "Normal"
    else:
        return "Alta"


def exercicio03() -> None:
    log_examples: list[dict[str, str]] = [
        {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
        {'timestamp': '2021-06-24 10:00:00', 'level': 'INFO', 'message': 'Alguma outra mensagem'}
    ]

    # Usando list comprehension
    [print(log['message']) for log in log_examples if log['level'] == 'ERROR']

    # Usando for loop tradicional
    # for log in log_examples:
    #     if log['level'] == 'ERROR':
    #         print(log['message'])

    # Using map
    # list(map(print, [log['message'] for log in log_examples if log['level'] == 'ERROR']))

@request_user_input
def exercicio04() -> None:
    try:
        email: str = input("Digite seu email: ")
        if not valida_email(email):
            raise UserWarning("Email inválido.")
        idade: int = int(input("Digite sua idade: "))
        #  Poderiamos usar uma comparação concisa como `not 18 <= idade <= 65`, porém acho a forma abaixo mais clara.
        if idade < 18 or idade > 65:
            raise UserWarning("Idade deve estar entre 18 e 65 anos.")
    except ValueError:
        raise ValueError("Idade deve ser um número inteiro.")
    else:
        print("Dados de usuário válido.")


def exercicio05() -> None:
    exemplos_transacoes: list[dict[str, int]] = [
        {'valor': 9000, 'hora': 14},
        {'valor': 12000, 'hora': 14},
        {'valor': 9000, 'hora': 21},
        {'valor': 12000, 'hora': 20},
    ]

    [valida_transacoes(transacao) for transacao in exemplos_transacoes]


def valida_transacoes(transacao: dict[str, int]) -> None:
    mensagens: list[str] = []

    # Apresentando mensagens mais específicas.
    if transacao['valor'] > 10000:
        mensagens.append("Transação de alto valor")

    if transacao['hora'] < 9 or transacao['hora'] > 18:
        mensagens.append("Transação fora do horário comercial")

    if not mensagens:
        mensagens.append("Transação normal")

    print(*mensagens, sep=", ", end=".\n")

    # Apresentando mensagem mais concisa.
    # if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
    #     print("Transação suspeita.")
    # else:
    #     print("Transação normal.")


def exercicio06() -> None:
    from re import sub

    # Usando regex para remover caracteres especiais, exceto espaço.
    texto: str = sub('[^A-Za-z ]', '', input("Informe um texto: "))
    palavras: dict[str, int] = {}

    for palavra in texto.split():
        palavras.update({palavra: palavras.get(palavra, 0) + 1})

    print(palavras)


def exercicio07() -> None:
    numeros: list[int] = [10, 20, 30, 40, 50]
    menor_fator : int = min(numeros)
    numeros_normalizados: list[str] = [(numero - menor_fator) / (max(numeros) - menor_fator) for numero in numeros]
    print(numeros_normalizados)


def exercicio08() -> None:
    usuarios: list[dict[str, str]] = [
        {"nome": "Alice", "email": "alice@example.com"},
        {"nome": "Bob", "email": ""},
        {"nome": "Carol", "email": "carol@example.com"}
    ]

    usuarios_sem_email: list = list(filter(lambda usuario: not valida_email(usuario['email']), usuarios))
    print(usuarios_sem_email)


def valida_email(email: str) -> None:
    if "@" not in email or "." not in email:
        return False
    return True


def exercicio09() -> None:
    numeros: list[int] = range(1, 101)

    # Usando filter, prefiro esta abordagem pois acho mais claro e uso de lazy evaluation pode ser útil em casos mais complexos.
    numeros_pares: list[int] = list(filter(lambda numero: numero % 2 == 0, numeros))

    # Usando list comprehension
    # numeros_pares = [numero for numero in numeros if numero % 2 == 0]

    print(numeros_pares)


def exercicio10() -> None:
    vendas: list[dict[str, Union[str, int]]] = [
        {"categoria": "eletrônicos", "valor": 1200},
        {"categoria": "livros", "valor": 200},
        {"categoria": "eletrônicos", "valor": 800}
    ]
    categorias: dict[str, int] = {}

    for venda in vendas:
        categoria = venda['categoria']
        categorias.update({categoria: categorias.get(categoria, 0) + venda['valor']})

    print(categorias)


@request_user_input
def exercicio11() -> None:
    entrada: str = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.lower() == "sair":
        raise KeyboardInterrupt

    print(f"Você digitou: {entrada}")


@request_user_input
def exercicio12() -> None:
    try:
        entrada: int = int(input("Digite um número entre 1 e 10: "))
        if entrada < 1 or entrada > 10:
            raise UserWarning("Número fora do intervalo permitido.")
    except ValueError:
        raise ValueError("Digite um número inteiro.")
    else:
        print(f"Você digitou: {entrada}")

@request_user_input
def exercicio13() -> None:
    from math import ceil

    try:
        total_de_registros: int = 10_000
        limite_pagina: int = int(input("Quantos itens por pagina: "))
        if limite_pagina <= 0:
            raise UserWarning("O limite de itens por página deve ser maior que zero.")

        total_de_paginas: int = ceil(total_de_registros / limite_pagina)
        pagina_atual: int = 1
        while pagina_atual <= total_de_paginas:
            print(f"Exibindo página {pagina_atual} de {total_de_paginas}")
            # print(f"Processados {limite_pagina * pagina_atual} de {total_de_registros} registros.")
            # print(f"Exibindo registros de {limite_pagina * (pagina_atual - 1) + 1} a {min(limite_pagina * pagina_atual, total_de_registros)}")
            pagina_atual += 1

    except ValueError:
        raise ValueError("Digite um número inteiro.")



def exercicio14() -> None:
    from time import sleep

    tentativas_maxima: int = 5
    tentativa_atual: int = 1

    while tentativa_atual <= tentativas_maxima:
        try:
            print(f"Simulando conexão... tentativa {tentativa_atual} de {tentativas_maxima}.")
            # Simula falha.
            if True:
                raise UserWarning("Falha na conexão.")
            print("Conexão bem sucedidade.")
            break
        except UserWarning:
            if tentativa_atual == tentativas_maxima:
                print("Falha! Número máximo de tentativas atingido, saindo...")
                break
            print(f"Falha na conexão, aguardando {2 ** tentativa_atual} segundos para tentar novamente.")
            tentativa_atual += 1
            sleep(2 ** tentativa_atual)


def exercicio15() -> None:
    itens = [1, 2, 3, "parar", 4, 5]

    i = 0
    while i < len(itens):
        if itens[i] == "parar":
            print(f"Encontrado item 'parar' na posição {i}.")
            break
        print(f"Processando item {itens[i]}")
        i += 1


def classificacao_numero(numero: Union[int, float]) -> str:
    if numero < 0.0:
        return "negativo"
    else:
        return "positivo"


def desafio() -> None:
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


if __name__ == '__main__':
    desafio()
