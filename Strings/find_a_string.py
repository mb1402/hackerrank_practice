def count_substring(string, sub_string):
    c = 0
    s = len(sub_string)
    print(string[::3])
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
