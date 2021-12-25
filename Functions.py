def initialize(ui, db):
    pass

from PyQt5.QtSql import *

#判断某个table中的某col是否存在target值
def judge(table, col, target):
        #target = str(target)
        target = "'"+target+"'"
        query = QSqlQuery()
        sql = "SELECT EXISTS(SELECT * FROM {} WHERE {} = {}) as p".format(str(table), str(col), target)

        if query.exec(sql):
            t = query.record().indexOf('p')
            query.next()
            judge = query.value(t)

            if judge:
                return 1
            else:
                return 0
        else:
            return -1



def buy(ui):
    name = ui.input_name.text()
    nums = ui.input_nums.text()

    query = QSqlQuery()
    #price = None
    #ui.output_buylist.setText(str(name))
