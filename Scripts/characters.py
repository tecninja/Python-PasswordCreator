letters_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

special_characters = ['!', '@', '#', '$', '%', '&', '*', '-', '=', ']', '[', '>',
                      '<', '+', '?', '/', '{', ']', '[', '{', '.', ',', '|', ';']

chrt_letter_num = []
for c in range(0, len(letters_upper) - 1):
    chrt_letter_num.append(letters_upper[c])
for c in range(0, len(letters_low) - 1):
    chrt_letter_num.append(letters_low[c])
for c in range(0, len(numbers) - 1):
    chrt_letter_num.append(numbers[c])

all_chrt = []
for c in range(0, len(special_characters) - 1):
    all_chrt.append(special_characters[c])
for c in range(0, len(chrt_letter_num) - 1):
    all_chrt.append(chrt_letter_num[c])

all_leters = []
for c in range(0, len(letters_upper)-1):
    all_leters.append(letters_upper[c])
for c in range(0, len(letters_low)-1):
    all_leters.append(letters_low[c])
