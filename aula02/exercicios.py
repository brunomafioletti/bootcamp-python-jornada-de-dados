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
        primeiro_numero: int = int(input("Digite um número inteiro: "))
        segundo_numero: int = int(input("Digite outro número inteiro, para somarmos ao primeiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        soma: int = primeiro_numero + segundo_numero
        print(soma)


@request_user_input
def exercicio02() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        resto: float = primeiro_numero % 5
        print(f"O resto de {primeiro_numero} dividido por 5 é {resto}.")


@request_user_input
def exercicio03() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro: "))
        segundo_numero: int = int(input("Digite outro número inteiro, para multiplicarmos pelo primeiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        produto: int = primeiro_numero * segundo_numero
        print(f"O produto da multiplicação de {primeiro_numero} por {segundo_numero} é {produto}.")


@request_user_input
def exercicio04() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro: "))
        segundo_numero: int = int(input("Digite outro número inteiro, para realizarmos a divisão pelo primeiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        quociente: int = primeiro_numero // segundo_numero
        print(f"O quociente da divisão de {primeiro_numero} por {segundo_numero} é {quociente}.")


@request_user_input
def exercicio05() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro para calcularmos o quadrado: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        produto: int = primeiro_numero ** 2
        print(f"{primeiro_numero} ao quadrado é {produto}.")


@request_user_input
def exercicio06() -> None:
    try:
        primeiro_numero: float = float(input("Digite um número decimal: "))
        segundo_numero: float = float(input("Digite outro número decimal, para realizarmos a soma pelo primeiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        soma: float = primeiro_numero + segundo_numero
        print(f"A soma de {primeiro_numero:.2f} com {segundo_numero:.2f} é {soma:.2f}.")


@request_user_input
def exercicio07() -> None:
    try:
        primeiro_numero: float = float(input("Digite um número decimal: "))
        segundo_numero: float = float(input("Digite outro número decimal, para calcularmos a média de ambos: "))
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        # poderiamos modificar o fluxo para que o usuário possa informar uma lista de números ou várias números em inputs diferentes
        # calculando a média a partir da lista `soma dos elementos` / `tamanho da lista`.
        soma: float = primeiro_numero + segundo_numero
        media: float = soma / 2
        print(f"A média de {primeiro_numero:.2f} e {segundo_numero:.2f} é {media:.2f}.")


@request_user_input
def exercicio08() -> None:
    try:
        print("Vamos calcular a potência de um número n por um expoente n.")
        primeiro_numero: float = float(input("Primeiro informe a base: "))
        segundo_numero: float = float(input("Agora, informe o expoente: "))
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        potencia: float = primeiro_numero ** segundo_numero
        print(f"A potência de {primeiro_numero:.2f} por {segundo_numero:.2f} é {potencia:.2f}.")


@request_user_input
def exercicio09() -> None:
    from re import sub

    try:
        print("Converter temperatura em Celsius para Fahrenheit.")
        temp_input: str = sub('[^0-9.]', '', input("Informe a temperatura em Celsius: "))
        temp_celsius: float = float(temp_input)
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        temp_fahr: float = (temp_celsius * 1.8) + 32
        print(f"{temp_celsius:.2f}°C equivale a {temp_fahr:.2f}°F.")


@request_user_input
def exercicio10() -> None:
    from math import pi

    try:
        print("Vamos calcular a área de um circulo.")
        raio: float = float(input("Informe o raio do círculo: "))
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        area: float = pi * (raio ** 2)
        print(f"A área do círculo com raio {raio:.2f} é {area:.2f}.")


def exercicio11() -> None:
    texto: str = input("Informe um texto para convertermos todas as letras para maiúsculas: ")
    print(texto.upper())


def exercicio12() -> None:
    nome: str = input("Informe seu nome completo: ")
    print(nome.upper())


def exercicio13() -> None:
    frase: str = input("Informe uma frase: ")
    print(frase.strip())


def exercicio14() -> None:
    while True:
        try:
            data: str = input("Informe uma data no formato dia/mes/ano: ")
            splitted_data: list[str] = data.split(sep='/')
            print(f"A data informada foi dia {splitted_data[0]}, mês {splitted_data[1]} e ano {splitted_data[2]}")
        except IndexError:
            print(f"A data deve respeitar o formato dia/mes/ano. Data informada: {data}.")
        except KeyboardInterrupt:
            print("\n", "Saindo...", sep="")
            break
        else:
            break


def exercicio15() -> None:
    print("Vamos juntar dois textos distintos.")
    primeiro_texto: str = input("Digite o primeiro texto: ")
    segundo_texto: str = input("Digite o segundo texto: ")
    print(f"Seu texto novo é: {primeiro_texto + segundo_texto}.")


def exercicio16(a: bool, b: bool) -> None:
    print(a and b)


def exercicio17(a: bool, b: bool) -> None:
    print(a or b)


def exercicio18(a: bool) -> None:
    print(not a)


@request_user_input
def exercicio19() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro: "))
        segundo_numero: int = int(input("Digite outro número inteiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        print(f"Os números informados são {'iguais' if primeiro_numero == segundo_numero else 'diferentes'}.")


@request_user_input
def exercicio20() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número inteiro: "))
        segundo_numero: int = int(input("Digite outro número inteiro: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        print(f"Os números informados são {'diferentes' if primeiro_numero != segundo_numero else 'iguais'}.")


exercicio21 = exercicio09


def exercicio22() -> None:
    from re import sub

    while True:
        try:
            palavra: str = sub('[^A-Za-z]', '', input("Por favor, informe uma palavra: "))
            palavra_inversa: str = ""
            # Outra maneira de inverter a palvra seria usando slicing: palavra[::-1]
            # desta forma não seria necessário o uso do loop.
            for index in range(len(palavra)-1, -1, -1):
                palavra_inversa += palavra[index]
            print(f"A palavra {'é' if palavra == palavra_inversa else 'não é'} um palíndromo.")
        except KeyboardInterrupt:
            print("\n", "Saindo...", sep="")
            break
        else:
            break


@request_user_input
def exercicio23() -> None:
    try:
        primeiro_numero: float = float(input("Digite um número: "))
        segundo_numero: float = float(input("Digite outro número: "))
    except ValueError:
        raise ValueError("Você deve informar um número decimal.")
    else:
        operacao: str = input("Digite a operação que deseja realizar (+, -, *, /): ")

        if operacao == '+':
            soma = primeiro_numero + segundo_numero
            print(f"A soma de {primeiro_numero:.2f} por {segundo_numero:.2f} é {soma:.2f}.")
        elif operacao == '-':
            subtracao = primeiro_numero - segundo_numero
            print(f"A subtração de {primeiro_numero:.2f} por {segundo_numero:.2f} é {subtracao:.2f}.")
        elif operacao == '*':
            produto = primeiro_numero * segundo_numero
            print(f"O produto de {primeiro_numero:.2f} por {segundo_numero:.2f} é {produto:.2f}.")
        elif operacao == '/':
            quociente = primeiro_numero / segundo_numero
            print(f"O quociente de {primeiro_numero:.2f} dividio por {segundo_numero:.2f} é {quociente:.2f}.")
        else:
            raise UserWarning("Operação inválida, tente novamente? ou pressione ctrl + c para sair.")


@request_user_input
def exercicio24() -> None:
    try:
        primeiro_numero: int = int(input("Digite um número: "))
    except ValueError:
        raise ValueError("Você deve informar um número inteiro.")
    else:
        if primeiro_numero == 0:
            print(f"{primeiro_numero} é zero.")
        elif primeiro_numero % 2 == 0:
            print(f"{primeiro_numero} é um número par e {classificacao_numero(primeiro_numero)}.")
        else:
            print(f"{primeiro_numero} é um número ímpar e {classificacao_numero(primeiro_numero)}.")


def classificacao_numero(numero: Union[int, float]) -> str:
    if numero < 0.0:
        return "negativo"
    else:
        return "positivo"

@request_user_input
def exercicio25() -> None:
    try:
        input_lista_numeros: list[str] = input("Digite uma lista de números separados por vírgula 1, 2, n: ").split(',')
        lista_numeros: list[int] = list(map(lambda n: int(n.strip()), input_lista_numeros))
    except ValueError:
        raise ValueError("Você deve informar uma lista exclusivamente de números inteiros separados por vírgula.")
    else:
        print(f"A lista de números é válida e possui os valores: {lista_numeros}")


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
