"""
Email to name
"""


def main():
    email = str(input("Email: "))
    name = get_name_from_email(email)
    print(name)


def get_name_from_email(email: str) -> str:
    """Get name from email"""
    before_at_symbol = email.split("@")[0]
    name_parts = before_at_symbol.split(".")
    name = " ".join(name_parts).title()
    return name


main()
