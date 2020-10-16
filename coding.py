#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Date: March 11, 2019
# Editor: Vim
# Operating System Used: CentOS 7 Linux

import os
import sys
import io

def change_extension(new_extension):
    new_name = sys.argv[1][:-3] + new_extension
    return new_name

def update_dictionary_encode():
    new_value = 1
    for token in mtf_list:
        dictionary[token] = new_value
        new_value = new_value+1

def encode():
    #open input and output files
    infile = open(sys.argv[1], 'r')
    out_name = change_extension("mtf") #create the output file name
    with open(out_name, encoding="latin-1", mode="w") as outfile:
        if (outfile == None):
            print("Unable to open " + out_name)
            sys.exit(1)
    
        #insert magic number
        MAGIC_NUMBER = chr(0xba)+chr(0x5e)+chr(0xba)+chr(0x11)
        for code in MAGIC_NUMBER:
            outfile.write(code)

        d_num = 1 #for dictionary values
        position = 1 #position of word in the list before move

        for line in infile:
            #tokenize the line
            line = line.strip()
            line = line.split(" ")
            master_list.extend(line)
            #deal with the words in the line
            for word in line:
                if(word==''):
                    continue
                #if the word is new add it to mtf_list and dictionary, and write correct output
                if((word in dictionary)==False):
                    mtf_list.append(word)
                    dictionary[word] = d_num
                    d_num = d_num +1
                    outfile.write(chr(128+position))
                    outfile.write(word)
                    position = position +1
                #if the word is old write correct output and move it to front
                else: 
                    outfile.write(chr(128+(position-dictionary[word])))
                    mtf_list.remove(word)
                    mtf_list.append(word)
                    update_dictionary_encode()
            outfile.write('\n')
    
def entire_dictionary_add(value, key):
    num = value
    word = key
    entire_dictionary[num] = word

def update_dictionary_decode(index_to_remove):
    temp = dictionary[index_to_remove+1]
    just_words.remove(just_words[index_to_remove])
    just_words.append(temp)
    counter = 1
    for y in just_words:
        dictionary[counter] = y
        counter+=1

def decode():
    #open input and output files
    with open(sys.argv[1], 'rb') as infile:
        #verify input file is an MTF file  
        first_four_bytes = infile.read(4)
        if not(first_four_bytes.startswith(b'\xba\x5e\xba\x11', 0, 4)):
            print("Error: file is not an MTF file")
            sys.exit(1)
        out_name = change_extension("txt") #create the output file name
        with open(out_name, encoding="latin-1", mode="w") as outfile:
            if (outfile == None):
                print("Unable to open " + out_name)
                sys.exit(1)
   
            ascii_max = 128 #largest ASCII code that can make up an input word
            string = ""
            index = 1
            numbers = []
            hex_num = infile.read(1)
            while hex_num:
                val = ord(hex_num)
                #if val>ascii_max, add string to dictionary, output correct number, reset string
                if(val>ascii_max):
                    val = val - ascii_max
                    if(string != ""):
                        entire_dictionary_add(index, string)
                        index+=1
                    string = "" 
                    numbers.append(val)
                #deal with '\n' separately
                elif(chr(val) == "\n"):
                    numbers.append(chr(val))
                #add letters to a string  
                else:
                    string = string + chr(val)
                hex_num = infile.read(1)
            #add the last word to entire_dictionary separately 
            if (string != ""):
                entire_dictionary[index] = string
            #implement MTF
            position = 1
            key = 1
            check = 1 #check next index for '\n'
            for item in numbers:
                if(item=="\n"):
                    outfile.write('\n')
                elif(item==position):
                   dictionary[key] = entire_dictionary[item]
                   outfile.write(dictionary[key]) 
                   if(numbers[check] != "\n"):
                       outfile.write(" ")
                   just_words.append(dictionary[key])
                   position+=1
                   key+=1
                else:
                    difference = position-item
                    outfile.write(dictionary[difference])
                    if(numbers[check] != "\n"):
                       outfile.write(" ")
                    #update dictionary
                    update_dictionary_decode(difference-1)
                check+=1
            
command = os.path.basename(__file__)
if __name__ == "__main__" and command == "text2mtf.py":
    if len(sys.argv)<2:
        print("Insufficient number of arguments received; please type in a file name")
        sys.exit(1)
    dictionary = {}
    master_list = [] #list of the words in the input file
    mtf_list = [] #list for MTF coding (grows as words are processed)
    encode()
elif __name__ == "__main__" and command == "mtf2text.py":
    if len(sys.argv)<2:
        print("Insufficient number of arguments received; please type in a file name")
        sys.exit(1)
    entire_dictionary = {}
    dictionary = {}
    just_words = []
    decode()
