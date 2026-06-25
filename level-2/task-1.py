email=input("Enter your email address: ")

if "@" in email and "." in email:
    print("Valid email address.")
    print("Email address:", email)
else:
    print("Invalid email address.")
    print("Email address:", email)