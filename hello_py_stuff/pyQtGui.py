#!/usr/bin/env python

import sys
import PyQt5
# from PyQt5.QtWidgets import *

# class userInterface(QtWidgets.QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

app = PyQt5.QtWidgets.QApplication([])
app.setStyle('Fusion')

def clickMethod(self):
    print('Your name: ' + self.line.text())

def on_button_clicked():
    # display a message box when this button is clicked..
    alert = QMessageBox()
    # define what to say when the button is clicked..
    alert.setText('you clicked the button!')
    alert.exec_()

def on_asic_click():
    # display a message box when this button is clicked..
    alert = QMessageBox()
    # define what to say when the button is clicked..
    alert.setText('you clicked the asic button!')
    alert.exec_()

def exit_button():
    # display a message box when this button is clicked..
    sys.exit()

def on_cell_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the cell!')
    alert.exec_()

def on_line_reg(word='something'):
    alert = QMessageBox()
    alert.setText(word)
    alert.exec_()

# we need a window
window = QWidget()
layout = QVBoxLayout()
window.setWindowTitle("App Title")
window.setGeometry(10, 10, 640, 480)

# define a button and a push button method
button2 = QPushButton('Press to exit')
button2.clicked.connect(exit_button)
layout.addWidget(button2)

# define a button and a push button method
button = QPushButton('Edit FSM')
button.clicked.connect(on_button_clicked)
layout.addWidget(button)

# define a button and a push button method
button3 = QPushButton('Display Asic Settings')
button3.clicked.connect(on_asic_click)
layout.addWidget(button3)

# make a label
label1 = QLabel("first text label")
layout.addWidget(label1)

# make a table with whatever rows / columns you want
table = QTableWidget(rowCount=2,columnCount=3)
table.cellClicked.connect(on_cell_clicked)
# lets do something cute with the table indiceis
table.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
layout.addWidget(table)

# make a line and do something with it
line = QLineEdit()
line.returnPressed.connect(on_line_reg)
layout.addWidget(line)

# add the widgets we've made
layout.addWidget(QCheckBox())

# add everything to out window
window.setLayout(layout)

# show what we've made
window.show()

sys.exit(app.exec_())

# # items inside a table take objects: 'QTableWidgetItem'..
#     self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
#     self.tableWidget.move(0,0)

# check to see if we're running this file as main
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     userWindow = userInterface()
#     userWindow.show()
#     sys.exit( app.exec_() )
