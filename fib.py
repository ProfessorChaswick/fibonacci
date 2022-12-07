from functools import lru_cache
import locale

@lru_cache(maxsize=1000)
def fibb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibb(n-1) + fibb(n-2)

for n in range(1, 101):
    print(n, ":", f"{fibb(n):,}")


# the 100th number will be 354,224,848,179,261,915,075
  