## - code academys version. NB mine does not work since I gave up.
def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))



## - The Vigenère Cipher - this one was so confusing. But one of my solutions looked quite similar. I gave up trying to go back with this one as I think i am quite comfuszeled. 

message6 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"

keyword ="friends"

def M_shift(keyword):
    for keyLetter in keyword:
        moving_shift =  alphabet.find(keyLetter)
    return moving_shift 

movingShift = M_shift(keyword)

def Vigenère_Cipher(message, shift, keyword):
    moving_shift
     for keyLetter in keyword:
        moving_shift =  alphabet.find(keyLetter)
    return moving_shift 
    new_message6 = ""
    for letter in message6:
        if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
            new_message6 += letter #this should append a space etc if it finds a space etc
        else:
            new_index = alphabet.find(letter) + movingShift
            decoded_gylph = alphabet[(new_index) % 26]
            new_message6 += decoded_gylph
    return new_message6
    

#print(Vigenère_Cipher(message6, movingShift, keyword))



