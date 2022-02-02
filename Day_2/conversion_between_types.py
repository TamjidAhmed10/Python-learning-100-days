def main():
    #convet to folat , int , string
    print(int(1.22))
    print(float(10))
    print(str(3))
    ## convet list items
    a_list = [1,2,3,4,4,4,5]
    print(set(a_list))
    print(tuple(a_list))
    #convert a set to list
    a_set={1,2,3,4,5,5}
    print(list(a_set))
    #convert a list to dictionary.
    a_list_v2=[[1,2],[2,3]]
    print(dict(a_list_v2))

if __name__ == "__main__":
    main()