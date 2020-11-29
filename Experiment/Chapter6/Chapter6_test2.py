class Goods:
    def __init__(self, na, anum=0, snum=0, p_price=0, s_price=0):
        self.name = na
        self.all_number = anum
        self.sell_number = snum
        self.purchase_price = p_price
        self.sell_price = s_price

    def __str__(self):
        if self.sell_number:
            info = "商品名称:%s\t销售数量:%d\t出售价格:%d元/单品" % (self.name, int(self.sell_number), self.sell_price)
            return info
        else:
            info = "商品名称:%s\t商品数量:%d\t进货价格:%d元/单品" % (self.name, int(self.all_number), self.purchase_price)
            return info


class Supermarket:
    def __init__(self):
        self.goodsdict = {}
        self.selldict = {}

    def addGoods(self):

        id = input("请输入添加商品编号:")
        if self.goodsdict.get(id):
            print("商品编号已存在，请重新输入！")
            return
        name = input("请输入商品名称:\n")
        num = eval(input("请输入商品数量:\n"))
        p_price = int(input("请输入添加商品进货价格:\n"))
        good = Goods(name, anum=num, p_price=p_price)
        self.goodsdict[id] = good
        print("添加成功！")

    def showGoods(self):

        print("=" * 40)
        for key in self.goodsdict.keys():
            good = self.goodsdict[key]
            print(good)
        print("=" * 40)

    def deleteGoods(self):

        id = input("请输入删除商品编号:")
        if self.goodsdict.get(id):
            del self.goodsdict[id]
            print("删除成功！")
        else:
            print("商品编号不存在！")

    def sellGoods(self):
        self.showGoods()
        id = input("请输入出售商品编号:")
        if self.goodsdict.get(id):
            print(self.goodsdict[id])
        else:
            print("商品编号不存在!")
            return
        name = input("请输入商品名称:\n")
        num = eval(input("请输入商品数量:\n"))
        s_price = int(input("请输入出售价格:\n"))
        sell_good = Goods(name, snum=num, s_price=s_price)
        self.selldict[id] = sell_good
        print("销售成功！")

    def updateGoods(self):
        self.showGoods()
        id = input("请输入要修改的商品编号:")
        if self.goodsdict.get(id):
            print(self.goodsdict[id])
        else:
            print("商品编号不存在!")
            return
        name = input("请输入商品名称:\n")
        num = eval(input("请输入商品数量:\n"))
        p_price = int(input("请输入商品进货价格:\n"))
        good = Goods(name, anum=num, p_price=p_price)
        self.goodsdict[id] = good
        print("修改成功！")

    def sum(self):
        for i in self.selldict.keys():
            print(self.selldict[i])

    def mainMenu(self):
        info = """
        ==========欢迎使用简易超市进销存管理系统==========
            输入功能编号，您可以选择以下功能：
            输入“1”：显示商品的信息
            输入“2”：添加商品的信息
            输入“3”：删除商品的信息
            输入“4”：修改商品信息
            输入“5”：出售商品
            输入“6”：汇总出售信息
            输入“-1”：退出系统功能
        ==========================================
        """
        print(info)
        while True:
            code = input("请输入功能编号:")
            if code == "1":
                self.showGoods()
            elif code == "2":
                self.addGoods()
            elif code == "3":
                self.deleteGoods()
            elif code == "4":
                self.updateGoods()
            elif code == "5":
                self.sellGoods()
            elif code == "6":
                self.sum()
            elif code == "-1":
                print("感谢您的使用，正在退出系统！！")
                break
            else:
                print("输入编号有误，请重新输入！！")


if __name__ == '__main__':
    shop = Supermarket()
    shop.mainMenu()
