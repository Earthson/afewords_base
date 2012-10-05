import logging

def log_error(des='error', **kw):
    logging.info('+'*30)
    logging.info('Error description : ' )
    logging.info(des)
    for oo in kw:
        logging.info(oo + kw[oo])
    logging.info('+'*30)
    
def log_warning(des='Warn', **kw):
    logging.info('+'*30)
    logging.info('Warn description : ' )
    logging.info(des)
    for oo in kw:
        logging.info(oo + kw[oo])
    logging.info('+'*30)

def log_info(des='INFO', **kw):
    logging.info('+'*30)
    logging.info('INFO description : ' )
    logging.info(des)
    for oo in kw:
        logging.info(oo + kw[oo])
    logging.info('+'*30)
