import random

def sorter():
    namelister = []
    f=open("finallist.txt", "r")
    
    for line in f.readlines():
        newline = line.replace('\n','')  # remove newlines character
        
        newline = newline.split(",")  # make a newline tuple with newline[0] being the name, newline[1] being the money spent
        # print(newline)  
        
        # tickets = newline[0]*int(float(newline[-1])/0.25)
        num = int(float(newline[-1])/0.25)  # number of tickets the person should receive
        
        for n in range(num+1):  # every ticket appends his name once to the list of names
            namelister.append(newline[0])
        print("length",len(namelister))  # checking for the right amount of tickets
    
    w = open("results.txt","w+")
    w.write(str(namelister))  # writing a file with all the names, check if everything is correct
    ticketnum = len(namelister)  # total number of tickets
    random.seed()  # uses system time as random
    chosen_one = random.randrange(ticketnum)  # chooses one random ticket
    print(chosen_one)
    print(namelister[chosen_one])  # check for the name in the list with said index
    
sorter()
