

def main():

    valid = False
    
    while not valid:

        x = input("Enter CTF OR CSF to continue: ")
        if x == "CTF" or x == "CSF":
            valid = True
        
    if x == "CTF":
        i = float(input("Enter Interest (in %): ")) / 100
        d = float(input("Enter d (in %): ")) / 100
        t = float(input("Enter tax (in %): ")) / 100
        numerator = t*d*(1+i/2)
        denominator = (i+d)*(1+i)
        CTF = 1 - numerator/denominator
        print("The CTF is", CTF)

    elif x == "CSF":
        i = float(input("Enter Interest (in %):")) / 100
        d = float(input("Enter d (in %): ")) / 100
        t = float(input("Enter tax (in %): ")) / 100
        numerator = t*d
        denominator = (i+d)
        CSF = 1 - numerator/denominator
        print("The CSF is", CSF)



if __name__ == "__main__":
    main()

