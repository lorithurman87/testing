def rot13(mess):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    
    text = mess.split()    #split message into a list of words in it
    for word in text:      # for each word in the list
        for char in word:   #seperates each char in the word
            code = alpha.find(char)   #finds the numerical index numb of char
            total_code = code + 13    #adds 13 to the numerical index numb
            if total_code > 25:        #if the number is over 25(bc start at 0)
                total_code = total_code % 26   #divide numb by numb of char in alpha
            new_char = alpha[total_code]   #gives the new char in the caesar cipher
            msg = msg + new_char     #adds the letters back together to make word 
        blank = " "          #adds a blank at the end of each word
        msg = msg + blank    #adds the words back together to make the phrase again
    return(msg[0:-1])    #returns the msg without the blank space at the end of it

def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()
