#https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/python
#letters: abcdefghijklmnopqrstuvwxyz
def find_the_number_plate(customer_id):
    letter= "abcdefghijklmnopqrstuvwxyz"
    letters=[]
    for i in letter:
        letters.append(i)
    part2=[]
    part1=[]
    letter1=0
    letter2=0
    letter3=0
    if customer_id <= 17558423:
        if customer_id<=999:
            part1.append(letters[letter1])
            part1.append(letters[letter2])
            part1.append(letters[letter3])
            part2=[str(customer_id).zfill(3)]

    if customer_id>999:
        int=customer_id//999
        mod=customer_id%999
        if int>999:
            letter1 +=1
            int=000
            mod=000
            part1.append(letters[letter1])
            part1.append(letters[letter2])
            part1.append(letters[letter3])
            part2=[str(customer_id).zfill(3)]
        
    total=part1+part2
    return "".join(total)










customer_id=int(input("Enter here: "))
print(find_the_number_plate(customer_id))