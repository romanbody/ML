for x in (1..10) :
    print (x)   
print (1)

    def __init__(self,init_name):
        print ('init1')
        self.first_name = init_name

    def print_out (self,o1):
        for x in range(1,o1,3):
            print (self.first_name + str(x))

rbo1 = rbo('test1')
rbo1.print_out(10)