import random

def sorter():
    namelister = []
    f=open("finallist.txt", "r")
    """
    for line in f.readlines():
        print(line)
    """
      
    for line in f.readlines():
        newline = line.replace('\n','')
        
        newline = newline.split(",")
        print(newline)
        
        #tickets = newline[0]*int(float(newline[-1])/0.25)
        num = int(float(newline[-1])/0.25)
        
        for n in range(num+1):
            namelister.append(newline[0])
        print("length",len(namelister))
    
    w = open("results.txt","w+")
    w.write(str(namelister))
    ticketnum = len(namelister)
    random.seed()
    chosen_one = random.randrange(ticketnum)
    print("chosen ticket number is:",chosen_one)
    print("the winner is:",namelister[chosen_one])
    
sorter()
