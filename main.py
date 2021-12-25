import sys
from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login import Ui_login as ui_login
from user_Interface import Ui_userInterface as ui_userinterface
from root_interface import Ui_rootinterface as ui_rootinterface

from Functions import *


def view_data(ui):
    ui.model = QSqlTableModel()
    ui.list_shoplist.setModel(ui.model)

    ui.model.setTable('shoplist')
    # ui.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # 允许字段更改
    ui.model.select()  # 查询所有数据
    # 设置表格头
    ui.model.setHeaderData(0, Qt.Horizontal, 'name')
    ui.model.setHeaderData(1, Qt.Horizontal, 'inventory')
    ui.model.setHeaderData(2, Qt.Horizontal, 'price')


class LoginWindow(QMainWindow, ui_login):
    switch_Windows = pyqtSignal();

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.button_commit.clicked.connect(self.gointerface)

    def gointerface(self):
        self.switch_Windows.emit()


class UserWindow(QMainWindow, ui_userinterface):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.setupUi(self)
        view_data(self)
        self.button_buy.clicked.connect(partial(buy, self))


class RootWindow(QMainWindow, ui_rootinterface):

    def __init__(self):
        super(RootWindow, self).__init__()
        self.setupUi(self)
        view_data(self)
        self.button_commit.clicked.connect(partial(add, self))


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_Windows.connect(self.judge_role)
        self.login.show()

    def judge_role(self):
        name = self.login.input_userName.text()
        password = self.login.input_Password.text()

        name = "'"+name+"'"
        password = "'" + password + "'"


        query = QSqlQuery()
        sql = "SELECT EXISTS(SELECT * FROM login WHERE USER = {} AND PASSWORD = {}) as p;".format(name, password)

        if query.exec(sql):
            t = query.record().indexOf('p')
            query.next()
            judge = query.value(t)


        if judge:
            query = QSqlQuery()
            sql = "SELECT ROLE FROM LOGIN WHERE USER = {}".format(name)
            query.exec(sql)
            t = query.record().indexOf('role')
            query.next()
            role = query.value(t)

            if role == 'user':
                self.show_user_interface()
            else:
                self.show_root_interface()
        else:
            return

    def show_user_interface(self):
        self.user_interface = UserWindow()
        self.login.close()
        self.user_interface.show()

    def show_root_interface(self):
        self.root_interface = RootWindow()
        self.login.close()
        self.root_interface.show()


def main():
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('flowerWarehouse.sqlite')


    if not db.open():
        print('无法建立与数据库的连接')
        return False

    controller = Controller()  # 控制器实例
    controller.show_login()  # 登录界面
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
