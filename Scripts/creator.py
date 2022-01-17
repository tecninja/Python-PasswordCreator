import characters as ch
from random import randint


class CreatePassword:
    def __init__(self, length, repeat=False):
        self.length = length
        self.repeat = repeat

    def master_password(self):
        final_password = []
        repetition_counter = []
        while len(final_password) < self.length:
            if self.length > len(ch.all_chrt) and self.repeat == False:
                print(f"Error! Password must contain no more than {len(ch.all_chrt)} characters!")
                break
            else:
                raffled = randint(0, len(ch.all_chrt) - 1)
                if self.repeat:
                    final_password.append(ch.all_chrt[raffled])
                else:
                    if ch.all_chrt[raffled] in repetition_counter:
                        pass
                    else:
                        final_password.append(ch.all_chrt[raffled])
                        repetition_counter.append(ch.all_chrt[raffled])
        return final_password

    def numeric_password(self):
        final_password = []
        repetition_counter = []
        while len(final_password) < self.length:
            if self.length > len(ch.numbers) and self.repeat == False:
                print(f"Error! Password must contain no more than {len(ch.numbers)} characters!")
                break
            else:
                raffled = randint(0, len(ch.numbers) - 1)
                if self.repeat:
                    final_password.append(ch.numbers[raffled])
                else:
                    if ch.numbers[raffled] in repetition_counter:
                        pass
                    else:
                        final_password.append(ch.numbers[raffled])
                        repetition_counter.append(ch.numbers[raffled])
        return final_password

    def letter_password(self):
        final_password = []
        repetition_counter = []
        while len(final_password) < self.length:
            if self.length > len(ch.all_leters) and self.repeat == False:
                print(f"Error! Password must contain no more than {len(ch.all_leters)} characters!")
                break
            else:
                raffled = randint(0, len(ch.all_leters) - 1)
                if self.repeat:
                    final_password.append(ch.all_leters[raffled])
                else:
                    if ch.all_leters[raffled] in repetition_counter:
                        pass
                    else:
                        final_password.append(ch.all_leters[raffled])
                        repetition_counter.append(ch.all_leters[raffled])
        return final_password

    def special_chrt_password(self):
        final_password = []
        repetition_counter = []
        while len(final_password) < self.length:
            if self.length > len(ch.special_characters) and self.repeat == False:
                print(f"Error! Password must contain no more than {len(ch.special_characters)} characters!")
                break
            else:
                raffled = randint(0, len(ch.special_characters) - 1)
                if self.repeat:
                    final_password.append(ch.special_characters[raffled])
                else:
                    if ch.special_characters[raffled] in repetition_counter:
                        pass
                    else:
                        final_password.append(ch.special_characters[raffled])
                        repetition_counter.append(ch.special_characters[raffled])
        return final_password

    def letter_num_password(self):
        final_password = []
        repetition_counter = []
        while len(final_password) < self.length:
            if self.length > len(ch.chrt_letter_num) and self.repeat == False:
                print(f"Error! Password must contain no more than {len(ch.chrt_letter_num)} characters!")
                break
            else:
                raffled = randint(0, len(ch.chrt_letter_num) - 1)
                if self.repeat:
                    final_password.append(ch.chrt_letter_num[raffled])
                else:
                    if ch.chrt_letter_num[raffled] in repetition_counter:
                        pass
                    else:
                        final_password.append(ch.chrt_letter_num[raffled])
                        repetition_counter.append(ch.chrt_letter_num[raffled])
        return final_password
