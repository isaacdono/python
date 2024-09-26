import modules.cpu_details as cpu_details
import modules.disk_details as disk_details
import modules.memory_details as memory_details
import modules.save_logs as save_logs


def main():
    print("Welcome to System Monitor app!\n")

    while(True):
        print("You can press:")
        print("1 to see CPU details.")
        print("2 to see  Disk details")
        print("3 to see  Memory detais")
        print("4 to log CPU, Disk and Memory basic metrics")
        print("0 to exit")
        choice = input("> ")
        print()

        if choice == '1':
            cpu_details.run()
        elif choice == '2':
            disk_details.run()
        elif choice == '3':
            memory_details.run()
        elif choice == '4':
            save_logs.run()
        elif choice == '0':
            print("Exiting...")
            exit(0)
        else:
            print("Please, type an option from above.\n")

if __name__ == "__main__":
    main()