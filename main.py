import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QLabel,
    QHBoxLayout, QRadioButton, QVBoxLayout, QDialog, QWidget, QListWidget, QListWidgetItem,
     QButtonGroup, QBoxLayout, QMainWindow, QGroupBox, QGridLayout, QTextBrowser, QScrollArea,
     QFrame, QSizePolicy, QComboBox
    )
from PySide6.QtCore import Qt
from utils import zhongyao, yijing
import re
import warnings
from collections import deque

warnings.filterwarnings('ignore')

zhongyao_example = '草 | 血痹'
yijing_example = '坎 | 010 | 010010'
hist_max = 50

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        grid:QGridLayout = QGridLayout()

        # 搜索结果list，左下角
        searchResultList:QGroupBox = QGroupBox('搜索结果列表')
        wrapVBox = QVBoxLayout();
        self.resultListScroll = QScrollArea()
        self.resultListVBox:QVBoxLayout = QVBoxLayout();
        wrapVBox.addWidget(self.resultListScroll)
        searchResultList.setLayout(wrapVBox)
        self.resultListScroll.setFrameShape(QFrame.NoFrame)
        wrapVBox.setContentsMargins(0, 0, 0, 0)

        self.searchResultContent:QTextBrowser = QTextBrowser(self)

        # 搜索框前面的下拉选项卡
        self.comboBox = QComboBox()
        self.comboBox.addItems(['中药', '易经'])
        # self.comboBox.changeEvent(self.onComboBoxChanged)
        self.comboBox.currentTextChanged[str].connect(self.onComboBoxChanged)

        # grid.addWidget(QWidget(), 0, 0, 1, 0);
        grid.addWidget(self.createSearchRegion(), 0, 0, 1, -1);
        grid.addWidget(searchResultList, 1, 0);
        grid.addWidget(self.searchResultContent, 1, 1);

        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 8)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 4)
        self.setLayout(grid);

        self.setWindowTitle("中华传统词典");
        self.resize(700, 500);

        self.search_history = deque(maxlen=hist_max)
        self.current_index = -1
    
    def createSearchRegion(self) -> QGroupBox:
        groupBox:QGroupBox = QGroupBox("");

        # 回退前进按钮
        bbutton = QPushButton("<")
        bbutton.clicked.connect(self.searchBack)
        bbutton.setFixedSize(25, 20)

        fbutton = QPushButton(">")
        fbutton.clicked.connect(self.searchFront)
        fbutton.setFixedSize(25, 20)

        # 搜索框
        self.search_edit = QLineEdit(zhongyao_example)
        # 搜索按钮
        button = QPushButton("搜索")
        button.setShortcut('return')
        button.clicked.connect(self.search(flag='now'))

        hbox:QHBoxLayout = QHBoxLayout();
        hbox.addWidget(bbutton);
        hbox.addWidget(fbutton);
        hbox.addWidget(self.comboBox)
        hbox.addWidget(self.search_edit);
        hbox.addWidget(button);
        
        groupBox.setLayout(hbox);
        
        return groupBox

    def searchBack(self):
        if not self.search_history:
            return
        if self.current_index > 0:
            self.current_index -= 1
        searchField, text = self.search_history[self.current_index]
        self.search_edit.setText(text)
        self.comboBox.setCurrentText(searchField)
        self.search(flag='back')()

    def searchFront(self):
        if not self.search_history:
            return
        if self.current_index < (len(self.search_history)-1):
            self.current_index += 1
        searchField, text = self.search_history[self.current_index]
        self.search_edit.setText(text)
        self.comboBox.setCurrentText(searchField)
        self.search(flag='front')()

    def search(self, flag='now'):
        def tmp():
            text = self.search_edit.text().strip()       
            searchField = self.comboBox.currentText()
            if flag == 'now':
                self.current_index = len(self.search_history)
                self.search_history.append((searchField, text))

            # 清空之前的结果
            item_list = list(range(self.resultListVBox.count()))
            item_list.reverse()

            for i in item_list:
                item = self.resultListVBox.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
                self.resultListVBox.removeItem(item)

            self.changeResultContent("")()

            show_list = []
            if searchField == '中药':
                item_list = zhongyao[zhongyao['名称'].str.contains(text)].values.tolist() + \
                            zhongyao[zhongyao['神农本草经文'].str.contains(text)].values.tolist() + \
                            zhongyao[zhongyao['功效与主治'].str.contains(text)].values.tolist()
                for pinglei, leixing, name, xingwei, shennong, gongxiao in item_list:
                    show_list.append((name, '\n\n'.join([f'【{leixing}】{name}', f'【{pinglei}】神农本草经\n\n{xingwei}{shennong}', f'【主治与功效】\n\n{gongxiao}'])))
            elif searchField == '易经':
                if re.match(r'[01]{6,7}', text):
                    item_list = yijing[yijing['二进制卦'] == text].values.tolist()
                if re.match(r'[01]{3,4}', text):
                    item_list = yijing[yijing['二进制卦'].str.startswith(text) | yijing['二进制卦'].str.endswith(text)].values.tolist()
                elif re.match(r'\d{1,3}', text):
                    item_list = yijing[yijing['序号'] == text].values.tolist()
                else:
                    item_list = yijing[yijing['名称'].str.contains(text)].values.tolist()

                for idx, tp, name, pinyin, bina, img_disc, img, tuan in item_list:
                    if tp == '六十四卦':
                        show_list.append((f'[64卦]{name}', '\n\n'.join([f'{idx}', f'[ {pinyin} ]', f'{name}', bina, f'<span style=”font-size:20px”>{img}</span>', img_disc, f'【彖辞】\n\n{tuan}'])))
                    elif tp == '八卦':
                        show_list.append((f'[8卦]{name}', '\n\n'.join([f'{idx}', f'[ {pinyin} ]', f'{name}', bina, img])))

            for j, (name, content) in enumerate(show_list):
                radio:QRadioButton = QRadioButton(name);
                radio.clicked.connect(self.changeResultContent(content))
                if j == 0:
                    radio.setChecked(True)
                    self.changeResultContent(content)()
                self.resultListVBox.addWidget(radio)

            widgetContainer = QWidget()
            widgetContainer.setLayout(self.resultListVBox)
            self.resultListScroll.setWidget(widgetContainer)
        return tmp

    def changeResultContent(self, content):
        def tmp():
            self.searchResultContent.setText(content)
        return tmp

    def onComboBoxChanged(self, searchField):
        # searchField = self.comboBox.currentText()
        if searchField == '中药':
            self.search_edit.setText(zhongyao_example)
        elif searchField == '易经':
            self.search_edit.setText(yijing_example)


if __name__ == "__main__":
    app = QApplication()

    w = Window()
    w.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())