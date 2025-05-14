from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGraphicsView


class ImageView(QGraphicsView):
    '''このクラスは画像のビューを提供
    QGraphicsViewを継承
    Attributes:
        scene(object): QGraphicsSceneオブジェクト。ImageViewにセット
        item(object) : QGraphicsPixmapItemオブジェクト。sceneに追加
    '''
    def __init__(self):
        '''コンストラクタ
        '''
        self.scene = QGraphicsScene()
        super().__init__(self.scene)
        self.item = QGraphicsPixmapItem()
        self.scene.addItem(self.item)

    @Slot(object)
    def update_view(self, pixmap):
        '''ビューを更新
        Args:
            picmap(object): 表示するpicmap
        '''
        self.item.setPixmap(pixmap)
        self.scene.setSceneRect(self.item.boundingRect())
