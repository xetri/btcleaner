from helper import getRandomHex, pvkhex_to_address_compressed
import notorapis

iter = 1
try:
    with open("./notorstate", "r") as f:
        iter = int(f.read())
except: pass

def saveAddr(addr, pvhex, balance):
    with open("./founds.btc", "a+") as f:
        f.write(f"({iter}): {balance} | {addr} || {pvhex} | \n")

while True:
    pvkhex = getRandomHex()
    addr = pvkhex_to_address_compressed(pvkhex)
    balance = notorapis.getBalance(addr)

    print(f"({iter}): {balance} | {addr} || {pvkhex}")

    if balance > 0.0:
        print(f"Found: {balance} | {addr} || {pvkhex}")
        saveAddr(addr, pvkhex, balance)

    if iter % 25 == 0:
        with open("./notorstate", "w+") as f: f.write(str(iter))
    iter += 1
