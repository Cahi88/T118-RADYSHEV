def entry_message(group):
    if group == "Т118":
        return ("т118: вход разрешён")
    return ("обратитесь к куратору")
check_entry = entry_message
print(check_entry("Т118"))
print(check_entry("Т119"))
print(check_entry("т118"))
print(check_entry(""))
print(type(check_entry("Т118")))
print(type(check_entry))