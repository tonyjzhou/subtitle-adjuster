import logging


def config_logger(logfile='logs/subtitle-adjuster.log'):
    log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    add_file_handler(log_formatter, root_logger, logfile)
    add_console_handler(log_formatter, root_logger)


def add_console_handler(log_formatter, root_logger):
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)


def add_file_handler(log_formatter, root_logger, logfile):
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
