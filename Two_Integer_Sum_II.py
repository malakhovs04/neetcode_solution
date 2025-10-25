<<<<<<< HEAD
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = 1

        while i < n - 1:
            # Проверяем, что j не выходит за границы
            if j >= n:
                # если дошли до конца массива, двигаем левый указатель и сбрасываем j
                i += 1
                j = i + 1
                continue

            s = numbers[i] + numbers[j]

            if s == target:
                return [i + 1, j + 1]  # индексы 1-based
            elif s < target:
                j += 1  # сумма меньше — двигаем правый указатель
            else:
                # сумма больше — двигаем левый указатель и сбрасываем j
                i += 1
                j = i + 1
=======
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = 1

        while i < n - 1:
            # Проверяем, что j не выходит за границы
            if j >= n:
                # если дошли до конца массива, двигаем левый указатель и сбрасываем j
                i += 1
                j = i + 1
                continue

            s = numbers[i] + numbers[j]

            if s == target:
                return [i + 1, j + 1]  # индексы 1-based
            elif s < target:
                j += 1  # сумма меньше — двигаем правый указатель
            else:
                # сумма больше — двигаем левый указатель и сбрасываем j
                i += 1
                j = i + 1
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
