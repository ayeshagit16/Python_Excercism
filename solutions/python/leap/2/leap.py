'''Determine whether a given year is a leap year.'''
def leap_year(year):
    '''
1.In every year that is evenly divisible by 4.
2. Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
'''
    flag = False
    if year%4 == 0:
        if year%100 != 0 and year%400 != 0:
            flag = True
        elif year%100 == 0 and year%400 == 0:
            flag = True
    return flag
