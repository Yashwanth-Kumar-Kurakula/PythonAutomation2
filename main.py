import random
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

curr_time =("date and time =", dt_string)

with open("useless_info.txt", "a+") as file:    
    # write a random number between 1 and 20 000
    # write the current date and time
    file.write(str(random.randint(0,20000)) + "\n")
    file.write(str(curr_time) + "\n")


