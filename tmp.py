import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QLabel,
    QHBoxLayout, QRadioButton, QVBoxLayout, QDialog, QWidget, QListWidget, QListWidgetItem,
     QButtonGroup, QBoxLayout, QMainWindow, QGroupBox, QGridLayout
    )
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        grid:QGridLayout = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0);
        # grid->addWidget(createSecondExclusiveGroup(), 1, 0);
        # grid->addWidget(createNonExclusiveGroup(), 0, 1);
        # grid->addWidget(createPushButtonGroup(), 1, 1);
        self.setLayout(grid);

        self.setWindowTitle("Group Boxes");
        self.resize(480, 320);

    def createFirstExclusiveGroup(self) -> QGroupBox:
        groupBox:QGroupBox = QGroupBox("Exclusive Radio Buttons");

        radio1:QRadioButton = QRadioButton("&Radio button 1");
        radio2:QRadioButton = QRadioButton("R&adio button 2");
        radio3:QRadioButton = QRadioButton("Ra&dio button 3");

        radio1.setChecked(True);

        vbox:QVBoxLayout = QVBoxLayout();
        vbox.addWidget(radio1);
        vbox.addWidget(radio2);
        vbox.addWidget(radio3);
        vbox.addStretch(1);
        
        groupBox.setLayout(vbox);
        
        return groupBox


if __name__ == "__main__":
    app = QApplication()

    w = Window()
    w.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())