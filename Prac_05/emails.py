"""
Email to name
"""


def main():
    """Make dictionary of names and emails"""
    email_to_name = {}
    email = str(input("Email: "))
    while email != "":
        name = get_name_from_email(email)
        name_conformation = str(input("Is your name {} (Y/N)".format(name)))
        if name_conformation.upper() != "Y" and name_conformation != "":
            name = str(input("Enter your name: "))
        email_to_name[email] = name
        email = str(input("Email: "))

    for email, name in email_to_name.items():
        print("{}  ({})".format(name, email))


def get_name_from_email(email: str) -> str:
    """Get name from email"""
    before_at_symbol = email.split("@")[0]
    name_parts = before_at_symbol.split(".")
    name = " ".join(name_parts).title()
    return name


main()
