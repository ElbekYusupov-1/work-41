# ================= Array11 =================
n = int(input("n: "))
K = int(input("K: "))
A = list(map(int, input("Massiv: ").split()))

# K ga karrali indekslar (K, 2K, 3K, ...)
for i in range(K, n, K):
    print(A[i], end=" ")
print()


# ================= Array12 =================
n = int(input("n (juft): "))
A = list(map(int, input("Massiv: ").split()))

# Juft indekslar: 0,2,4,...
for i in range(0, n, 2):
    print(A[i], end=" ")
print()


# ================= Array13 =================
n = int(input("n (toq): "))
A = list(map(int, input("Massiv: ").split()))

# Toq indekslarni teskari chiqarish: n-1, n-3, ...
for i in range(n-1, -1, -2):
    print(A[i], end=" ")
print()


# ================= Array14 =================
n = int(input("n: "))
A = list(map(int, input("Massiv: ").split()))

# Avval juft indekslar
for i in range(0, n, 2):
    print(A[i], end=" ")

# Keyin toq indekslar
for i in range(1, n, 2):
    print(A[i], end=" ")
print()


# ================= Array15 =================
n = int(input("n (juft): "))
A = list(map(int, input("Massiv: ").split()))

# Avval toq indekslar o‘sish tartibida
for i in range(1, n, 2):
    print(A[i], end=" ")

# Keyin juft indekslar kamayish tartibida
for i in range(n-2, -1, -2):
    print(A[i], end=" ")
print()


# ================= Array16 =================
n = int(input("n: "))
A = list(map(int, input("Massiv: ").split()))

# A[0], A[n-1], A[1], A[n-2], ...
l = 0
r = n - 1

while l <= r:
    print(A[l], end=" ")
    if l != r:
        print(A[r], end=" ")
    l += 1
    r -= 1
print()


# ================= Array17 =================
n = int(input("n: "))
A = list(map(int, input("Massiv: ").split()))

# A[0], A[1], A[n-1], A[n-2], A[2], A[3], ...
l = 0
r = n - 1

while l <= r:
    print(A[l], end=" ")
    if l + 1 < n:
        print(A[l+1], end=" ")
    if r != l and r != l+1:
        print(A[r], end=" ")
    if r - 1 > l:
        print(A[r-1], end=" ")
    l += 2
    r -= 2
print()