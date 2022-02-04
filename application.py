from PySide6.QtWidgets import QApplication

from view.minimal_gui_main_window import MinimalGUIMainWindow


class MinimalGui(QApplication):
    def __init__(self) -> None:
        super().__init__()
        self._main_window: MinimalGUIMainWindow = MinimalGUIMainWindow()
        self._main_window.show()
