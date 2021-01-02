def replace_domain(email, old_domain, new_domain):

    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email

    return email


old_domain = input("Enter Old Domain: ").strip()
new_domain = input("Enter New Domain: ").strip()

emails = input("Enter Email (space for multiple emails): ").strip().split(" ")

print("Changed Emails List\n")
for email in emails:
    print("Old Email: " + email)
    new_email = replace_domain(email, old_domain, new_domain)
    print("New Email: " + new_email)
    print()
