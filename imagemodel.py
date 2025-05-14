from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QPixmap, QColor, QImage
import cv2
import numpy as np

class ImageModel(QObject):
    '''このクラスは画像のモデルを提供
    QObjectを継承
    Attributes:
        img(object)   : 画像(opencv)
        pixmap(object): 画面表示用pixmap
    Signals:
        pixmap_updated(pixmap): pixmapが変更され、画面表示を更新するときに通知
    '''
    pixmap_updated = Signal(object)
    def __init__(self):
        '''コンストラクタ
        '''
        super().__init__()
        self.img = None
    
    @Slot()
    def initial_update(self):
        '''初期画面を作成して、更新を通知
        '''
        pixmap = QPixmap(640, 480)
        pixmap.fill(QColor('white'))
        self.pixmap_updated.emit(pixmap)
        

    def update_pixmap(self, img):
            '''pixmapを更新して、通知
            Args:
                img(objrct): 更新用画像
            '''
            cimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, channels = cimg.shape
            bytes_per_line = channels * width
            qimg = QImage(cimg.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.pixmap_updated.emit(pixmap)
        
    @Slot(str, int, int)
    def open_image(self, fpath: str, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
        '''画像の読込み、pixmapを更新
        Args:
            fpath(str): ファイルパス
            flags(int): 読込みフラグ
            dtype(int): データタイプ
        '''
        try:
            n = np.fromfile(fpath, dtype)
            self.img = cv2.imdecode(n, flags)
            self.update_pixmap(self.img)
        except Exception as e:
            print(e)
