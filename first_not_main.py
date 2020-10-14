import sys
import not_main, orange

# print("first_not_main.py")
# print(__name__)
if "__main__" == __name__:
    # print("I am main!")
    list_to_iterate = ["I", "am", "main"]
    # for i in list_to_iterate:
        # print(i)
    print(sys.argv)
    for count, arg in enumerate(sys.argv):
        print(f"Argument at count:{count} arg:{arg}")
    
