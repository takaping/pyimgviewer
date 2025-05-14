# PySide6を使ったImage Viewer
シングル・フレームウィンドウ型の画像ビューア
ファイルから画像を読み込み表示

## 環境
* Windows 11
* Python 3.12.7
* requirements.txtを参照

[OpenCVのライセンス](https://opencv.org/license/)

[PySideのライセンス](https://doc.qt.io/qtforpython-6/licenses.html)


## ソースファイル
| ファイル名 | 概要 |
|----------|------|
| imagemodel.py | 画像のモデルクラスを実装 |
| imageview.py | 画像のビュークラスを実装 |
| mainwindow.py | メインウィンドウクラスを実装 |
| pygui.py | メインプログラム<br>クラス間のSignsl, Slotの設定 |
｜mainwindow.ui | メインウィンドウのレイアウト<br>PySide6のパッケージフォルダ内の<br>designer.exeを使用 |
| ui_mainwindow.py | Scripts内のpyside6-uic.exeを<br>使用してmainwindow.uiから変換<br>mainwindow.py で使用 |


