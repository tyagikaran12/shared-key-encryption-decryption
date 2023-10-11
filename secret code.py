import string
import random

n = 0
while n<=20:
    n+=1
    l1 = [1, 2, 3]
    choice = int(input("Enter 1 for encoding or 2 for decoding or 3 for exit : "))
    if (choice == l1[0]):
        print("ENCODING : \n")
        characters = input("Enter the message : ")
        words = characters.split(" ")
        nwords = []
        lt1 = "qwertyuiopasdfghjklxcvbnm1234567890~!@#$%^&*()_+{}:<>?,./;'[]-="
        lt2 = [2, 3, 4, 5]
        i = random.choice(lt2)
        key = ""

        n = 0
        while n <= i:
            key += random.choice(lt1)
            n += 1

        print("Key is : " + key)

        length = 2
        for word in words:
            if len(word) >= 3:
                res1 = ''.join(random.choices(string.ascii_letters, k=len(key)))
                res2 = ''.join(random.choices(string.ascii_letters, k=len(key)))
                res3 = ''.join(random.choices(string.ascii_letters, k=len(key)))
                str1 = word[:length]
                str2 = word[length:]
                stnew = str(res1) + str1 + str(res2) + str2 + str(res3)
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])

        print("Cipher text is : " + "$".join(nwords))

    if choice == l1[1]:
        print("DECODING : \n")
        decode = input("Enter to decode : ")
        words2 = decode.split("$")
        newords = []
        key = input("Enter the key : ")
        length = 2
        for i in words2:
            if len(i) >= 3:
                r2 = i[len(key):-len(key)]
                r3 = r2[length:]
                r4 = r3[len(key):]
                r5 = r2[:length]
                stnew2 = r5 + r4
                newords.append(stnew2)
            else:
                newords.append(i[::-1])

        print("Original message is : " + " ".join(newords))

    if choice == l1[2]:
        quit()
