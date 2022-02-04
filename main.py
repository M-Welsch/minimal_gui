import sys
from PySide2.QtCore import QCoreApplication, Qt

from application import MinimalGui


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = MinimalGui()
    sys.exit(app.exec_())
