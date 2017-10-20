#!/usr/bin/env python
# -*- coding: UTF-8 -*-

f=open("receipt.txt","w")
good_list={}
class market(object):
    def  __init__(self,number,name,price):
        self.number=number
        self.name=name
        self.price=price
def  print_information(self):
    print("-"*30)
    print("商品编号：  ", self.number)
    print("商品名称：  ", self.name)
    print("商品价格：  ", self.price)
    print("-"*30)
def  add_a_good():
    self=input("请输入要添加的商品名称：")
    name=self
    number=int(input("请输入要添加的商品编号："))
    price=int(input("请输入要添加的商品价格："))
    if id in good_list.keys():
        print("系统中已有此商品，请勿重复添加！")
    else:
        self=market(number,name,price)
        good_list[number]=self
def  remove_a_good():
    number=int(input("请输入要删除的商品编号："))
    if number in good_list.keys():
        print("以下是你要删除的商品信息：")
        print_information(good_list[number])
        while True:
            flag=input("确定删除吗？请回复yes或no：")
            if flag=="yes":
                del good_list[number]
                print("成功删除该商品！")
                return
            elif flag=="no":
                return
            else:
                print("输入错误！请重新输入！")
    else:
        print("商品不存在！请重新输入！")
        remove_a_good()
def  cal():
    f.write("商品名    编号    单价    总价\n")
    shopping_list=[]
    number=0
    total=0
    while True:
        name=input("请输入你要购买的商品名称：")
        for key in good_list:
            if good_list[key].name==name:
                number=key
        if number==0:
            print("对不起，您想要的商品不存在")
        else:
            self=good_list[number]
            n=int(input("请输入要购买的数量："))
            Sum=n*self.price
            print("商品名：%s 单价：%d 数量：%d 总价：%d" % (self.name,self.price,n,Sum))
            f.write("%s        %d        %d       %d\n" % (self.name,self.price,n,Sum))
            total+=Sum
        flag=input("继续购买吗？回复yes或no:")
        if flag=="no":
            return total
def help():
    print("1:添加一个商品\n"
          "2:删除一个商品\n"
          "3:收银服务\n"
          "4:退出\n")
def main():
    while True:
        help()
        choice=int(input("欢迎来到超市收银平台！请问你想做什么呢？"))
        if choice==1:
            add_a_good()
        elif choice==2:
            remove_a_good()
        elif choice==3:
            x=cal()
            print("您本次消费金额为：",x)
            f.write("\n您本次消费总额是：%d\n" % x)
            f.close()
        elif choice==4:
            SystemExit
        else:
            print("对不起，您输入的指令不存在！")
main()                
                
