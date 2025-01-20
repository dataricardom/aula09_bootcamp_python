from loguru import logger
numero = 10
numero2 = 20


def soma(a,b) -> int:
    return a + b

logger.info(soma(numero,numero2))

print(soma(numero, numero2))