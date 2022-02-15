"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.


Be sure to read the project description page for further information
about the expected behavior of the program.

"""
import datetime

def days_in_month(year, month):
    """

    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month <= 0:
        print('Invaild Year')
        return (0, False)
    elif month != 12:
        month_start=datetime.date(year,month,1)
        month_end=datetime.date(year,month+1,1)
        results=(month_end-month_start)
        print(results.days)
        return results.days
    else:
        month_start=datetime.date(year,month,1)
        dec_month_end=datetime.date(year+1,1,1)
        results=(dec_month_end-month_start)
        print(results.days)
        return results.days

days_in_month(2005,2);

def is_valid_date(year, month, day):
    """

    Function to access validfity of given date.
    Inputs:
    year  - an integer representing the year
    month - an integer representing the month
    day   - an integer representing the day

    Returns:
    True if year-month-day is a valid date and False otherwise
    """
    #test_date = datetime.date(year,month,day)
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        print("Uh..Ohhh. Invalid Date - Bad Year")
        return False
    elif month < 0 or month > 12:
        print("Uh..Ohhh. Invalid Date - Bad Month")
        return False
    elif day > days_in_month(year, month):
        print("Uh..Ohhh. Invalid Date - Bad Day")
        return False
    elif day <= 0:
        print("Uh..Ohhh. Invalid Date - Bad Day")
        return False
    # elif month in [4,6,9,11] and day > 30:
    #     print("Uh..Ohhh. Invalid Date - Bad Day")
    #     return False
    # elif month == 2 and day > 28:
    #     print("Uh..Ohhh. Invalid Date - Bad Day")
    else:
        print('Good Job - Date is Vaild')
        return True


#is_valid_date(1400, 1, 0);
def days_between(year1, month1, day1, year2, month2, day2):
    """

    Inputs:
    year1  - an integer representing the year of the first date
    month1 - an integer representing the month of the first date
    day1   - an integer representing the day of the first date
    year2  - an integer representing the year of the second date
    month2 - an integer representing the month of the second date
    day2   - an integer representing the day of the second date

    Returns:
    The number of days from the first date to the second date.
    Returns 0 if either date is invalid or the second date is
    before the first date.
    """
    if (year1 < datetime.MINYEAR or year1 > datetime.MAXYEAR) or (year2 < datetime.MINYEAR or year2 > datetime.MAXYEAR):
        print(0)
        return 0
    elif(month1 <= 0 or month1 > 12) or (month2 <= 0 or month2 > 12):
        print(0)
        return 0
    elif (day1 > days_in_month(year1,month1) or day1 <= 0) or (day2 > days_in_month(year2,month2) or day2 <= 0):
        print(0)
        return 0
    else:
        begin_date = datetime.date(year1, month1, day1)
        end_date = datetime.date(year2, month2, day2)
        days_between_results = (end_date - begin_date).days
    if days_between_results < 0:
        print(0)
        return 0
    else:
        print(days_between_results)
        return (days_between_results)

#days_between(20000, 1, 1, 2047, 8, 2);

def age_in_days(year, month, day):
   """

   Inputs:
     year  - an integer representing the birthday year
     month - an integer representing the birthday month
     day   - an integer representing the birthday day

   Returns:
     The age of a person with the input birthday as of today.
     Returns 0 if the input date is invalid or if the input
     date is in the future.
   """
   if (year < datetime.MINYEAR) or (year > datetime.MAXYEAR) or (month <= 0 or month > 12) or  (day <= 0 or day > days_in_month(month, year)):
      print(0)
      return 0
   else:
      birthday = datetime.date(year, month, day)
      today = datetime.date.today()
      days_aged = (today-birthday)
      results_of_age_in_days= int(days_aged.days)
   if results_of_age_in_days < 0:
      print(0)
      return 0
   else:
     print(results_of_age_in_days)
     return (results_of_age_in_days)
  # print(days_aged.days)
  # return days_aged.days

age_in_days(2017, 1, 1)
age_in_days(0, 1, 21);
