import sys

from PyQt5.QtGui import QPixmapCache
from PyQt5.QtWidgets import QApplication
import os

from media_objects_47.widgets.media_object_main_window import MediaObjectMainWindow


def excepthook(excType, excValue, tracebackobj):
    print(excType, excValue, tracebackobj)


sys.excepthook = excepthook

def main():
    app = QApplication(sys.argv)
    win = MediaObjectMainWindow()
    cache_size_in_kb = 300 * 10 ** 3
    QPixmapCache.setCacheLimit(cache_size_in_kb)

    win.show()

    default_action = win.load_actions[list(win.load_actions.keys())[0]]
    # filepathes = [
    #                  '/home/dimathe47/data/geo_tiny/Segm_RemoteSensing1/jpg-png/poligon_minsk_1_yandex_z18_train_0_0.jpg',
    #                  '/home/dimathe47/data/geo_tiny/Segm_RemoteSensing1/jpg-png/poligon_minsk_1_yandex_z18_train_0_0.png'] * 4
    # dirpath = '/home/dimathe47/Downloads/Mountains'
    dirpath = r'C:\Users\DIMA\Google Диск\Pictures\Mountains'
    filepathes = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    default_action.update_list_model(filepathes)
    default_action.setChecked(True)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
