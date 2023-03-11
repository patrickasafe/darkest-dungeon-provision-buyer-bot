from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class LabelledIntField(QWidget):
    def __init__(self, title, initial_value=None):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel()
        self.label.setText(title)
        # self.label.setFixedWidth(100)
        self.label.setFont(QFont("Arial",weight=QFont.Weight.Bold))
        layout.addWidget(self.label)
        self.label.alignment()
        
        self.lineEdit = QLineEdit(self)
        # self.lineEdit.setFixedWidth(40)
        self.lineEdit.setValidator(QIntValidator())
        if initial_value != None:
            self.lineEdit.setText(str(initial_value))
        layout.addWidget(self.lineEdit)
        layout.addStretch()
        
    def setLabelWidth(self, width):
        self.label.setFixedWidth(width)
        
    def setInputWidth(self, width):
        self.lineEdit.setFixedWidth(width)
        
    def getValue(self):
        return int(self.lineEdit.text())