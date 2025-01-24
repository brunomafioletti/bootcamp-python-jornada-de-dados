def exercicio01() -> None:
    name_size: int = len(input("Digite seu nome e direi quantos caracteres ele possui: ").strip())
    print(f"Seu nome possui {name_size} caracteres")


def exercicio02() -> None:
    while True:
        try:
            primeiro_numero: int = int(input("Digite um número: "))
            segundo_numero: int = int(input("Digete outro número, para somarmos ao primeiro: "))
            soma: int = primeiro_numero + segundo_numero
            print(soma)
        except ValueError as e:
            print("Você deve informar um número, tente novamente.")
        except KeyboardInterrupt as e:
            print("\n", "Saindo...", sep="")
            break
        else:
            break


def desafio() -> None:
    """
    Este desafio tem como objetivo calcular o valor bônus recebido por uma pessoa em cima de seu salário mensal.
    É preciso informar o nome, em seguida será solicitado o salário e o bônus percentual a ser calculado.

    A fórmula de cálculé 1.000,00 + (salário * bônus).

    É possível cancelar a operação pressionando ctrl + c a qualquer momento.
    """
    try:
        nome: str = input("Olá, por favor informe seu nome: ").strip()

        while True:
            try:
                salario: float = float(input("Informe seu salário mensal (exemplo: 3200.0): ").strip())
                bonus: float = float(input("Agora informe o bônus (entre 0.0 a 100.0): ").strip())
                if bonus < 0.0 or bonus > 100:
                    raise AttributeError
            except ValueError:
                print("Você deve informar um número.")
            except AttributeError:
                print("O bônus deve ser entre 0 e 100.")
            else:
                break

        salario_bonus: float = 1_000 + salario * (bonus / 100)
        print(f"Olá, {nome}. Seu bônus neste ano é de {salario_bonus:.2f}")
    except KeyboardInterrupt:
        print("\n", "Saindo...", sep="")
        exit()

if __name__ == '__main__':
    desafio()
