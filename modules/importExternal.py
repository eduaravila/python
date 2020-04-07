from myExample import example
from hidden.hidden import hiddenFunction


# ? this is the python main function somethin like in java
if __name__ == "__main__":
    # ! if this code gets executed this means that this script is the main one
    print(example("Eduardo"))
    print(hiddenFunction())
else:
    print("this script is being imported")
