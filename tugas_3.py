Fname = input('Enter the file name: ')
try:
    with open(Fname, 'r') as file:
        count={}
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                count[email] = count.get(email, 0) + 1
                
        print (count)
except:
    print('File tersebut tidak dapat ditemukan')