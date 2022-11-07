import math
import time


class Bsic_Calc:

    def GCD_Valid_Calc(self, num1, num2):
        return math.gcd(num1, num2)

    def Multiplicative_Inverse(self, num, mod):
        GError = self.GCD_Valid_Calc(num, mod)
        t1=0
        t2=1
        r1=mod
        r2=num

        if GError !=1:
            print('The gcd is not ONE!')
            print('\n\n********\n\n\n Error: The gcd is not ONE!(Numbers are not coprime) \n\n\n*********\n\n')
        else:
            ### implementing extented Euclidian Algorithm ###
            while r2!=0:
                #calculating
                q = int(r1/r2)
                t = t1-(q*t2)
                r = (r1 % r2)
                #replacing
                r1 = r2
                r2 = r
                t1 = t2
                t2 = t         
            if t1 <0:
                return (mod + t1)
            else:
                return t1


    def Additative_Inverse(self, num, mod):

        return (mod - num)


class Enc_Dec:
    alphabet_number_dic = {
        'a' : 0, 
        'b' : 1, 
        'c' : 2, 
        'd' : 3, 
        'e' : 4, 
        'f' : 5, 
        'g' : 6, 
        'h' : 7, 
        'i' : 8, 
        'j' : 9, 
        'k' : 10, 
        'l' : 11, 
        'm' : 12, 
        'n' : 13, 
        'o' : 14, 
        'p' : 15, 
        'q' : 16, 
        'r' : 17, 
        's' : 18, 
        't' : 19, 
        'u' : 20, 
        'v' : 21, 
        'w' : 22, 
        'x' : 23, 
        'y' : 24, 
        'z' : 25
    }
    # list out keys and values separately
    alphabet_number_dic_key_list = list(alphabet_number_dic.keys())
    alphabet_number_dic_val_list = list(alphabet_number_dic.values())
    multip_valid_key_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

    mod = 26

    def additive_cipher_Encryption(self, letter, key):
        letter_number = self.alphabet_number_dic[letter]
        enc_letter_num = ((letter_number + key)%self.mod)
        Lindex = self.alphabet_number_dic_val_list.index(enc_letter_num)

        return self.alphabet_number_dic_key_list[Lindex]

    def additive_cipher_Decryption(self, letter, key):
        letter_number = self.alphabet_number_dic[letter]
        enc_letter_num = ((letter_number - key)%self.mod)
        Lindex = self.alphabet_number_dic_val_list.index(enc_letter_num)

        return self.alphabet_number_dic_key_list[Lindex]

    def additive_cipher_sentence_Encryption(self, Sentence, key):
        word_list = list(Sentence)
        enc_sent = ''
        
        for let in word_list:
            enc_word = self.additive_cipher_Encryption(let, key)
            enc_sent = enc_sent + enc_word

        return enc_sent

    def additive_cipher_sentence_Decryption(self, Sentence, key):
        word_list = list(Sentence)
        dec_sent = ''
        for let in word_list:
            dec_word = self.additive_cipher_Decryption(let, key)
            dec_sent = dec_sent + dec_word
            
        return dec_sent

    def multiplicative_cipher_Encryption(self, letter, key):
        letter_number = self.alphabet_number_dic[letter]
        enc_letter_num = ((letter_number * key)%self.mod)
        Lindex = self.alphabet_number_dic_val_list.index(enc_letter_num)

        return self.alphabet_number_dic_key_list[Lindex]

    def multiplicative_cipher_Decryption(self, letter, key):
        Calculator = Bsic_Calc()
        key = Calculator.Multiplicative_Inverse(key, self.mod)
        letter_number = self.alphabet_number_dic[letter]
        enc_letter_num = ((letter_number * key)%self.mod)
        Lindex = self.alphabet_number_dic_val_list.index(enc_letter_num)

        return self.alphabet_number_dic_key_list[Lindex]

    def multiplicative_cipher_sentence_Encryption(self, Sentence, key):
        if key in self.multip_valid_key_list:
            word_list = list(Sentence)
            enc_sent = ''
            
            for let in word_list:
                enc_word = self.multiplicative_cipher_Encryption(let, key)
                enc_sent = enc_sent + enc_word

            return enc_sent
        else:
            print('key should be in range')

    def multiplicative_cipher_sentence_Decryption(self, Sentence, key):
        if key in self.multip_valid_key_list:
            word_list = list(Sentence)
            dec_sent = ''
            for let in word_list:
                dec_word = self.multiplicative_cipher_Decryption(let, key)
                dec_sent = dec_sent + dec_word
                
            return dec_sent
        else:
            print('key should be in range')

    def autokey_cipher_Enc(self, sentence, key1):
        plaintext_list = list(sentence)
        Lindex = self.alphabet_number_dic_val_list.index(key1)

        key_char = self.alphabet_number_dic_key_list[Lindex]
        
        key_list = [key_char] + plaintext_list[:-1]
        key_list_num = map (lambda char: self.alphabet_number_dic[char], key_list)

        message = ''
        for index, item in enumerate(plaintext_list):
            # hashed_char = ((item + key_list[index]) % self.mod)
            hashed_char_num = ((self.alphabet_number_dic[item] + self.alphabet_number_dic[key_list[index]]) % self.mod)
            Lindex = self.alphabet_number_dic_val_list.index(hashed_char_num)
            hash_char = self.alphabet_number_dic_key_list[Lindex]
            message = message + hash_char

        # key_string = ''.join(key_list)
        key_string = ' '.join([str(elem) for elem in key_list_num]) 
        print('\n\n********\n\n\n\nthe message is: {} \n\n\n*********\n\n'.format(message)) 
        print('\n\n********\n\n\n\nthe key  is: {} \n\n\n*********\n\n'.format(key_string)) 
    
    def autokey_cipher_Dec(self, sentence, key_array):
        plaintext_list = list(sentence)
        
        key_list_temp = key_array.split()
        key_list_num = list (map (lambda item: int(item), key_list_temp))
        key_list = []

        for item in key_list_num:
            Lindex = self.alphabet_number_dic_val_list.index(item)           
            key_list.append(self.alphabet_number_dic_key_list[Lindex])

        print('char key list is :   {}'.format(key_list))

        message = ''
        for index, item in enumerate(plaintext_list):
            # hashed_char = ((item + key_list[index]) % self.mod)
            print('cipher text list is:  {}'.format(plaintext_list))
            hashed_char_num = ((self.alphabet_number_dic[item] - self.alphabet_number_dic[key_list[index]]) % self.mod)
            print(hashed_char_num)
            Lindex = self.alphabet_number_dic_val_list.index(hashed_char_num)
            hash_char = self.alphabet_number_dic_key_list[Lindex]
            message = message + hash_char

        print('\n\n********\n\n\n\nthe message is: {} \n\n\n*********\n\n'.format(message))     


