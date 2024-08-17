import logging


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(filename=name,
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        encoding='utf-8')
    return logging.getLogger()
