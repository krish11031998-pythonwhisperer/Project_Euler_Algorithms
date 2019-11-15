Months = {'Jan':31,'Feb':[28,29],'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
fol_days = {'Sunday':['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'], 'Monday':['Tuesday','Wednesday','Thrusday','Friday','Saturday'],'Tuesday':['Wednesday','Thrusday','Friday','Saturday'],'Wednesday':['Thrusday','Friday','Saturday'],'Thrusday':['Friday','Saturday'],'Friday':['Saturday']}
days_in_week = ['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']

def days_in_year(type = 'normal'):
	Days_months_years = [1]
	if type == 'normal':
		no_days_year = 365
	else:
		no_days_year = 366

	counter = 0
	for x in Months.keys():
		if x == 'Feb':
			if type == 'leap':
				Days_months_years.append((Months[x][1]+Days_months_years[counter]))
			else:
				Days_months_years.append((Months[x][0]+Days_months_years[counter]))
		else:
			if (Months[x]+Days_months_years[counter]) <= no_days_year:
				Days_months_years.append((Months[x]+Days_months_years[counter]))


		counter+=1

	print("First days in the month wrt to {} is {}".format(no_days_year,Days_months_years))
	return Days_months_years

#
# def normal_year(first_day):
#
# for x,y in zip(3)


def check_leap_year(year):

	if year == 2000:
		if year%400 == 0:
			return 'leap'
	elif year%4 == 0:
		return 'leap'
	else:
		return 'normal'


def days_in_the_year(start,year):
	sunday_month_start = 0
	type = check_leap_year(year)
	month_first_day_check = days_in_year(type)

	if type == 'normal':
		no_days_year = 365
	else:
		no_days_year = 366

	days_year = []
	if start in fol_days.keys():
		days_year.append(start)
		for day in fol_days[start]:
			days_year.append(day)
	else:
		days_year.append(days_in_week)

	for x in range((no_days_year - len(days_year))//7):
		for day in days_in_week:
			days_year.append(day)

	remaining_days = no_days_year - len(days_year)
	for day in days_in_week[:remaining_days]:
		days_year.append(day)

	last_day = days_year[len(days_year)-1]

	if last_day != 'Saturday':
		next_day_year = fol_days[last_day][0]
	else:
		next_day_year = 'Sunday'


	for day_no in month_first_day_check:
		if days_year[day_no-1] == 'Sunday':
			sunday_month_start+=1


	return (days_year,next_day_year,sunday_month_start)

if __name__ == '__main__':
	total_sunday_month_start = 0
	next_day_year = 'Tuesday'
	for x in range(1901,2001):
		days_in_year_arr , next_day_year ,sunday_month_start = days_in_the_year(next_day_year,x)
		print('Year {}: {} number of starting with Sunday and day the next year will be starting is {} '.format(x,sunday_month_start,next_day_year))
		total_sunday_month_start += sunday_month_start
		print(total_sunday_month_start)





