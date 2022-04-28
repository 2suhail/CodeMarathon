from random import randrange

def string_in(input_string,no_of_tries):
    in_string = input_string.lower()#converting to lowercase
    length_in = len(in_string) 
    str_list = list(in_string) #converting to list
    no_of_tries += 1
    return length_in, str_list, no_of_tries

def random_number_generate(length_in):
    random_num = []
    for i in range(length_in):
        j = randrange(27)
        random_num.append(j)
    return random_num

def alphabet_generator(random_num,alphabets):
    random_alphabets = []
    for i in random_num:
        j = alphabets[i]
        random_alphabets.append(j)
    return random_alphabets

def str_supervisor(str_list,random_alphabets,length_in):
    accuracy_count = 0
    accuracy_percent = 0
    wrong_index = []
    for i in range(length_in):
        if ord(str_list[i]) == ord(random_alphabets[i]):
            accuracy_count = accuracy_count + 1
    accuracy_percent = (accuracy_count / length_in) * 100
    return accuracy_percent

def main():
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    test_string = 'pin'
    no_of_tries = 0
    accuracy_percent = 0
    while accuracy_percent != 100:
        length_in, str_list, no_of_tries = string_in(test_string,no_of_tries)
        random_num = random_number_generate(length_in)
        random_alphabets = alphabet_generator(random_num,alphabets)
        accuracy_percent = str_supervisor(test_string,random_alphabets,length_in)
        if (no_of_tries % 1100 == 0):
            s = ''.join([str(elem) for elem in random_alphabets])
            print(s)
    
    print('It took', no_of_tries, 'tries to find',test_string) 

if __name__ == "__main__":
    main()