def create_user_profile(name, email, **kwargs):
    profile = {'name': name, 'email': email}  # Name und Email sind erforderlich

    for key, value in kwargs.items():
        profile[key] = value                  #Optionale Attribute hinzufügen

    return profile

#Beispielaufruf
alice = create_user_profile(name="Alice", email="alice@example.com", age=33, city="New York")
bob = create_user_profile(name="Bob", email="bob@example.com", last_name="Smith", age=22, phone_number=1234567890)

print(alice)
print(bob)


