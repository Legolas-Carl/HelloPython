#Dictionary language + gender

user_preferences = {
    'language': 'en',
    'gender': 'f'
}

if user_preferences['language'] == 'en':
    if user_preferences['gender'] == 'f':
        print("Hello madam, welcome back")
    elif user_preferences['gender'] == 'm':
        print("Hello sir, welcome back")
    else: print("Hello, welcome back")
elif user_preferences['language'] == 'nl':
    if user_preferences['gender'] == 'f':
        print("Hallo mevrouw, welkom terug")
    elif user_preferences['gender'] == 'm':
        print("Hallo meneer, welkom terug")
    else:
        print("Hallo, welkom terug")
else:
    print("Error: Language not supported!")