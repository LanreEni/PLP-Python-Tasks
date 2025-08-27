def file_read_write():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Check file permissions or try again.")


# Run the program
file_read_write()
