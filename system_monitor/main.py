import cpu_details
import disk_details
import memory_details


def main():
    print("Welcome to System Monitor app!\n")

    while(True):
        print("You can press:")
        print("1 to see CPU details.")
        print("2 to see  Disk details")
        print("3 to see  Memory detais")
        print("0 to exit")
        choice = input("> ")
        print()

        if choice == '1':
            cpu_details.run()
        elif choice == '2':
            disk_details.run()
        elif choice == '3':
            memory_details.run()
        elif choice == '0':
            print("Exiting...")
            exit(0)
        else:
            print("Please, type an option from above.\n")

if __name__ == "__main__":
    main()