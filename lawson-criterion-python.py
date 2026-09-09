"""
ローソン条件をPythonで計算する｜核融合が"成立"する境界

元記事: https://fusion.yurufuwa.work/learn/lawson-criterion-python
ゆるふわ核融合・次世代エネルギー (fusion.yurufuwa.work) の解説記事から抜粋したコードです。
"""

import numpy as np

def triple_product(n, T, tau):
    return n * T * tau

IGNITION = 3e21          # D-T点火のおおよその閾値 [keV·s/m^3]

# トカマク型のおおよその狙い
n   = 1e20               # 密度 [1/m^3]
T   = 15                 # 温度 [keV]（約1.7億℃）
tau = 3.0                # 閉じ込め時間 [s]

tp = triple_product(n, T, tau)
print(f"三重積 = {tp:.2e} keV·s/m^3")
print("点火まで到達？:", tp >= IGNITION)
print("閾値に対する比:", round(tp / IGNITION, 2))

# 磁場閉じ込め（トカマク）: 薄いプラズマを長く保つ
tokamak = triple_product(n=1e20, T=15, tau=3.0)

# 慣性閉じ込め（レーザー）: 超高密度を一瞬だけ
laser   = triple_product(n=1e31, T=15, tau=1e-11)

print(f"トカマク : {tokamak:.2e}")
print(f"レーザー : {laser:.2e}")
