import random
import os

nums = ["0","1","2","3","4","5","6","7","8","9","@","&","%","#","/","{","}"]
mins = ["a","b","c","e","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mais = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def createPassword(nums,mins,mais):
    s = ""
    fs = ""
    var = random.randint(0,2)
    for i in range(16):
        if var == 0:
            s = nums[random.randint(0,len(nums)-1)]
            var = random.randint(0,1)
            fs += s
        elif var == 1:
            s = mins[random.randint(0,len(mins)-1)]
            var = random.randint(0,1)
            fs += s
        else:
            s = mais[random.randint(0,len(mais)-1)]
            var = random.randint(0,1)
            fs += s
    return fs

def writeFile():
    file = open("passwords.txt", "a")
    password = createPassword(nums,mins,mais)
    os.system("cls")
    print(f"the password is: {password}")
    inp = input("retry? ")
    while True:
        if inp.lower().strip() != "y" and inp.lower().strip() != "yes":
            os.system("cls")
            metadata = input("this password's associated with: ")
            file.write(f"{metadata} | {password}\n")
            file.close()
            os.system("cls")
            print("File created successfully!")
            break
        else:
            os.system("cls")
            password = createPassword(nums,mins,mais)
            print(f"the password is: {password}")
            inp = input("retry? ")

def main():
    writeFile()

main()