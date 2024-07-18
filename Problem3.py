# Import necessary librsry
import os

# Define function at first
def print_directory_contents(path):
    try:
        # List the contents of the directory
        contents = os.listdir(path)
        
        # Provide information about what have to print
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)

        # If file does not exist
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

        # If permission is denided
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

        # For other errors
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = "/"
print_directory_contents(directory_path)
