def bisiesto(anno:int)->bool:
        
    return(anno%4==0 and anno%100!=0) or (anno%400==0)
    


def num_of_day (month:int, anno:int)->int:

    if month  in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2 and bisiesto(anno):
        return 29
    else:
        return 28
    



def calculate_juliano_day(day:int,month:int,anno:int)->int:
    juliano_day=0

    for i in range(1,month):
        juliano_day+= num_of_day(i,anno)
    
    juliano_day += day

    return juliano_day





if __name__=="__main__":
    day = int(input("Give a day: "))
    month =int(input("Give a month: "))
    anno = int(input("Give a anno: "))

    print(calculate_juliano_day(day,month,anno))

