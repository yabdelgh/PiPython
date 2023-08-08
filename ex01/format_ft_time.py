import datetime

tmp     = str("Seconds since January 1, 1970: ")
epoch   = datetime.datetime.now()
time    = epoch - datetime.datetime(1970, 1, 1)
time    = round(time.total_seconds(), 4)
myStr   = str(time).split(".")

i   = int(len(myStr[0]) % 3)
j   = int(0)

while (j < len(myStr[0])) :
    tmp += myStr[0][j:i]    
    if (i != len(myStr[0])) :
        tmp += ","
    else :
        tmp += "." + myStr[1] + " or "
    j = i
    i += 3

scientific_notation = f"{time:.2e}"

tmp += scientific_notation + " in scientific notation"

print(tmp)
print(epoch.strftime("%B %d %Y"))