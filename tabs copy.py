import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout,QLabel,QTabWidget,QVBoxLayout
from PyQt5.QtCore import *

class Principal (QMainWindow):
    #constructor de la clase  principal 
    def __init__(self):
       super().__init__()
       self.setWindowTitle ("Menu")
       self.setGeometry (100,100,400,300)
       self.layout = QVBoxLayout (self)
       self.tabs = QTabWidget()
       self.setCentralWidget(self.tabs)

       self.tab_registro = QWidget()
       self.tab_test = QWidget()
       self.tab_res = QWidget()

       self.tabs.addTab(self.tab_registro,"Registro")
       self.tabs.addTab(self.tab_test,"Test")
       self.tabs.addTab(self.tab_res,"Resultados")

       self.crear_pestana_registro()
       self.crear_pestana_test()
       self.crear_pestana_resultados ()
    
    def crear_pestana_registro(self):
        layout=QGridLayout()
        etiqueta1= QLabel ("Registro")
        layout.addWidget(etiqueta1,0,0) 
        self.tab_registro.setLayout(layout)

    def crear_pestana_test(self):
        layout=QGridLayout()
        etiqueta2=QLabel ("Test")
        layout.addWidget (etiqueta2,0,0)
        self.tab_test.setLayout(layout)

    def crear_pestana_resultados(self):
        layout  =  QGridLayout()
        etiqueta3=QLabel("Resultados")
        layout.addWidget(etiqueta3,0,0)
        self.tab_res.setLayout(layout)



app= QApplication(sys.argv)
window= Principal()
window.show()
app.exec()



