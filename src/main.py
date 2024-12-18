# 导入必要的模块
import sys
from PyQt5.QtWidgets import QApplication  # 导入Qt应用程序类
from ui.main_window import FakeConsole    # 导入主窗口类

def main():
    """
    主函数:初始化并运行应用程序
    """
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建主窗口实例
    ex = FakeConsole()
    # 显示主窗口
    ex.show()
    # 进入事件循环,并在退出时返回状态码
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 