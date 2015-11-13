import re

#HTMLのエスケープ元に戻す
def decode(text):
    result = text.replace('&gt;','>').replace('&lt;','<').replace('&amp;','&')
    return result
