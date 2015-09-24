cipherText = raw_input("Please input the cipher text\n")

mode = raw_input(
    "Select a mode by its accompaning digit: \n"
    + "1: Select a shift to use in decryption \n"
    + "2: Run through all 26 iterations printing a snippet \n"
    + "3: Run through all 26 iterations printing the full text \n\n"
)
if mode == 1:
    shift = raw_input("Select amount to shift \n\n")
else:
    shift = 26

caeser(cipherText, shift)


def caeser(cipherText, shift):
    cipherText = cipherText.ascii_lowercase

    for i in shift:
        for letter in cipherText:
