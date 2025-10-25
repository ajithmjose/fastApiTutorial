def get_full_name(first_name: str, last_name: str):
    full_name=first_name.capitalize + " " + last_name.capitalize()
    return full_name

print(get_full_name("john","doe"))