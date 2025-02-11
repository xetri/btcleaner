from tornet import change_ip
from helper import getRandomHex, pvkhex_to_address_compressed
import apis

iter = 1
try:
    with open("./state", "r") as f:
        iter = int(f.read())
except: pass

def saveAddr(addr, pvhex, balance):
    with open("./founds.btc", "a+") as f:
        f.write(f"[{apis.ip}]({iter}): {balance} | {addr} || {pvhex} | \n")

while True:
    pvkhex = getRandomHex()
    addr = pvkhex_to_address_compressed(pvkhex)
    balance = apis.getBalance(addr)

    print(f"[{apis.ip}]({iter}): {balance} | {addr} || {pvkhex}")

    if balance > 0.0:
        print(f"Found: {balance} | {addr} || {pvkhex}")
        saveAddr(addr, pvkhex, balance)

    if iter % 21 == 0:
        apis.ip = change_ip()
        with open("./state", "w+") as f: f.write(str(iter))
    iter += 1
