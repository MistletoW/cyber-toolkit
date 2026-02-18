from itertools import product
import string

# Generate all digit combinations (000-999)
digits = [str(i).zfill(3) for i in range(1000)]
uppers = list(string.ascii_uppercase)

# Create all combinations
password_list = [f"{d}{u}" for d, u in product(digits, uppers)]

# Or as a generator (better):
password_gen = (f"{d}{u}" for d, u in product(digits, uppers))