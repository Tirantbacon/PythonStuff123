name_input = input("Please enter a name here : ")
fav_color = input("please enter your favorite color! : ")


def name():
    if len(name_input) > 0:
        print('Your name is {}'.format(name_input))
    else:
        print("enter a name!")


def color():
    if len(fav_color) > 0:
        print("Your favourite color is {}".format(fav_color))
    else:
        print("enter a color!")



name()
color()
