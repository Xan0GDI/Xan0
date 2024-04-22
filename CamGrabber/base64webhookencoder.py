import base64
import subprocess

def encode_to_base64_and_copy_to_clipboard(input_string):
    # Encode the input string to Base64
    encoded_string = base64.b64encode(input_string.encode("utf-8")).decode("utf-8")

    # Print the Base64-encoded string
    print(f"Base64-encoded string: {encoded_string}")

    # Copy the encoded string to the clipboard (Windows only)
    try:
        subprocess.run(["clip"], input=encoded_string.encode("utf-8"), check=True)
        print("Encoded string copied to clipboard.")
    except subprocess.CalledProcessError:
        print("Copying to clipboard failed. Make sure you are on a Windows system.")

# Example usage
user_input = input("Enter a webhook to encode: ")
encode_to_base64_and_copy_to_clipboard(user_input)
input()
exit()
