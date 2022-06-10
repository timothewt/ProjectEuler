# 1 Jan 1901 was a tuesday

current_month = 0   # Jan 0, Feb 1, Mar 2, Apr 3, May 4, Jun 5, Jul 6, Aug 7, Sep 8, Oct 9, Nov 10, Dec 11
current_day = 1     # Monday 0, Tuesday 1, Wednesday 2, Thursday 3, Friday 4, Saturday 5, Sunday 6
starting_year = 1901
max_year = 2000

sunday_count = 0

for i in range(starting_year, max_year + 1):
    current_month = 0
    while current_month < 12:
        match current_month:
            case 3 | 5 | 8 | 10:
                current_day = (current_day + 30 % 7) % 7
            case 0 | 2 | 4 | 6 | 7 | 9 | 11:
                current_day = (current_day + 31 % 7) % 7
            case 1:
                if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                    current_day = (current_day + 29 % 7) % 7
                else:
                    current_day = (current_day + 28 % 7) % 7
        current_month += 1
        if current_day == 6:
            sunday_count += 1

print("Number of sundays between the 1st of January of", starting_year, "and 31st of December of", max_year, ":", sunday_count)
