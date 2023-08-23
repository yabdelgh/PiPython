import datetime

output     = "Seconds since January 1, 1970: {}.{} or {} in scientific notation"
epoch   = datetime.datetime.now()
time    = epoch - datetime.datetime(1970, 1, 1) # unix epoch
time    = round(time.total_seconds(), 4)
myStr   = str(time).split(".")

i   = int(len(myStr[0]) % 3)
j   = int(0)

tmp = ""
while (j < len(myStr[0])) :
    tmp += myStr[0][j:i]    
    if (i != len(myStr[0])) :
        tmp += ","
    j = i
    i += 3

print(output.format(tmp, myStr[1], f"{time:.2e}"))
print(epoch.strftime("%B %d %Y"))