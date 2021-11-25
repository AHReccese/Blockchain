import math
import hashlib

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.digest()


def upgradeLeaves(ms):
    n = len(ms)
    merkleR = int(math.log2(n))
    if (not (2 ** merkleR == n)):
        merkleR = merkleR + 1
    temp = []
    for i in range(0, 2 ** merkleR - len(ms)):
        temp.append(ms[-(i + 1)])
    ms.extend(temp)
    print("Merkle tree Leaves: ")
    print(ms)


def Hash(string):
    return hashlib.sha256(string.encode()).hexdigest()


def addLayerHashes(layer, ms):
    if (layer == 0):
        return [Hash(ms[0]) + Hash(ms[1])]
    else:
        return [Hash(ms[2 * i]) + Hash(ms[2 * i + 1]) for i in range(2 ** layer)]


def calculateRoot(ms):
    depth = int(math.log2(len(ms)))
    for layer in range(depth):
        ms = addLayerHashes((depth - 1) - layer, ms)
    print("Hex output of root: ")
    print(Hash(ms[0]))
    return Hash(ms[0])


def rootCalculater(n):
    # simply put your 14 files here and use sha256sum to get a hash of file ,but for simplicity
    # I used ms with strings :)
    ms = [str(i) for i in range(1, n + 1)]
    print("before Upgrading")
    print(ms)
    upgradeLeaves(ms)
    return calculateRoot(ms)
