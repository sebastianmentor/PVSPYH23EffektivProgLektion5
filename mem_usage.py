import sys

# kvadrater_list = [x**2 for x in range(1_000_000)]
kvadrater_gen = (x**2 for x in range(1_000_000_000))

# print(f"List comprehension: {sys.getsizeof(kvadrater_list)} bytes")
# for square in kvadrater_gen:
#     print(f"Generator: {sys.getsizeof(square)} bytes")
#     print(f"Generator: {sys.getsizeof(kvadrater_gen)} bytes")
# print(f"Size of integer 1.000.000.000: {sys.getsizeof(1_000_000_000)} bytes")

input()