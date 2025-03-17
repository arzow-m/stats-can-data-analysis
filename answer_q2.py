import csv
import sys

INPUT_DELIMITER = ","

csv_fh = open("q2_data.csv", "r")
csvdata = csv.reader(csv_fh, delimiter= INPUT_DELIMITER)

for row in csvdata:
    header = row
    break # extract header 

# create empty list to store results 
results = []

for row in csvdata:
    year = row[0]
    # slices off the last 6 chars + extra space (the random [XXXX] number sequence)
    occupation = row[2][:-7] 
    full_time = row[3]
    hourly_wage = row[5]

    # attempting to cast hourly_wage to a float 
    try:
        hourly_wage = float(hourly_wage)

    except IOError as err:
        print(f"Could not convert hourly wage into a float: {err}", file = sys.stderr)
        sys.exit(1)

    # create a list with all above into, append into result array
    results.append([year, occupation, full_time, hourly_wage])

# calculate total salaries in csv file 
total_salaries = 0
count = 0

for result in results:
    # calculate annual salary based on hourly wage 
    salary = ((((result[3] * 8) * 5) * 4) * 12)
    total_salaries += salary
    count += 1

average_salary = total_salaries / count

# attempting to cast average_salary to an int  
try:
    average_salary = int(average_salary)

except IOError as err:
    print(f"Could not convert total salary into a float: {err}", file = sys.stderr)
    sys.exit(1)

print(f"Average salary for {occupation} in {year}: {average_salary}$")
