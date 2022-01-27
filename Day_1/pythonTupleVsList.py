def main():
    #list
    simple_list=["1",2,True,False,"yooo man","oho"]
    sliced_list=simple_list[0:2]
    selected_list=simple_list[4]
    #tuple
    simple_tuple=(0,1,2,3,4,5,6)
    selected_tuple=simple_list[0]
    print(simple_list)
    print(sliced_list)
    print(selected_list)
    print(simple_tuple)
    print(selected_tuple)
    print(simple_tuple[0:3])
    #not work couse tuple are unchangable
    simple_tuple[1]="rrr"

if __name__ == "__main__":
    main()