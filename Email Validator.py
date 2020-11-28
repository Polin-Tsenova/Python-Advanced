class NameTooShortError(Exception):
    def __str__(self):
        return f"Name must be more than 4 characters"


class MustContainAtSymbolError(Exception):
    def __str__(self):
        return f"Email must contain @"


class InvalidDomainError(Exception):
    def __str__(self):
        return f"Domain must be one of the following: .com, .bg, .org, .net"


def validate_name(email):
    username = email.split('@')[0]
    if len(username) <= 4:
        raise NameTooShortError


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError


def validate_domain(email, domains):
    domain = email.split('.')[-1]
    if domain not in domains:
        raise InvalidDomainError


while True:
   email = input()
   valid_domains = ("com","bg",".org", ".net")
   if email == 'End':
       break

   validate_name(email)
   validate_at_symbol(email)
   validate_domain(email,valid_domains)

   print('Email is valid')

