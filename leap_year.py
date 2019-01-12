year = 2017
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("year is visokosnuy")
else:
    print("year is not visok")