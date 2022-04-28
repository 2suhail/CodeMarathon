from random import randrange
from time import sleep
def string_in(input_string):
    in_string = input_string.lower()#converting to lowercase
    length_in = len(in_string) 
    str_list = list(in_string) #converting to list
    return length_in, str_list

def random_number_generate(length_in, no_of_tries):
    random_num = []
    for i in range(length_in):
        j = randrange(38)
        random_num.append(j)
    no_of_tries += 1
    return random_num, no_of_tries

def alphabet_generator(random_num,alphabets):
    guessed_str = []
    for i in random_num:
        j = alphabets[i]
        guessed_str.append(j)
    return guessed_str

def str_supervisor(input_str_list,guessed_str):
    length_in = len(input_str_list)
    accuracy_count = 0
    accuracy_percent = 0
    wrong_index = []
    for i in range(length_in):
        if ord(input_str_list[i]) == ord(guessed_str[i]):
            accuracy_count = accuracy_count + 1
        else:
            wrong_index.append(i)
    accuracy_percent = (accuracy_count / length_in) * 100
    return accuracy_percent, wrong_index

def str_inserter(guessed_str, guessed_alphabets, wrong_index):
    for i in wrong_index:
        del guessed_str[i]
        k = wrong_index.index(i) #just for observation
        guessed_str.insert(i, guessed_alphabets[wrong_index.index(i)])
    else:
        pass
    return guessed_str

def main():
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
    ',','.','"',"'",'?',':',';','!','&','-','/']
    print('This is an infinite monkey program. Valid inputs are all alphabets including spaces and' + ','+'.'+'"'+"'"+'?'+':'+';'+'!'+'&'+'-'+'/')
    input_string = input("Enter a string: ")
    accuracy_percent = 0
    random_num = []
    wrong_index = []
    no_of_tries = 0
    guessed_str = []
    length_in, input_str_list = string_in(input_string)
    random_num, no_of_tries = random_number_generate(length_in, no_of_tries)
    guessed_alphabets = alphabet_generator(random_num, alphabets)
    guessed_str = guessed_alphabets
    accuracy_percent, wrong_index = str_supervisor(input_str_list, guessed_str)

    while accuracy_percent != 100:
        length_in = len(wrong_index)
        random_num, no_of_tries = random_number_generate(length_in, no_of_tries)
        guessed_alphabets = alphabet_generator(random_num, alphabets)
        guessed_str = str_inserter(guessed_str, guessed_alphabets, wrong_index)
        accuracy_percent, wrong_index = str_supervisor(input_str_list, guessed_str)
        out_s = ''.join([str(elem) for elem in guessed_str])
        print(out_s, end="\r")
        sleep(0.10)

    print('It took', no_of_tries, 'tries to find: ',out_s)

if __name__ == "__main__":
    main()