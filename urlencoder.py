import urllib.parse

def url_encode_input():
    user_input = input("Enter the string to URL encode: ")

    # Perform URL encoding
    encoded_string = urllib.parse.quote(user_input)

    print("\nOriginal string:", user_input)
    print("URL encoded string:", encoded_string)

if __name__ == "__main__":
    url_encode_input()
