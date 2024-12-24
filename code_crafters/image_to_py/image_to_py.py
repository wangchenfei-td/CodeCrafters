# -*- coding: utf-8 -*-


def image_to_py(image_path, py_file_path, variable_name):
    """
    将图片转换为py文件
    """

    # 读取图片数据
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # 将字节数据转换为十六进制字符串
    image_data = image_data.hex()

    # 创建Python文件并写入数据
    with open(py_file_path, "w") as py_file:
        py_file.write("%s = bytes.fromhex('%s')\n" % (variable_name, image_data))


if __name__ == "__main__":
    image_to_py(
        "C:/Users/admin/Downloads/选择区域.png", "select_area.py", "select_area"
    )
