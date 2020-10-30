arr = [1,1,1]
n = 7

res = {}
mx_freq = 0
mx_count = 0

for t in arr:
    if t not in res:
        res[t] = 1
    else:
        res[t] += 1

    if res[t] > mx_freq:
        mx_freq = res[t]
        mx_count = 1
    elif res[t] == mx_freq:
        mx_count += 1

print mx_count, mx_freq
print  (mx_freq-1) * (n) + mx_count
# if len(res) <= n+1:
#     print (mx_freq-1) * (n+1) + mx_count
# else:
#     print max((mx_freq-1) * (n+1) + mx_count, len(arr))
