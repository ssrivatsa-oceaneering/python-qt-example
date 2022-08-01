# This Python file uses the following encoding: utf-8
#gb 1Aug2022.
#Making some notes to see how Git works.  Sidd made some changes to the code to help us understand how widgets work between the HMI and the code.
import os
from pathlib import Path
import sys


from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class GBWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        # self.xfmr_window.chatPB.clicked.connect(self.chat_pb_cb)

        # Callback function when button is pressed
        self.main_window.pushButton.clicked.connect(self.pushButtonCallBack)

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)

        # Make window a class memeber so it's accessible in other methods
        self.main_window = loader.load(ui_file, self)
        self.setWindowTitle("Hello From Greg")  # Sets title
        ui_file.close()

    def pushButtonCallBack(self):
        """
        Callback function to update text when pushbutton is pressed
        """
        print("Push button was pressed!")#added an exclaimation just to see the change.  This prints to a command window.

        # Get input text
        input_text = self.main_window.lineEdit.text()

        # Set output text
        self.main_window.lineEdit_2.setText(input_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GBWidget()
    widget.show()                                                                
    sys.exit(app.exec())
