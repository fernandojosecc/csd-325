def generate_greeting(name, language):
    """Returns a greeting based on the selected language."""
    if language.lower() == "es":
        return f"¡Hola, {name}! Bienvenido al sistema."
    elif language.lower() == "en":
        return f"Hello, {name}! Welcome to the system."
    else:
        return f"Hi {name}, language not supported."

def main():
    print("--- Bilingual Greeting Tool ---")
    user_name = input("Enter your name: ")
    lang_choice = input("Choose language (en/es): ")
    
    # Logic to process greeting
    result = generate_greeting(user_name, lang_choice)
    
    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()