#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# Date: March 25, 2019
# Editor: Vim
# Operating System Used: CentOS 7 Linux

import os
import sys
import io

MAGIC_NUMBER_1 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x11)
MAGIC_NUMBER_2 = chr(0xBA) + chr(0x5E) + chr(0xBA) + chr(0x12)

class Encoder:

    def __init__(self, input_file_name, output_file_name):
        #dictionary of a dictionary for encoding, a list of words in the input file, a list for implementing MTF 
        self.master_dictionary = {'encode_dictionary':{}, 'master_list':[], 'mtf_list':[]}

        self.i_name = input_file_name
        self.o_name = output_file_name
        self.main_encoder(self.i_name, self.o_name)

    def calculate_code(self, number, output_file):
        if (number<121):
            output_file.write(chr(128+number))
        elif (number>120 and number<376):
            output_file.write(chr(121+128)+chr(number-121))
        else:
            output_file.write(chr(122+128)+chr((number-376)//256)+chr((number-376)%256))

    def update_dictionary_encode(self):
        new_value = 1
        for token in self.master_dictionary['mtf_list']:
            self.master_dictionary['encode_dictionary'][token] = new_value
            new_value = new_value+1

    def main_encoder(self, input_name, output_name):

        outfile = open(output_name, encoding="latin-1", mode="w")
        if (outfile == None):
            print("Unable to open " + output_name)
            sys.exit(1)

        #insert magic number
        for code in MAGIC_NUMBER_2:
            outfile.write(code)

        d_num = 1 #for dictionary values
        position = 1 #position of word in the list before move
        infile = open(input_name, 'r')

        for line in infile:
            #tokenize the line
            line = line.strip()
            line = line.split(" ")
            self.master_dictionary['master_list'].extend(line)
            #deal with the words in the line
            for word in line:
                if(word==''):
                    continue
                #if the word is new add it to mtf_list and dictionary, and write correct output
                if((word in self.master_dictionary['encode_dictionary'])==False):
                    self.master_dictionary['mtf_list'].append(word)
                    self.master_dictionary['encode_dictionary'][word] = d_num
                    d_num = d_num +1
                    self.calculate_code(position, outfile)
                    outfile.write(word)
                    position = position +1
                #if the word is old write correct output and move it to front
                else:
                    self.calculate_code(position-self.master_dictionary['encode_dictionary'][word], outfile)
                    self.master_dictionary['mtf_list'].remove(word)
                    self.master_dictionary['mtf_list'].append(word)
                    self.update_dictionary_encode()
            outfile.write('\n')
        outfile.close()
        
def encode(input_name):
    (base_name, _, _) = input_name.rpartition(".")
    output_name = base_name + "." + "mtf"
    encoder_object = Encoder(input_name, output_name)

class Decoder:

    def __init__(self, input_file_name, output_file_name):
        #dictionary of a dictionary for entire input file, and 1 dictionary and 2 lists for implementing MTF
        self.master_dictionary = {'entire_dictionary':{}, 'decode_dictionary':{}, 'just_words':[], 'numbers':[]}

        self.i_name = input_file_name
        self.o_name = output_file_name
        self.main_decoder(self.i_name, self.o_name)

    def update_dictionary_decode(self, index_to_remove):
        moved = self.master_dictionary['decode_dictionary'][index_to_remove+1]
        self.master_dictionary['just_words'].remove(self.master_dictionary['just_words'][index_to_remove])
        self.master_dictionary['just_words'].append(moved)
        counter = 1
        for y in self.master_dictionary['just_words']:
            self.master_dictionary['decode_dictionary'][counter] = y
            counter+=1

    def get_code(self, ipt_file, hx):
        if(hx>b'\x7f' and hx<b'\xf9'): #code is from 1 to 120
            return ord(hx)-128
        elif(hx == b'\xf9'): #code is from 121 to 275
            second_code = ipt_file.read(1)
            second_code_val = ord(second_code)
            return second_code_val+121
        elif(hx == b'\xfa'): #code is from 376 to 65912
            second_code = ipt_file.read(1)
            second_code_val = ord(second_code)*256
            third_code = ipt_file.read(1)
            return 376+second_code_val+ord(third_code)

    def main_decoder(self, input_name, output_name):
        infile = open(input_name, 'rb')
        #verify input file is an MTF file
        mag_num = infile.read(4)
        if (not(mag_num.startswith(b'\xba\x5e\xba\x11', 0, 4) or mag_num.startswith(b'\xba\x5e\xba\x12', 0, 4))):
            print("Error: file is not an MTF file")
            sys.exit(1)

        with open(output_name, encoding="latin-1", mode="w") as outfile:
            if (outfile == None):
                print("Unable to open " + output_name)
                sys.exit(1)

            string = ""
            index = 1
            hex_num = infile.read(1)
            while hex_num:
                val = ord(hex_num)
                if(hex_num>b'\x7f' or hex_num == b'\xf9' or hex_num == b'\xfa'):
                    code = self.get_code(infile, hex_num)
                    if(string != ""):
                        self.master_dictionary['entire_dictionary'][index] = string
                        index+=1
                    string = ""
                    self.master_dictionary['numbers'].append(code)
                #deal with '\n' separately
                elif(chr(val) == "\n"):
                    self.master_dictionary['numbers'].append(chr(val))
                #add letters to a string
                else:
                    string = string + chr(val)
                hex_num = infile.read(1)
            #add the last word to entire_dictionary separately
            if (string != ""):
                self.master_dictionary['entire_dictionary'][index] = string
            #implement MTF
            position = 1
            key = 1
            check = 1 #check next index for '\n'
            for item in self.master_dictionary['numbers']:
                if(item=="\n"):
                    outfile.write('\n')
                elif(item==position):
                    self.master_dictionary['decode_dictionary'][key] = self.master_dictionary['entire_dictionary'][item]
                    outfile.write(self.master_dictionary['decode_dictionary'][key])
                    if(self.master_dictionary['numbers'][check] != "\n"):
                        outfile.write(" ")
                    self.master_dictionary['just_words'].append(self.master_dictionary['decode_dictionary'][key])
                    position+=1
                    key+=1
                else:
                    difference = position-item
                    outfile.write(self.master_dictionary['decode_dictionary'][difference])
                    if(self.master_dictionary['numbers'][check] != "\n"):
                        outfile.write(" ")
                    #update dictionary
                    self.update_dictionary_decode(difference-1)
                check+=1 

def decode(input_name):
    (base_name, _, _) = input_name.rpartition(".")
    output_name = base_name + "." + "txt"
    decoder_object = Decoder(input_name, output_name)