class Attacks:
    multip_valid_key_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    alphabet_number_dic = {
        'a' : 0, 
        'b' : 1, 
        'c' : 2, 
        'd' : 3, 
        'e' : 4, 
        'f' : 5, 
        'g' : 6, 
        'h' : 7, 
        'i' : 8, 
        'j' : 9, 
        'k' : 10, 
        'l' : 11, 
        'm' : 12, 
        'n' : 13, 
        'o' : 14, 
        'p' : 15, 
        'q' : 16, 
        'r' : 17, 
        's' : 18, 
        't' : 19, 
        'u' : 20, 
        'v' : 21, 
        'w' : 22, 
        'x' : 23, 
        'y' : 24, 
        'z' : 25
    }
    # Frequency of occurence of letters
    fool_list = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'q', 'x', 'z']

    def Brute_Force_Attack(self, sentence):
        Encrypter_Decrypter = Enc_Dec()
        for key in range(0, 25):
            # print('the message with key    "{}"  is:'.format(key))
            ans = Encrypter_Decrypter.additive_cipher_sentence_Decryption(sentence, key)
            print('\n\n********\n\n\n\nthe message with key    "{}"  is: {} \n\n\n*********\n\n'.format(key, ans))
            time.sleep(2)

    def Statistical_Attack(self, sentence):
        Encrypter_Decrypter = Enc_Dec()
        msg_given = sentence
        msg_alpha = sorted(msg_given)
        sorted_letter_list = sorted(msg_alpha, key=lambda c: msg_alpha.count(c))

        for letter in sorted_letter_list:
            for fletter in self.fool_list:
                key = abs(self.alphabet_number_dic[letter] - self.alphabet_number_dic[fletter])
                # print('the message with key    "{}"  is:'.format(key))
                ans = Encrypter_Decrypter.additive_cipher_sentence_Decryption(sentence, key)
                print('\n\n********\n\n\n\nthe message with key    "{}"  is: {} \n\n\n*********\n\n'.format(key, ans))
                time.sleep(2)


