from custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


def check_for_current_symbol(current_email):
    email_parts = current_email.split("@")
    if len(email_parts) != 2:
        return True
    return False


def check_for_length_name(current_email):
    name = current_email.split("@")[0]
    if len(name) <= 4:
        return True
    return False


def check_valid_domain(current_email):
    valid_domains = [".com", ".bg", ".net", ".org"]
    domain_parts = current_email.split("@")[-1]
    domain = f'.{domain_parts.split(".")[-1]}'
    if domain not in valid_domains:
        return True
    return False


email = input()
while not email == "End":

    if check_for_current_symbol(email):
        raise MustContainAtSymbolError("Email must contain @")

    if check_for_length_name(email):
        raise NameTooShortError("Name must be more than 4 characters")

    if check_valid_domain(email):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .net, .org")

    print("Email is valid")
    email = input()
