def listprint():
    a_list=["hi", "here" , "how","are","you"]
    i=0
    while (i < len(a_list)):
        print(a_list[i])
        i+=1



def main():
    #initialize the variable
    u=0
    sum = 0
    while u<=10:
        sum = sum+u
        u+=1
    print(sum)
    
if __name__ == "__main__":
    main()
    listprint()