def Starter_func():

    while True:
        print('\n\nselect From menu:\n')

        print('1. GCD Calc\n\
               2. Multiplicative_Inverse Calc\n\
               3. Additative_Inverse Calc\n\
               4. for Encrypting using additive cipher\n\
               5. for Decrypting using additive cipher\n\
               6. for Encrypting using multiplicative cipher\n\
               7. for Decrypting using multiplicative cipher\n\
               8. for Encrypting using autokey cipher\n\
               9. for Decrypting using autokey cipher\n\
               10. for Brute force Attack\n\
               11. for Statistical Attack\n\
               \n\nfor quiting type "exit".\n')
               
        MChoice = str(input())
        Calculator = Bsic_Calc()
        Encrypter_Decrypter = Enc_Dec()
        Attacker = Attacks()
        if MChoice == '1':
            print('Enter  first Number:')
            number1 = int(input())
            print('Enter second Number:')
            number2 = int(input())
            ans = Calculator.GCD_Valid_Calc(number1, number2)
            print('\n\n********\n\n\nthe GCD of {} and {} is     {}\n\n\n*********\n\n'.format(number1, number2, ans))
        elif MChoice == '2':
            print('Enter Number:')
            number = int(input())
            print('Enter Mod:')
            mod = int(input())
            ans = Calculator.Multiplicative_Inverse(number, mod)
            print('\n\n********\n\n\nthe Multiplicative_Inverse of {} with mod {} is     {}\n\n\n*********\n\n'.format(number, mod, ans))
        elif MChoice == '3':
            print('Enter Number:')
            number = int(input())
            print('Enter Mod:')
            mod = int(input())
            ans = Calculator.Additative_Inverse(number, mod)
            print('\n\n********\n\n\nthe Multiplicative_Inverse of {} with mod {} is     {}\n\n\n*********\n\n'.format(number, mod, ans))
        elif MChoice == '4':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key = int(input())
            ans = Encrypter_Decrypter.additive_cipher_sentence_Encryption(sentence, key)
            print('\n\n********\n\n\nThe encrypted message is:\n {} \n\n\n*********\n\n'.format(ans))
        elif MChoice == '5':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key = int(input())
            ans = Encrypter_Decrypter.additive_cipher_sentence_Decryption(sentence, key)
            print('\n\n********\n\n\nThe decrypted message is:\n {} \n\n\n*********\n\n'.format(ans))
        elif MChoice == '6':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key = int(input())
            ans = Encrypter_Decrypter.multiplicative_cipher_sentence_Encryption(sentence, key)
            print('\n\n********\n\n\nThe encrypted message is:\n {} \n\n\n*********\n\n'.format(ans))
        elif MChoice == '7':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key = int(input())
            ans = Encrypter_Decrypter.multiplicative_cipher_sentence_Decryption(sentence, key)
            print('\n\n********\n\n\nThe decrypted message is:\n {} \n\n\n*********\n\n'.format(ans))
        elif MChoice == '8':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key = int(input())
            ans = Encrypter_Decrypter.autokey_cipher_Enc(sentence, key)
        elif MChoice == '9':
            print('Enter Message:')
            sentence = str(input())
            print('Enter Key:')
            key_arr = str(input())
            ans = Encrypter_Decrypter.autokey_cipher_Dec(sentence, key_arr)
        elif MChoice == '10':
            print('Enter Message:')
            sentence = str(input())
            ans = Attacker.Brute_Force_Attack(sentence)
        elif MChoice == '11':
            print('Enter Message:')
            sentence = str(input())
            ans = Attacker.Statistical_Attack(sentence)
        elif MChoice == 'exit':
            print('End of program')
            break
        else:
            print('choose from menu!')


Starter_func()
