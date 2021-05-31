# STRINGS

# Coded Correspondence

# To code and decode various messages

# Decode Message (with an offset of 10). 
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj?  yj'i ubucudjqho, co tuqh mqjied!  iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)  
# output
# this is an example of a caesar cipher. were you able to decode it?  it's elementary, my dear watson!  send me a message back with the same offset!

# Code Message (with an offset of 10). 
message_for_s = "hello sherlock! every budding investigator knows this! what else have you got?"
translated_message = ""
for letter in message_for_s:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value - 10) % 26]
    else:
        translated_message += letter
print(translated_message)
# output
# xubbe ixuhbesa! uluho rkttydw ydluijywqjeh ademi jxyi! mxqj ubiu xqlu oek wej?

# Define two functions decoder(message, offset) and coder(message, offset) that can be used to easily decode and code messages given any offset.
def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
    
def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

message_one = "kyv fwwjvk wfi kyv jvtfeu dvjjrxv zj knvcmv."
# message one uses an offset of 9 but advises message two will be solved with a different offset number.
print(decoder(message_one, 9))
# output
# the offset for the second message is twelve.

#  message two is solved by using the offset mentioned by message one.
message_two = "dsftcfawbu aizhwdzs qosgof qwdvsfg vszdg aoys qcrsr asggousg acfs gsqifs!"

print(decoder(message_two, 12))
# output
# performing multiple caesar ciphers helps make coding messages more secure!
