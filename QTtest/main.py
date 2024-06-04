from PySide2.QtWidgets import *

from QueryAPI import QueryAPI
from ui.UI_ui import Ui_MainWindow
import os, sys


cur_dir = os.path.dirname(__file__)
sys.path.append(cur_dir)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("天气查询")
        self.text = ""
        self.pushButtonQuery.clicked.connect(self.query_weather)
        self.pushButtonQuit.clicked.connect(self.close)
        self.item_add()

    def item_add(self):
        self.comboBox.clear()
        file_path = "C:/Users/asus/Documents/Python code/QTtest/CityCode.txt"
        with open(file=file_path, mode="r", encoding="utf-8") as fp:
            try:
                lines = fp.readlines()
                i = 0
                line = ""
                fp.seek(0)
                while i < len(lines):
                    line = fp.readline()
                    s = line.split("=")
                    self.comboBox.addItem(str(s[1])[:-1], s[0])
                    i += 1
            except Exception as exp:
                print(str(exp))
            finally:
                fp.close()

    def query_weather(self):
        curText = self.comboBox.currentText()
        curData = str(self.comboBox.currentData())
        api = QueryAPI()
        re = api.get(curData)
        self.plainTextEdit.setPlainText(curText + curData + "\n" + str(re))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
