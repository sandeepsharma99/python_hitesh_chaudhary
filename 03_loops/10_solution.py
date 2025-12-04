# Exponential Backoff: im plement an exponential backoff strategy tha dobles the wait time b/w retries,starting from 1 second  but stop after 5 tries

import time

wait_time = 1
max_tries = 5
attempts = 0

while attempts<max_tries:
    print("Attempts",attempts,+1,"-wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1