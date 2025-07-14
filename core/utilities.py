import logging, mimetypes

logging.basicConfig(filename="logs/history.log", level=logging.INFO)

def log_action(msg): logging.info(msg)
def get_mime_type(path): return mimetypes.guess_type(path)[0]
