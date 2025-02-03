
class PrimeFilter:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime_filter = PrimeFilter()
prime_numbers = list(filter(lambda x: prime_filter.is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)
