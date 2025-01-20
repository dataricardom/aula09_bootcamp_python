from loguru import logger

numero = 10
numero2 = 20
def soma(a,b) -> int:
    try:
        soma = a + b
        logger.info(f"Os valores digitados foram corretos {soma}")
        return a + b
    except:
        logger.critical("Operação invalida")
logger.add("resultado.log", level="CRITICAL")
print(soma(numero, "a"))

