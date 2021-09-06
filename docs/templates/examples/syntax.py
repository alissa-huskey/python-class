"""My first program"""

import time
import shutil

size = shutil.get_terminal_size()
today = time.localtime()

greeting = "Hello"

if today.tm_hour < 11:
  greeting = "Good morning"  # before 12pm

# put together the message and make it centered
message = (greeting + " world!").center(size.columns)

print(message)
