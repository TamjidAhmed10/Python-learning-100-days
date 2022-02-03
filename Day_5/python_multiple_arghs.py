def multiple_args(a,*the_args):
    """The doc of multiple args the results are saved in tuple."""
    print(a)
    for i in the_args:
        print("hello ",i)

def main():
    multiple_args("aa","bb","cc","dd","ee","ff","gg")

if __name__ == "__main__":
    main()