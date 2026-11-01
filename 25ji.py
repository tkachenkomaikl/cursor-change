import time
import subprocess
import random


themes = ["25ji", "25ji-Kanade", "25ji-Mafuyu", "25ji-Ena", "25ji-Mizuki"]

wait_minutes = 10

sleep = wait_minutes * 60

while True:
    random.shuffle(themes)

    for theme in themes:
        subprocess.run(["plasma-apply-cursortheme", theme])
        time.sleep(sleep)
