message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

#alphabet = "pqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk" # i added on the first 10 letters to the back to avoid the problem of going out of range. I didn't understand the idea of using %. 

alphabet = "abcdefghijklmnopqrstuvwxyz" # if you add the % 26 to the code you can use the alphabet like this.

#print(alphabet.find("a")+10) # this takes in a letter and finds the index for that letter in the alphabet string. Then it adds an index number of 10 to it and prints the new index number. 
#print(alphabet[0]) # this takes in an index number and prints out a letter from the alphabet. 
#print(alphabet.find(" ")) # this find the index of a space. If they find this index we want them to print a space.

new_message = ""
for letter in message:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        new_message += letter #this should append a space etc if it finds a space etc
    else:
        new_index = alphabet.find(letter)+10
        decoded_gylph = alphabet[(new_index) % 26]
        new_message += decoded_gylph
print()
print(new_message)

ovando_message = "hi vishal, i hope this message gets to you."

coded_message = ""
for letter in ovando_message:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        coded_message += letter #this should append a space if it finds a space
    else:
        new_index = alphabet.find(letter)-10
        #print(alphabet.find(letter))
        #print(new_index)
        coded_gylph = alphabet[(new_index) % 26]
        #print((new_index) % 26)
        coded_message += coded_gylph
print()
print(coded_message)

new_decoded_message = ""
for letter in coded_message:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        new_decoded_message += letter #this should append a space etc if it finds a space etc
    else:
        new_index = alphabet.find(letter)+10
        decoded_gylph = alphabet[(new_index) % 26]
        new_decoded_message += decoded_gylph
print()
print(new_decoded_message)

## - second message sent.
message2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

new_message2 = ""
for letter in message2:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        new_message2 += letter #this should append a space etc if it finds a space etc
    else:
        new_index = alphabet.find(letter)+10
        decoded_gylph = alphabet[(new_index) % 26]
        new_message2 += decoded_gylph
print()
print(new_message2)

## - second cipher
message3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

new_message3 = ""
for letter in message3:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        new_message3 += letter #this should append a space etc if it finds a space etc
    else:
        new_index = alphabet.find(letter)+14
        decoded_gylph = alphabet[(new_index) % 26]
        new_message3 += decoded_gylph
print()
print(new_message3)

## - brute force cipher (this time I was not told the shift. I have to figure this out myself)
# the shift is 7.

message4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def coder(message, shift):
    new_message4 = ""
    for letter in message4:
        if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
            new_message4 += letter #this should append a space etc if it finds a space etc
        else:
            new_index = alphabet.find(letter)+shift
            decoded_gylph = alphabet[(new_index) % 26]
            new_message4 += decoded_gylph
    return new_message4

print()
for i in range(1,26): # this beautiful code will look at all 26 shift possibilities in one go. 
    print("shift: " + str(i))
    print("\t " + coder(message4, i) + "\n")

## - new message
message5 = "Have you been training?"

coded_message2 = ""
for letter in message5:
    if " " == letter or "!" == letter or "?" == letter or "." == letter or "," == letter:
        coded_message2 += letter #this should append a space if it finds a space
    else:
        new_index = alphabet.find(letter)-10
        #print(alphabet.find(letter))
        #print(new_index)
        coded_gylph = alphabet[(new_index) % 26]
        #print((new_index) % 26)
        coded_message2 += coded_gylph

print()
print(coded_message2)

## Code academys version. 
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
punctuation = ".,?'! "

print()
print(vigenere_decoder(message, keyword))