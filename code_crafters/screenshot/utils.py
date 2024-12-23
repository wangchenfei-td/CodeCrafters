# -*- coding: utf-8 -*-

from PySide2 import QtGui, QtCore, QtWidgets


def get_screen_info():
    """
    获取屏幕信息
    """

    # 获取所有屏幕对象
    app = QtGui.QGuiApplication()
    screens = app.screens()
    if not screens:
        raise Exception("未检测到屏幕")

    # 屏幕信息
    screen_info = {
        "objects": screens,
        "count": len(screens),
        "geometry": QtCore.QRect(),
    }

    # 初始化屏幕的左上角和右下角坐标
    top_left_point = QtCore.QPoint()
    bottom_right_point = QtCore.QPoint()

    # 遍历所有屏幕对象
    for screen in screens:
        # 获取屏幕的几何信息
        screen_rect = screen.geometry()

        # 更新左上角坐标
        if screen_rect.x() < top_left_point.x():
            top_left_point.setX(screen_rect.x())
        if screen_rect.y() < top_left_point.y():
            top_left_point.setY(screen_rect.y())

        # 更新右下角坐标
        if screen_rect.x() + screen_rect.width() > bottom_right_point.x():
            bottom_right_point.setX(screen_rect.x() + screen_rect.width())
        if screen_rect.y() + screen_rect.height() > bottom_right_point.y():
            bottom_right_point.setY(screen_rect.y() + screen_rect.height())

    # 更新屏幕信息
    screen_info["geometry"] = QtCore.QRect(top_left_point, bottom_right_point)

    return screen_info


def get_screens_pixmap(screen_info=None):
    """
    获取屏幕截图Pixmap对象
    """

    # 获取屏幕信息
    screen_info = screen_info or get_screen_info()

    # 屏幕截图Pixmap对象
    pixmap = QtGui.QPixmap(
        screen_info["geometry"].width(),
        screen_info["geometry"].height()
    )
    pixmap.fill(QtCore.Qt.transparent)

    # 画笔Painter对象
    painter = QtGui.QPainter(pixmap)

    # 遍历所有屏幕对象
    for screen in screen_info["objects"]:
        # 获取屏幕的几何信息
        screen_rect = screen.geometry()

        # 获取屏幕截图
        screenshot = screen.grabWindow(0)

        # 计算截图在pixmap中的位置
        x = screen_rect.x() - screen_info["geometry"].x()
        y = screen_rect.y() - screen_info["geometry"].y()

        # 在pixmap上绘制截图
        painter.drawPixmap(x, y, screenshot)

    # 结束画笔
    painter.end()

    return pixmap
