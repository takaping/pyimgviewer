import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from imagemodel import ImageModel
from imageview import ImageView


def main(app_name):
    # オブジェクトのインスタンス化
    app = QApplication(sys.argv)
    image_model = ImageModel()
    image_view = ImageView()
    main_window = MainWindow(app_name)
    # ビューをメインウィンドウに載せる
    main_window.setCentralWidget(image_view)
    # Connect signals and slots
    main_window.new_triggered.connect(image_model.initial_update)
    image_model.pixmap_updated.connect(image_view.update_view)
    main_window.fpath_changed.connect(image_model.open_image)
    # 初期ビューの更新
    image_model.initial_update()

    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app_name = 'Image Viewer'
    main(app_name)
