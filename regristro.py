import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import PROYECTO.Alumno as Alumno
class Principal(QMainWindow):
    #constructor de la clase Principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar")

    #crea los diferentes widgets
        self.lb_control = QLabel("Numero de control")
        self.lb_nombre= QLabel("Nombre")
        self.lb_semestre= QLabel("Semestre")
        self.lb_grupo= QLabel("Grupo")
        self.txt_control = QLineEdit()
        self.txt_nombre= QLineEdit()
        self.txt_semestre = QLineEdit()
        self.txt_grupo = QLineEdit()
        self.btn_convertir = QPushButton("Registrar")

        layout = QGridLayout()
        layout.addWidget(self.lb_control, 0, 0)
        layout.addWidget(self.txt_control, 0, 1)
        layout.addWidget(self.lb_nombre, 1, 0)
        layout.addWidget(self.txt_nombre, 1, 1)
        layout.addWidget(self.lb_semestre, 2, 0)
        layout.addWidget(self.txt_semestre, 2, 1)
        layout.addWidget(self.lb_grupo, 3, 0)
        layout.addWidget(self.txt_grupo ,3, 1)
        layout.addWidget(self.btn_convertir, 4, 0)

        self.btn_convertir.clicked.connect(self.convertir)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def convertir(self):
        try:
            control= float(self.txt_control.text())
        except:
            print("ERROR")
            QMessageBox.warning(self,"error"," Ingresa solo numeros")
        else:
            nombre=self.txt_nombre.text()
            apellidos=self.txtapellidos.text()

            estudiante=estudiante(control,nombre,apellidos,telefono)
            #alumno=alumno(control,nombre,semestre,grupo)
            print("el usuario se resgristro correctamente ")
    
            nombre= control
            self.txt_control.setText(str(nombre))

app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()