f = open("26.txt")
n = int(f.readline())
arr = [list(map(int, s.split())) for s in f]
arr.sort()
res = []
for i in range(n-2):
        if arr[i+1][1] - arr[i][1]-1 == 1 and arr[i+2][1] - arr[i+1][1] - 1 == 1 and \
            arr[i][0] == arr[i+1][0] == arr[i+2][0]:
                res.append([arr[i][0], arr[i][1] + 1])
print(min(res))

privet tvari
