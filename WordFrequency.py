def main():
    text = open("sometext-1.txt", "r") 
    mydict = {} 
    
    for line in text: 
        line = line.strip()  
        line = line.lower()  
        words = line.split(" ")  
        
        for word in words: 
            mydict[word] = mydict.get(word, 0) + 1  
            
    text.close()
    

    for key in mydict: 
        print(key, mydict[key]) 


main()
