# l1

# remove duplicates function
def remove_duplicates(value):
    var=""
    for i in value:
        if i in value:
            if i in var:
                pass
            else:
                var=var+i
    return var

# split input string into k blocks and remove duplicates

def merge_the_tools(string, k):
    # your code goes here
    l = int(len(string)/k);
    x=int(0)
    for y in range(0,l):
        s1 = string[x:x+k]
        print(remove_duplicates(s1))
        x=x+k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



