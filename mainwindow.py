import os
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    '''このクラスメインウィンドウを提供
    QMainWindow, Ui_MainWindowを継承
    Attributes:
        app_name(str): アプリケーション名
    Signals:
        fpath_changed(ファイルパス): ファイルパスが変わったことを通知
    '''
    new_triggered = Signal()
    fpath_changed = Signal(str)
    def __init__(self, app_name):
        '''コンストラクタ
        '''
        super().__init__()
        self.setupUi(self)
        self.app_name = app_name
        self.setWindowTitle(self.app_name)

        # connect signals and slots
        self.action_Quit.triggered.connect(self.on_quit)
        self.action_New.triggered.connect(self.new_triggered.emit)
        self.action_Open.triggered.connect(self.on_file_open)

    def closeEvent(self, event):
          event.accept()

    @Slot()
    def on_quit(self):
        '''アプリケーション終了処理
        '''
        self.close()
    
    @Slot()
    def on_file_open(self):
            '''ファイルを開く処理
            ファイル選択ダイアログを表示して指定したファイルパスを取得し、ファイルパスが変わったことを通知
            '''
            dlg = QFileDialog(self)
            dlg.setFileMode(QFileDialog.ExistingFile)
            dlg.setNameFilter("Image files (*.bmp *.png *.jprg *.jpg *.jpe *.tiff *.tif);; all files (*.*)")
            dlg.setViewMode(QFileDialog.Detail)
            if dlg.exec_():
                    fpath = dlg.selectedFiles()
                    self.setWindowTitle(self.app_name + os.path.basename(fpath[0]))
                    self.fpath_changed.emit(fpath[0])
