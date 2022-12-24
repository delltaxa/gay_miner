import random, time, string, sys
while 1: print(f"{sys.exit(f'[+] Found {str().join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))}')}\x1b[39m" if random.randint(0, 10000) % 100 == 0 else f"\x1b[31m[-] Mining {''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))}{str(time.sleep(0.05)).replace('None', '')}\x1b[39m");
