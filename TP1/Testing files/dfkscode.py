import sys
from collections import deque
import heapq
from typing import List
 # random just for sakes 
dp = []
flag = []

class InputReader:
    def __init__(self, stream):
        self.reader = stream
        self.tokenizer = None

    def next(self):
        while self.tokenizer is None or not self.tokenizer.hasMoreTokens():
            self.tokenizer = self.reader.readline().split()
        return self.tokenizer.pop(0)

    def nextInt(self):
        return int(self.next())

    def nextLong(self):
        return int(self.next())

class Wahana:
    def __init__(self, harga, poin, kapasitas, kapasitas_ft):
        self.harga = harga
        self.poin = poin
        self.kapasitas = kapasitas
        self.kapasitas_ft = int(self.kapasitas * kapasitas_ft / 100.0)
        self.antrian_ft = []
        self.antrian_reg = []

class Pengunjung:
    def __init__(self, id, jenis, uang):
        self.id = id
        self.jenis = jenis
        self.uang = uang
        self.counter_bermain = 0
        self.poin = 0

def A(id_pengunjung, id_wahana):
    pengunjung = pengunjung_arr[id_pengunjung - 1]
    wahana = wahana_arr[id_wahana - 1]

    if pengunjung.uang < wahana.harga:
        return -1

    if pengunjung.jenis == "FT":
        wahana.antrian_ft.append(Pengunjung(pengunjung.id, pengunjung.jenis, pengunjung.uang))
    else:
        wahana.antrian_reg.append(Pengunjung(pengunjung.id, pengunjung.jenis, pengunjung.uang))

    return len(wahana.antrian_ft) + len(wahana.antrian_reg)

def E(id_wahana):
    wahana = wahana_arr[id_wahana - 1]
    kapasitas_counter = wahana.kapasitas_ft
    antrian_ft = list(wahana.antrian_ft)
    antrian_reg = list(wahana.antrian_reg)
    slot = wahana.kapasitas

    empty_flag = True

    if not antrian_ft and not antrian_reg:
        print(-1)
        return

    while kapasitas_counter > 0 and antrian_ft:
        tmp = antrian_ft.pop(0)
        actual = pengunjung_arr[tmp.id - 1]
        if actual.uang >= wahana.harga:
            empty_flag = False
            print(tmp.id, end=" ")
            actual.uang -= wahana.harga
            actual.poin += wahana.poin
            actual.counter_bermain += 1
            kapasitas_counter -= 1
            slot -= 1
            if actual.uang == 0:
                keluar.append(actual)

    while slot > 0 and antrian_reg:
        tmp = antrian_reg.pop(0)
        actual = pengunjung_arr[tmp.id - 1]
        if actual.uang >= wahana.harga:
            empty_flag = False
            print(tmp.id, end=" ")
            actual.uang -= wahana.harga
            actual.poin += wahana.poin
            actual.counter_bermain += 1
            kapasitas_counter -= 1
            slot -= 1
            if actual.uang == 0:
                keluar.append(actual)

    while slot > 0 and antrian_ft:
        tmp = antrian_ft.pop(0)
        actual = pengunjung_arr[tmp.id - 1]
        if actual.uang >= wahana.harga:
            empty_flag = False
            print(tmp.id, end=" ")
            actual.uang -= wahana.harga
            actual.poin += wahana.poin
            actual.counter_bermain += 1
            kapasitas_counter -= 1
            slot -= 1
            if actual.uang == 0:
                keluar.append(actual)

    if empty_flag:
        print(-1)
    else:
        print()

