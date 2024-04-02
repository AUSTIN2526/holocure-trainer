from PyQt5.QtCore import QThread, QTimer, pyqtSignal

class ModifyThread(QThread):
    modification_signal = pyqtSignal()

    def __init__(self, checkbox=None, data=None, game_module=None, windows=None):
        super(ModifyThread, self).__init__()
        self.checkbox = checkbox
        self.data = data
        self.game_module = game_module
        self.windows = windows
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.modify_data)

    def run(self):
        self.timer.start(1)  # Give a delay; too low a value may cause modification function to fail

    def modify_data(self):
        if not self.checkbox.isChecked():
            self.timer.stop()
            return

        value, address, offsets = self.data.values()
        try:
            addr = self.calculate_address(self.game_module + address, offsets)
            if self.windows.read_double(addr) != value:
                self.windows.write_double(addr, value)
                self.modification_signal.emit()
        except Exception as e:
            pass

    def calculate_address(self, address, offsets):
        addr = self.windows.read_longlong(address)
        for index, offset in enumerate(offsets):
            if index + 1 != len(offsets):
                addr = self.windows.read_longlong(addr + offset)
        return addr + offsets[-1]