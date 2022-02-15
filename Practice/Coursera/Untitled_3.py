import math
Turn_Count = 1
money = 5
while money <= 300:
	for turns in range(0,30):
		Turn_Count += 1
		money = int(math.ceil((money * 1.5)+money))
		print("Turn Count:"+str(Turn_Count)+" |Money at This Turn:"+str(money))
