num_min = int(input())
num_max = int(input())

for i in range (num_min, num_max + 1):
    for j in range(num_min, num_max + 1):
        for k in range(num_min, num_max + 1):
            for l in range(num_min, num_max + 1):
                result = j + k
                if i > l and result % 2 == 0:
                    if i % 2 == 0 and l % 2 != 0:
                        print(f"{i}{j}{k}{l}", end=" ")
                    elif i % 2 != 0 and l % 2 == 0:
                        print(f"{i}{j}{k}{l}", end=" ")
