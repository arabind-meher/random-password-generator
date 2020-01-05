from random import choice

upper = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
lower = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
number = '0 1 2 3 4 5 6 7 8 9'.split()
symbol = '~ ! @ # $ % ^ & *'.split()


class GeneratePassword:
    def __init__(self, nlength, isupper, islower, isnumber, issymbol):
        self.nlength = nlength
        self.isupper = isupper
        self.islower = islower
        self.isnumber = isnumber
        self.issymbol = issymbol

        print(nlength, isupper, islower, isnumber, issymbol)

        characters = []

        if isupper == 1:
            characters.extend(upper)
        if islower == 1:
            characters.extend(lower)
        if isnumber == 1:
            characters.extend(number)
        if issymbol == 1:
            characters.extend(symbol)

        self.password = []
        while True:
            for _ in range(nlength):
                self.password.append(choice(characters))

            result = self.check_password(self.password, nlength, isupper, islower, isnumber, issymbol)
            if result:
                break
            else:
                del self.password[:]

        self.password = ''.join(self.password)

    def get_password(self):
        return self.password

    @staticmethod
    def check_password(password, nlength, isupper, islower, isnumber, issymbol):
        if len(password) != nlength:
            return False
        else:
            if isupper:
                if len(set(password) & set(upper)) == 0:
                    return False
            if islower:
                if len(set(password) & set(lower)) == 0:
                    return False
            if isnumber:
                if len(set(password) & set(number)) == 0:
                    return False
            if issymbol:
                if len(set(password) & set(symbol)) == 0:
                    return False
            return True


def generate_password(nlength, isupper, islower, isnumber, issymbol):
    generated_password = GeneratePassword(nlength, isupper, islower, isnumber, issymbol).get_password()
    return generated_password
