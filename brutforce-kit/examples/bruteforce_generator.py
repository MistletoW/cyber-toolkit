def password_generator():
    """Generate passwords on the fly: 000A, 001A, ..., 999Z"""
    for num in range(1000):
        base = str(num).zfill(3)
        for char in string.ascii_uppercase:
            yield f"{base}{char}"

def brute_force():
    for password in password_generator():  # No memory used until needed
        data = {"username": username, "password": password}
        # ... same request code ...