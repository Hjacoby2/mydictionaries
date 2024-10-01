import json
infile = open('school_data.json', 'r')
schools = json.load(infile)
print(type(schools))  


conference_schools = [372, 108, 107, 130]


print(len(schools))


for school in schools:
    print(type(school))  
    conf_number = school['NCAA']['NAIA conference number football (IC2020)']
    

    if conf_number in conference_schools:
        grad_rate = school['Graduation rate women (DRVG2020)']
        
       
        if grad_rate > 75:
            print(f"University Name: {school['instnm']}")
            print(f"Graduation rate for Women: {grad_rate}")
            print()
        
      
        tuition = school['Total price for in-state students living off campus']
        
       
        if tuition > 60_000:
            print(f"University Name: {school['instnm']}")
            print(f"Tuition Cost: {tuition}")
            print()
