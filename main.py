from tornet import change_ip, ma_ip
from helper import getRandomHex, pvkhex_to_address_compressed
import apis

change_ip()
iter = 1

def saveAddr(addr, pvhex, balance):
    with open("./founds.btc", "a+") as f:
        f.write(f"[{ma_ip()}]({iter}): {balance} | {addr} || {pvhex} | \n")

while True:
    pvkhex = getRandomHex()
    addr = pvkhex_to_address_compressed(pvkhex)
    balance = apis.getBalance(addr)

    print(f"[{ma_ip()}]({iter}): {balance} | {addr} || {pvkhex}")

    if balance > 0.0:
        print(f"Found: {balance} | {addr} || {pvkhex}")
        saveAddr(addr, pvkhex, balance)

    if iter % 13 == 0: change_ip()
    iter += 1