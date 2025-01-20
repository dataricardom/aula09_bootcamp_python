from loguru import logger

logger.debug("Um aviso")
logger.info("Informação do processo")
logger.warning("Aviso que possivelmente algo vai parar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu algo que aborta a aplicação")