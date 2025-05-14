#made by lunatrionia with <3
#version 0.0.1

import os
import time
from desktop_notifier import DesktopNotifier
from tqdm import tqdm
import asyncio

notifier = DesktopNotifier()
async def main():
    await notifier.send(title="timer ended", message="shutting down")

#print("welcome, what would you like to do?")
#userAction = input(">")

userAction = "timer"

if userAction == "timer":
    print("how long do you want the timer to be? (in seconds)")

    while True:
        timerLength = input(">")

        if timerLength.isdigit() and int(timerLength) != 0:
            timerLength = int(timerLength)
            print(f"set timer for {timerLength} seconds")

            for i in tqdm(range(timerLength), desc="timer running"):
                time.sleep(1)

            print("your time has ended, goodbye")
            print("shutting down in 5 seconds...")
            asyncio.run(main())
            time.sleep(5)
            os.system("shutdown now")
            break

        print("invalid input, try again")
