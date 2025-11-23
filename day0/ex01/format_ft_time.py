import time
from datetime import datetime

now = time.time()

formatted = f"{now:,.2f}"

sci = f"{now:.2e}"

print(f"Seconds since January 1, 1970: {formatted} or {sci} in scientific notation")

today = datetime.now()
print(today.strftime("%b %d %Y"))