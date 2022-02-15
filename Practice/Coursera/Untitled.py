import datetime

def is_vaild_date(year ,month ,day):
	test_date:datetime.date(year ,month ,date)
	if year < datetime.MINYEAR or year > datetime.MAXYEAR:
		print("Uh..Ohhh. Invalid Date - Bad Year")
	elif month < 0 or month > 12:
		print("Uh..Ohhh. Invalid Date - Bad Month")
	elif month == 2 and day >28
		print("Uh..Ohhh. Invalid Date - Bad Day")
	elif 
