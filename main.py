text_morse_dic = {"a": "*-","b":"-***", "c":"-*-*", "d":"-**", "e":"*", "f":"**-*", "g":"--*","h":"****",
                  "i":"**", "j":"*---", "k":"-*-", "l":"*-**", "m":"--", "n":"-*", "o":"---", "p":"*--*",
                  "q":"--*-", "r":"*-*", "s":"***", "t":"-", "u":"**-", "v":"***-", "w":"*--", "x":"-**-",
                  "y":"-*--", "z":"--**", "1":"*----", "2":"**---", "3":"***--", "4":"****-", "5":"*****",
                  "6":"-****","7":"--***","8":"---**", "9":"----*", "0":"-----", ".":"*-*-*-", ",":"--**--",
                  ":":"---***", "?":"**--**","'":"*----*","-":"-****-","/":"-**-*",")":"-*--*-","(":"-*--*",'"':"*-**-*"}


def char_morse(char):
    """ here is to return the proper morse of a character"""
    l_morse = list(text_morse_dic.get(char, char))
    if l_morse != char:
        l_morse = [c for c in l_morse]
    return " ".join(l_morse)

def word_morse(word):
    """ here is to return the proper morse of a word"""
    l_chars = list(word)
    l_morse = [char_morse(char)+(" "*3) for char in l_chars]
    return " ".join(l_morse)


def sentence_morse(sentence):
    """ here is to return the proper morse of a sentence"""
    words = sentence.split()
    l_morse = [word_morse(word)+(" "*7) for word in words]
    return " ".join(l_morse)[0:-7]


sentence = input("enter a word to get its morse code: ").lower()
print(sentence,": ", sentence_morse(sentence))

