import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout,QLabel,QTabWidget,QVBoxLayout,QLineEdit,QPushButton,QMessageBox,QGroupBox,QRadioButton
from PyQt5.QtCore import *
from pregunta import Pregunta 

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
        self.tab_registro.setLayout(layout)

    def crear_pestana_test(self):
        
        self.crearCuestionario()
        self.index = 0
        self.maximo=len (self.cuestionario)
        
        # Crea los diferentes widgets
        self.lb_num=QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_pregunta = QLabel(self.cuestionario [self.index].texto)
        self.btn_siguiente = QPushButton("Siguiente")
        
        #radio buttons
        self.grupo=QGroupBox("seleccione una opcion")
        vbox=QVBoxLayout()        
        self.nunca = QRadioButton("nunca")
        self.aveces = QRadioButton(" a veces ")
        self.frec = QRadioButton ("frecuentemente ")
        self.siempre = QRadioButton ("siempre")

        vbox.addWidget(self.nunca)
        vbox.addWidget(self.aveces)
        vbox.addWidget(self.frec)
        vbox.addWidget(self.siempre)
        self.grupo.setLayout(vbox)

        
        # Crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_num,0,0)
        layout.addWidget(self.lb_pregunta,1,0)
        layout.addWidget(self.grupo,2,0)
        layout.addWidget(self.btn_siguiente,3,0)
        #self.index= self.index+1
        
        # Crea los eventos
        self.btn_siguiente.clicked.connect(self.siguiente)
        self.tab_test.setLayout(layout)

    def crear_pestana_resultados(self):
        layout  =  QGridLayout()
        etiqueta3=QLabel("Resultados")
        layout.addWidget(etiqueta3,0,0)
        self.tab_res.setLayout(layout)

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

    def crearCuestionario(self):
        #llenar cuestionario 
        Pregunta1= Pregunta(1,"¿pasas mucho tiempo viendo redes sociales?",0)
        Pregunta2= Pregunta(2,"¿revisas tus redes sociales apenas que te levantas?",0)
        Pregunta3= Pregunta(3,"¿te cuesta pasar un dia sin entrar a tus redes sociales?",0)
        Pregunta4= Pregunta(4,"¿sientes la necesidad de estar conectado todo el tiempo para no perderte nada?",0)
        Pregunta5= Pregunta(5,"¿pierdes la nocion del tiempo cuando estas en redes sociales?",0)
        Pregunta6= Pregunta(6,"¿Has descuidado tareas o estudios por usar redes sociales?",0)
        Pregunta7= Pregunta(7,"¿Has dormido menos horas por quedarte usando redes sociales?",0)
        Pregunta8= Pregunta(8,"¿Prefieres estar en redes sociales antes que convivir con amigos o familia?",0)
        Pregunta9= Pregunta(9,"¿Te distraes fácilmente pensando en tus redes mientras haces otras actividad?",0)
        Pregunta10= Pregunta(10,"¿Usas redes sociales en momentos inadecuados (clase, trabajo, comidas)?",0)


       
        # Agrega los elementos a la lista llamada cuestionario
        self.cuestionario=[Pregunta1,Pregunta2,Pregunta3,Pregunta4,Pregunta5,Pregunta6,Pregunta7,Pregunta8,Pregunta9,Pregunta10]
        
    
    def siguiente(self):
        self.validar_respuesta()
        if self.resp >=0:
            #guardar la respuesta
            self.cuestionario[self.index].respuesta=self.resp
            print(self.cuestionario[self.index].respuesta)

        if self.index < self.maximo -1:
            self.index = self.index + 1
            num=str(self.cuestionario[self.index].num_pregunta)
            preg=self.cuestionario[self.index].texto
            self.lb_num.setText(num)
            self.lb_pregunta.setText(preg)

    def validar_respuesta(self):
        if self.nunca.isChecked():
            self.resp = 0
        elif self.aveces.isChecked():
            self.resp = 1
        elif self.frec.isChecked():
            self.resp = 2
        elif self.siempre.isChecked():
            self.resp = 3
        else:
            QMessageBox.warning(self, "Error","Seleccione una opción")
            self.resp = -1

    
app= QApplication(sys.argv)
window= Principal()
window.show()
app.exec()



