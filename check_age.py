def check_age(age):
    if age<18:
        print("The user is younger.",age)
    else:
        print("The user is considered an adult",age)
    


if __name__ == "__main__":
    user_age=int(input("Enter the user age:"))
    check_age(user_age)