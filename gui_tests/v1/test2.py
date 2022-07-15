import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import threading
import asyncio
import time



def gui():
    global typed_msg
    class MainWindow(qtw.QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Discord 2")

            self.setLayout(qtw.QVBoxLayout())

            my_label = qtw.QLabel()
            my_label.setFont(qtg.QFont('Helvetica', 10))
            self.layout().addWidget(my_label)

            my_entry = qtw.QLineEdit()
            my_entry.setObjectName("name_field")
            my_entry.setText("")
            self.layout().addWidget(my_entry)

            my_button = qtw.QPushButton("Send", clicked = lambda: press_it())
            self.layout().addWidget(my_button)

            self.show()

            def press_it():
                typed_msg = f'{my_entry.text()}'
                #print(typed_msg)
                my_entry.setText("")
                test(typed_msg)



    app = qtw.QApplication([])
    mw = MainWindow()


    app.exec_()


def test(typed_msg):
    print(typed_msg)
     #ok so like use my_label = qtw.QLabel(homo) to change what label says instead of variables

t1 = threading.Thread(target=gui, args=())
t1.start()








'''if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowOpacity(0.3)
    w.show()

    
    
    sys.exit(app.exec_())'''