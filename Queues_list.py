from collections import deque

antrian = deque([1,2,3,4,5])

antrian.append(6)
print('angka masuk',6)
print('data sekarang:',antrian)

antrian.append(7)
print('angka masuk',7)
print('data sekarang:',antrian)

out=antrian.popleft()
print('antrian keluar',out)
print('data sekarang:',antrian)

out=antrian.popleft()
print('antrian keluar',out)
print('data sekarang:',antrian)




