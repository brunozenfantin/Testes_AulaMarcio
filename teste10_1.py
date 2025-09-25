import time
from numba import njit

@njit
def contar():
    for i in range(1, 1_000_000_000):
        pass

inicio = time.perf_counter()

contar()

fim = time.perf_counter()

print(f"Tempo: {fim - inicio} segundos")