"""Countdown exercise for the CLI Lesson
   https://alissa-huskey.github.io/python-class/lessons/cli.html
"""
import sys
import time

count = 3

if len(sys.argv) >= 2:
  count = int(sys.argv[1])

for num in range(count, 0, -1):
    print(f"{num}...")
    time.sleep(1)
