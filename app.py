'''
Este es un programa que calcula el indice de masa corporal
Lenguage python
created by: Jhon Fernando Moreno Ramírez
'''

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

class ejemplo_GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/principal.ui",self)
        self.btnCalcular.clicked.connect(self.calcular)
    
    def diagnostico(self,res):
        if res < 18.5:
            return 'EL paciente esta con peso bajo'
        elif res >=18.5 and res < 25:
            return 'El paciente presenta peso normal'
        elif res >=25 and res < 30:
            return 'El paciente presenta sobrepeso'
        else:
            return 'El paciente se encuentra en estado de obesidad'
        
    def calcular(self):
        est=self.textEstatura.text()
        pes=self.textPeso.text()
        opc=self.comboBoxSeleccionar.currentText()
        if est =='' or pes == '':
            #diag=dialogo(self)
            #diag.show()
            QMessageBox.about(self,"Error","Las casillas NO pueden estar vacias")
        elif opc=='cm y Kg':
            cm=float(est)
            kg=float(pes)
            imc=kg/((cm/100)**2)
            diag=self.diagnostico(imc)
            frase='Su indice Masa corporal es :'+str(imc)+'Su diagnostico es '+diag
            
            print("palabra frase ",type(frase))
            self.resultado.setPlaceholderText(str(frase))
        elif opc=='pul y libras':
            pul=float(est)
            libras=float(pes)
            imc=(libras/(pul)**2)*703
            diag=self.diagnostico(imc)
            frase='Su indice Masa corporal es :'+str(imc)+'Su diagnostico es '+diag
            self.resultado.setPlaceholderText(str(frase))

class dialogo(QDialog):
    def __init__(self ,*args, **kwargs):
        super(dialogo,self).__init__(*args, **kwargs)
        self.setWindowTitle("Soy un popup")
        self.setFixedSize(200, 100)
                
            
if __name__=='__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())