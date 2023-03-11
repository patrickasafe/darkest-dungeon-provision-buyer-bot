import threading

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from utils.LabelledIntField import LabelledIntField

from utils.buy_provisions import buy_provisions

from configs import GAME_SCREEN_RESOLUTION

event = threading.Event()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # window title
        self.title = "Provision Bot"

        # window geometry
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.icon_name = "./utils/icon.png"

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon_name))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()

        wid = QWidget(self)
        self.setCentralWidget(wid)

        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)

        wid.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.group_box = QGroupBox("Game Resolution")
        grid_layout = QGridLayout()

        # # width resolution label
        # label_x = QLabel()
        # label_x.setText('Width Resolution')
        # grid_layout.addWidget(label_x, 0, 0,)

        # width resolution input
        self.input_x = LabelledIntField(
            'Width Resolution', GAME_SCREEN_RESOLUTION[0])
        grid_layout.addWidget(self.input_x, 1, 0,)

        # # height resolution label
        # label_y = QLabel()
        # label_y.setText('Height Resolution')
        # grid_layout.addWidget(label_y, 0, 1,)

        # height resolution input
        self.input_y = LabelledIntField(
            'Height Resolution', GAME_SCREEN_RESOLUTION[1])
        grid_layout.addWidget(self.input_y, 1, 1,)

        # start button
        start_button = QPushButton("Start")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.start_threading)
        grid_layout.addWidget(start_button, 3, 0)

        # stop button
        stop_button = QPushButton("Stop")
        stop_button.setCheckable(True)
        stop_button.clicked.connect(self.stop_process)
        grid_layout.addWidget(stop_button, 3, 1)

        self.group_box.setLayout(grid_layout)

    def start_threading(self):
        threading.Thread(target=self.run_process, daemon=True).start()

    def run_process(self):
        event.set()

        while event.is_set():
            GAME_SCREEN_RESOLUTION[0] = self.input_x.getValue()
            GAME_SCREEN_RESOLUTION[1] = self.input_y.getValue()
            buy_provisions()


    def stop_process(self):
        event.clear()