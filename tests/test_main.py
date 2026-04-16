from laboratorio1_ia.main import suma, es_mayor_que_cinco

def test_suma() -> None:
    assert suma(5, 3) == 8

def test_es_mayor_que_cinco_true() -> None:
    assert es_mayor_que_cinco(8) is True

def test_es_mayor_que_cinco_false() -> None:
    assert es_mayor_que_cinco(5) is False

def suma(a: int, b: int) -> int:
    return a + b

def es_mayor_que_cinco(valor: int) -> bool:
    return valor > 5

# Operación Nueva
def multiplicar(a: int, b: int) -> int:
    return a * b

def main() -> None:
    print("Curso: Sistemas Inteligentes")
    print("Sesión 1 - Entorno reproducible con Poetry")
    a = 5
    b = 3
    resultado = suma(a, b)
    print("La suma es:", resultado)

    # uso de la nueva operación
    resultado_mult = multiplicar(a, b)
    print("La multiplicación es:", resultado_mult)
    if es_mayor_que_cinco(resultado):
        print("La suma es mayor que 5")
    else:
        print("La suma es menor o igual que 5")

    numero = int(input("Ingrese un número: "))
    print("El número ingresado es:", numero)


if __name__ == "__main__":
    main()

from laboratorio1_ia.main import multiplicar
def test_multiplicar() -> None:
    assert multiplicar(4, 3) == 12