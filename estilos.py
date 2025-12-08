import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout,QPushButton
class Principal(QMainWindow):
    #constructor de la clase Principal
    def __init__(self):
        super().__init__()
        estilo_boton = """QPushButton{ background-color: #FFFFFF;
                                        border: 2px solid #007BFF;
                                        color: #000000;
                                        padding: 15px 32px;
                                        text-align: center;
                                        text-decoration:none;
                                        font-size: 16px;
                                        margin: 4px 2px;
                                        border-radius:10px;}
        QPushButton:hover{ background-color: #E1F0FF;
                           border-color: #000000;
                           }
                           """

        self.btn_registrar= QPushButton("Registrar")
        self.btn_registrar.setStyleSheet(estilo_boton)
        #Crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.btn_registrar,4,1)

        #Agrega el layout a la ventana
        widget   = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app= QApplication(sys.argv)
window= Principal()
window.show()
app.exec()