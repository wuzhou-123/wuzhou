#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2019.11.18
"""
print("��ӭʹ��RPSLS��Ϸ")
print("--------")
player_choice=input("���������ѡ��")
print("--------")
import random
comp_number=random.randint(0,4)
def  name_to_number(name):#������������һһ��Ӧ
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="��":
		return 2
	elif  name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error: No Correct Name")
				
def number_to_name(number):#������ת��Ϊ��Ϸ����
	if  number==0:
		return	"ʯͷ"
	elif number==1:
		return	"ʷ����"
	elif number==2:
		return	"��"
	elif number==3:
		return	"����"
	elif number==4:
		return	"����"
	else :
		print("Error: No Correct Name")
		
def  rpsls(player_choice):#��ҵ�ѡ��
	print("���ѡ���ǣ�%s"%(player_choice))
	player_choice= name_to_number(player_choice)#�����ѡ��ת��Ϊ��Ӧ������
	comp_choice=random.randrange(0,5)#�������ѡ��һ����������Ե�ѡ��
	print("���Ե�ѡ����:%s"%(number_to_name(comp_choice)))
	if player_choice==0 and  (comp_choice==1 or comp_choice==2):#����ѡ��������
		print("������")
	elif player_choice ==1 and (comp_choice==2 or comp_choice==3):
		print("������")
	elif player_choice ==2 and  (comp_choice==3 or  comp_choice==4):
		print("������")
	elif player_choice ==3 and (comp_choice==0 or comp_choice==4):
		print("������")
	elif player_choice ==4 and (comp_choice==0 or comp_choice==1):
		print("������")
	elif player_choice ==0 and (comp_choice==3 or comp_choice==4):
		print("��Ӯ��")
	elif player_choice ==1 and (comp_choice==0 or comp_choice==4):
		print("��Ӯ��")
	elif player_choice ==2 and (comp_choice==0 or comp_choice==1):
		print("��Ӯ��")
	elif player_choice ==3 and (comp_choice==1 or comp_choice==2):
		print("��Ӯ��")
	elif player_choice ==4 and (comp_choice==2 or comp_choice==3):
		print("��Ӯ��")
	elif player_choice == comp_choice:
		print("��͵���ѡ������ͬ�ģ���ƽ��")
rpsls(player_choice)#���ú���
