from PyQt5 import uic

with open("Panel.py", "w", encoding="utf-8") as fout:
    uic.compileUi("panel.ui", fout)