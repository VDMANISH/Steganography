while True:
    print("\n1. Encode Secret Message")
    print("2. Decode Secret Message")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        secret = input("Enter the secret message: ")
        cover = input("Enter the cover text: ")
        
        if len(secret) > len(cover):
            print("Warning: The secret message is longer than the cover text.")
            proceed = input("Do you want to proceed anyway? (yes/no): ").lower()
            if proceed != "yes":
                print("Please ensure the cover text and secret message are of equal length.")
                continue

        encoded = ""
        i, j = 0, 0
        while i < len(cover) or j < len(secret):
            if i < len(cover):
                encoded += cover[i]
                i += 1
            if j < len(secret):
                encoded += secret[j]
                j += 1
        print("Stego Text:", encoded)
    elif choice == "2":
        stego = input("Enter the stego text: ")
        decoded = ""
        for k in range(1, len(stego), 2):  # Extract every second character
            decoded += stego[k]
        print("Secret Message:", decoded)
    elif choice == "3":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
