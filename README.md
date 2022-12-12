
import math


def merge_sort(arr: list[int]):
    if len(arr) > 1:
        middle: int = len(arr) // 2
        L: list[int] = arr[:middle]
        R: list[int] = arr[middle:]

        merge_sort(L)
        merge_sort(R)

        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def is_primo(number: int) -> bool:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def firts_primos(num):
    numbers = 7
    while num > 0:
        if is_primo(numbers):
            print(numbers)
            num -= 1
        numbers += 1


def swap(arr: list[list[list[int]]], x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
    aux:int = arr[x1][y1][z1]
    arr[x1][y1][z1] = arr[x2][y2][z2]
    arr[x2][y2][z2] = aux


if __name__ == "__main__":
    pass
