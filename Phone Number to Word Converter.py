# Create a Library
digit_map = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    '9':"Nine"
}
phone_no = input("Please key in the phone number >> ")

output = "" #Create an empty output first
for char in phone_no:
    output += digit_map.get(char, '%') + " " # The % sign is there if the user key in anything other than numbers
print(output)