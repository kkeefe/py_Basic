#!/usr/bin/env python

from PyQt5.QtWidgets import *


class userInterface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        # define the full layout of where to put the interface
        self.layout = QVBoxLayout()
        self.layout.addWidget(QPushButton('Top'))
        self.layout.addWidget(QPushButton('Bottom'))
        # define a button and a push button method
        button = QPushButton('Click')
        button.clicked.connect(on_button_clicked)
        button.show()

        layout.addWidget(QCheckBox())
        label1 = QLabel("first text label")
        layout.addWidget(label1)

        # make a table with whatever rows / columns you want
        table = QTableWidget(rowCount=2,columnCount=3)
        table.cellClicked.connect(on_cell_clicked)
        layout.addWidget(table)

        line = QLineEdit()
        layout.addWidget(line)
        line.returnPressed.connect(on_line_reg('you returned something'))

        window = QWidget()
        window.setLayout(layout)
        window.setWindowTitle("App Title")
        window.setGeometry(10, 10, 640, 480)

        self.layout.addWidget(button)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def clickMethod(self):
        print('Your name: ' + self.line.text())

    def on_button_clicked():
        # display a message box when this button is clicked..
        alert = QMessageBox()
        # define what to say when the button is clicked..
        alert.setText('You clicked the button!')
        alert.exec_()

    def on_cell_clicked():
        alert = QMessageBox()
        alert.setText('You clicked the cell!')
        alert.exec_()

    def on_line_reg(word='something'):
        alert = QMessageBox()
        alert.setText(word)
        alert.exec_()

# # items inside a table take objects: 'QTableWidgetItem'..
#     self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
#     self.tableWidget.move(0,0)

# check to see if we're running this file as main
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    userWindow = userInterface()
    userWindow.show()
    sys.exit( app.exec_() )
