#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：吴洲
日期：2019.11.18
"""
print("欢迎使用RPSLS游戏")
print("--------")
player_choice=input("请输入你的选择：")
print("--------")
import random
comp_number=random.randint(0,4)
def  name_to_number(name):#将名字与数字一一对应
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="布":
		return 2
	elif  name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error: No Correct Name")
				
def number_to_name(number):#将数字转化为游戏对象
	if  number==0:
		return	"石头"
	elif number==1:
		return	"史波克"
	elif number==2:
		return	"布"
	elif number==3:
		return	"蜥蜴"
	elif number==4:
		return	"剪刀"
	else :
		print("Error: No Correct Name")
		
def  rpsls(player_choice):#玩家的选择
	print("你的选择是：%s"%(player_choice))
	player_choice= name_to_number(player_choice)#将玩家选择转换为对应的数字
	comp_choice=random.randrange(0,5)#电脑随机选择一个数代表电脑的选择
	print("电脑的选择是:%s"%(number_to_name(comp_choice)))
	if player_choice==0 and  (comp_choice==1 or comp_choice==2):#条件选择并输出结果
		print("你输了")
	elif player_choice ==1 and (comp_choice==2 or comp_choice==3):
		print("你输了")
	elif player_choice ==2 and  (comp_choice==3 or  comp_choice==4):
		print("你输了")
	elif player_choice ==3 and (comp_choice==0 or comp_choice==4):
		print("你输了")
	elif player_choice ==4 and (comp_choice==0 or comp_choice==1):
		print("你输了")
	elif player_choice ==0 and (comp_choice==3 or comp_choice==4):
		print("你赢了")
	elif player_choice ==1 and (comp_choice==0 or comp_choice==4):
		print("你赢了")
	elif player_choice ==2 and (comp_choice==0 or comp_choice==1):
		print("你赢了")
	elif player_choice ==3 and (comp_choice==1 or comp_choice==2):
		print("你赢了")
	elif player_choice ==4 and (comp_choice==2 or comp_choice==3):
		print("你赢了")
	elif player_choice == comp_choice:
		print("你和电脑选的是相同的，是平局")
rpsls(player_choice)#调用函数
