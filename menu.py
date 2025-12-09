from PyQt5.QtWidgets import *

app = QApplication([])
w = QWidget()
v = QVBoxLayout(w)
v.addWidget(QLabel("Menu prinpal"))
h = QHBoxLayout()
for t in ("Registro","Test","Resultados"): h.addWidget(QPushButton(t))
v.addLayout(h)

w.show()
app.exec_()