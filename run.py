import sys

from PyQt6.QtWidgets import QApplication

from utils.MainWindow import MainWindow


# run the window
if __name__ == "__main__":
    # # disable font errors
    # warnings.filterwarnings('ignore')

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
