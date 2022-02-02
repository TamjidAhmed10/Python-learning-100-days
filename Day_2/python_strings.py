def main():
    #declear a string
    s="This is a string"
    print(s)
    #declear a multiline string
    sm='''
        this is a multiline
        string. okay.
    '''
    print(sm)
    #strings can be sliced
    print(s[3:9])
    #string cant be replaced
    sm[2]="a"




if __name__ == "__main__":
    main()