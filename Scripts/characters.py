

class Characters:
    def __init__(self) -> None:
        self.letters_low = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
        ]
        
        self.letters_upper = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        self.special_characters = [
            '!', '@', '#', '$', '%', '&', '*', '-', '=', ']',
            '[', '>', '<', '+', '?', '/', '{', ']', '[', '{',
            '.', ',', '|', ';'
        ]

    def chrt_letter_num(self) -> list:
        lista = []
        lista += self.letters_upper 
        lista += self.letters_low
        lista += self.numbers
        return lista

    def all_chrt(self) -> list:
        lista = []
        lista += self.special_characters
        lista += self.chrt_letter_num()
        return lista
    
    def all_leters(self) -> list:
        lista = []
        lista += self.letters_low
        lista += self.letters_upper
        return lista
