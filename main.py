from flask import jsonify
from api.languages import Languages

JS = Languages("javascript", 3, "js", "test", "hello world", "js")
PY = Languages("python", 3, "python", "test", "hello world", "python")


print(PY.getLanguage())





