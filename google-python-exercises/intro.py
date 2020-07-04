def repeat(word):
    result = word * 3
    # result = word + word +word / is the same as the above
    return result


def rawText(text):
    return r(text)


def multiText(text):
    return f"""{text}
    other line"""


def itiration(word, start, end):
    return word[start:end]


def main():
    print(repeat("Eduardo"))
    print(multiText("exmaple"))
    print(itiration("Example", 0, 2))
    textMulti = ("some"
                 "text"
                 "here"
                 "also"
                 "some"
                 "operators"
                 "%d" % (22))
    # ? some unicode text ir i18u
    ustring = u"some dope text \u018e"

    # converts unicode to a string
    encodedString = ustring.encode("utf-8")

    # * if you are using python <3 you can use unicode instead of str
    # converts the string back to an unicode string
    convertedString = str(encodedString, "utf-8")
    print(textMulti, ustring, encodedString)


if __name__ == "__main__":
    main()
