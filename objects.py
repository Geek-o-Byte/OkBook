from PyPDF2 import PdfReader
from PIL import Image
import mimetypes
import re

def is_image(mimetype):
    if len(re.findall('/(^image)(\/)[a-zA-Z0-9_]*/gm',mimetype)) > 0:
        return True
    return False


class File:
    def __init__(self, path):
        self.type = mimetypes.guess_type(path)[0]
        if is_image(self.type):
            self.file = Image.open(path)
        elif self.type == 'application/pdf':
            self.file = PdfReader(path)
            self.pages = self.file.pages
        else:
            self.file = None