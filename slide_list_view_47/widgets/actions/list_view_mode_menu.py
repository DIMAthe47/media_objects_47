from typing import Callable

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction, QGroupBox, QHBoxLayout, QLineEdit, QFormLayout, QDialog, QDialogButtonBox, \
    QVBoxLayout, QMenu, QActionGroup, QStyledItemDelegate, QMenuBar

from slide_list_view_47.model.role_funcs import decoration_size_func_factory, slideviewparams_to_pixmap, \
    slidepath_to_pximap, slideviewparams_to_str
from slide_list_view_47.model.slide_list_model import SlideListModel
from slide_list_view_47.widgets.actions.item_mode_menu import ItemModeMenu
from slide_list_view_47.widgets.actions.on_change_view_mode_action import OnChangeViewModeAction
from slide_list_view_47.widgets.actions.on_icon_max_size_or_ratio_action import OnIconMaxSizeOrRatioAction
from slide_list_view_47.widgets.slide_list_widget import SlideListWidget
from slide_list_view_47.widgets.slide_viewer_delegate import SlideViewerDelegate
from slide_viewer_47.common.slide_view_params import SlideViewParams


class ListViewModeMenu(QMenu):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.window = None
        if isinstance(parent, QMenu) or isinstance(parent, QMenuBar):
            self.window = parent.parent()
            parent.addMenu(self)

        self.slide_list_widget: SlideListWidget = None

    def set_slide_list_widget(self, slide_list_widget: SlideListWidget):
        self.slide_list_widget = slide_list_widget
        self.clear()
        icon_max_size_or_ratio_action = OnIconMaxSizeOrRatioAction("change icon_size_or_ratio", self,
                                                                   self.slide_list_widget)
        change_view_mode_action = OnChangeViewModeAction("change view mode", self, self.slide_list_widget.list_view)

        self.on_change_mode_menu = ItemModeMenu("change mode", self)
        self.on_change_mode_menu.set_slide_list_widget(self.slide_list_widget)
