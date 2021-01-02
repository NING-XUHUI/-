import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口尺寸
        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CenterForm()
    main.center()
    main.show()
    sys.exit(app.exec_())
