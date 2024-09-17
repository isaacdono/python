import cpu_details
import disk_details
import memory_details


def main():
    print("Welcome to System Monitor app!\n")
    print("You can:")
    print("Press 1 to see CPU details.")
    print("Press 2 to see  Disk details")
    print("Press 3 to see  Memory detais\n")

    while(True):
        choice = input()
        if choice == 1:
            cpu_details.run()
        elif choice == 2:
            disk_details.run()
        elif choice == 3:
            memory_details.run()
        elif choice == 0:
            print("Exiting...")
        else:
            print("Please, type an option from above.\n")

if __name__ == "__main__":
    main()