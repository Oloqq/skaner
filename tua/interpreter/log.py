import logging

log = logging.getLogger("tua")

def init_log(lvl):
    global log

    log.setLevel(lvl)
    # create a formatter for the log messages
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(levelname)s - %(message)s')

    if lvl < logging.WARNING:
        # create a file handler for debug logs
        debug_handler = logging.FileHandler('debug.log', mode='w')
        debug_handler.setLevel(logging.DEBUG)

        # create a file handler for info logs
        info_handler = logging.FileHandler('info.log', mode='w')
        info_handler.setLevel(logging.INFO)

        # create a file handler for warning logs
        warning_handler = logging.FileHandler('warning.log', mode='w')
        warning_handler.setLevel(logging.WARNING)

        # create a file handler for error logs
        error_handler = logging.FileHandler('error.log', mode='w')
        error_handler.setLevel(logging.ERROR)

        # add the formatter to the handlers
        debug_handler.setFormatter(formatter)
        info_handler.setFormatter(formatter)
        warning_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        # add the handlers to the logger
        log.addHandler(debug_handler)
        log.addHandler(info_handler)
        log.addHandler(warning_handler)
        log.addHandler(error_handler)

    if lvl >= logging.WARNING:
        # write warning and error logs to the console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.WARNING)
        stream_handler.setFormatter(formatter)

        # add the stream handler to the logger
        log.addHandler(stream_handler)