def S(id_pengunjung, id_wahana):
    pengunjung = pengunjung_arr[id_pengunjung - 1]
    wahana = wahana_arr[id_wahana - 1]
    counter = 0
    slot_ft = wahana.kapasitas_ft
    slot = wahana.kapasitas
    antrian_ft = list(wahana.antrian_ft)
    antrian_reg = list(wahana.antrian_reg)

    while antrian_ft or antrian_reg:
        while slot_ft > 0 and antrian_ft:
            target = antrian_ft.pop(0)
            if pengunjung_arr[target.id - 1].uang >= wahana.harga:
                counter += 1
                if target.id == pengunjung.id:
                    return counter
            slot_ft -= 1
            slot -= 1

        while slot > 0 and antrian_reg:
            target = antrian_reg.pop(0)
            if pengunjung_arr[target.id - 1].uang >= wahana.harga:
                counter += 1
                if target.id == pengunjung.id:
                    return counter
            slot -= 1

        slot_ft = wahana.kapasitas_ft
        slot = wahana.kapasitas

    return -1

def F(p):
    if not keluar:
        return -1

    if p == 0:
        return keluar.popleft().poin

    return keluar.pop().poin

def initialize_dp():
    uang = max(daftar_uang) + 1
    dp = [[[0] * 3 for _ in range(uang + 1)] for _ in range(len(wahana_arr) + 2)]
    flag = [[[0] * 3 for _ in range(uang + 1)] for _ in range(len(wahana_arr) + 2)]

    for id in range(len(wahana_arr) + 1, 0, -1):
        for ku in range(uang + 1):
            for k in range(3):
                if id == len(wahana_arr) + 1:
                    dp[id][ku][k] = 0
                else:
                    dp[id][ku][k] = dp[id + 1][ku][k]
                    if ku >= wahana_arr[id - 1].harga and (k != id % 2 or k == 2):
                        take = dp[id + 1][ku - wahana_arr[id - 1].harga][id % 2] + wahana_arr[id - 1].poin
                        dont_take = dp[id + 1][ku][k]
                        if take >= dont_take:
                            dp[id][ku][k] = take
                            flag[id][ku][k] = 1
                        else:
                            flag[id][ku][k] = 0
                    else:
                        flag[id][ku][k] = 0

def O(id_pengunjung):
    pengunjung = pengunjung_arr[id_pengunjung - 1]
    uang = pengunjung.uang

    optimum = dp[1][uang][2]
    if optimum == 0:
        print(optimum)
        return

    print(optimum, end=" ")
    while uang - 1 > 0 and dp[1][uang][2] == dp[1][uang - 1][2]:
        uang -= 1

    last_OE = 2
    id = 1
    while id <= len(wahana_arr):
        if uang <= 0:
            break
        if id % 2 != last_OE and flag[id][uang][last_OE] == 1:
            uang -= wahana_arr[id - 1].harga
            last_OE = id % 2
            print(id, end=" ")
        id += 1
    print()

input_stream = sys.stdin
in_ = InputReader(input_stream)

M = in_.nextInt()
wahana_arr = []

for _ in range(M):
    harga = in_.nextInt()
    poin = in_.nextInt()
    kapasitas = in_.nextInt()
    max_ft = in_.nextInt()
    wahana_arr.append(Wahana(harga, poin, kapasitas, max_ft))

N = in_.nextInt()
pengunjung_arr = []
daftar_uang = []

for i in range(N):
    jenis = in_.next()
    uang = in_.nextInt()
    pengunjung_arr.append(Pengunjung(i + 1, jenis, uang))
    daftar_uang.append(uang)

T = in_.nextInt()
keluar = deque()

for _ in range(T):
    command = in_.next()

    if command == "A":
        par1 = in_.nextInt()
        par2 = in_.nextInt()
        print(A(par1, par2))

    elif command == "S":
        par1 = in_.nextInt()
        par2 = in_.nextInt()
        print(S(par1, par2))

    elif command == "E":
        par1 = in_.nextInt()
        E(par1)

    elif command == "F":
        par1 = in_.nextInt()
        print(F(par1))

    else:
        if not depe_done:
            depe_done = True
            initialize_dp()
        par1 = in_.nextInt()
        O(par1)
