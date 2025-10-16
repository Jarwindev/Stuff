import encrypt as e

def tryalgos():
    plaintext = input("Enter plaintext: ")
    print("Algorithm 1 Output:", e.algo1(plaintext))
    print("Algorithm 2 Output:", e.algo2(plaintext))
    print("Algorithm 3 Output:", e.algo3(plaintext))
    print("Algorithm 4 Output:", e.algo4(plaintext))

def trydealgo():
    ciphertext = input("Enter ciphertext: ")
    print("Decryption Algorithm 1 Output:", e.dealgo1(ciphertext))
    print("Decryption Algorithm 2 Output:", e.dealgo2(ciphertext))
    print("Decryption Algorithm 3 Output:", e.dealgo3(ciphertext))
    print("Decryption Algorithm 4 Output:", e.dealgo4(ciphertext))

def main():
    while True:
        choice = input("Choose (1) Encrypt or (2) Decrypt or (q) Quit: ")
        if choice == '1':
            tryalgos()
        elif choice == '2':
            trydealgo()
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()