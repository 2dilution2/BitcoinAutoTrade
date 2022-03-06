import pyupbit

access = "d1AKKJjjOj1qgDbqkwsXK76GaY4txveK5HLnDu85"          # 본인 값으로 변경
secret = "wqEKkZHCf0vo4hIlAhyOMcBRRp6p7Bz257JRjDHE"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회