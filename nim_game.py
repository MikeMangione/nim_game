#!/usr/bin/env python
#coding=utf-8

#cool opening text from the site below
#http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
import string
import random
import time
import sys

def print_rules():
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████      '
    time.sleep(0.1)
    print '  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      '
    time.sleep(0.1)
    print '  ███    █▀    ███    ███ ███   ███   ███   ███    █▀       '
    time.sleep(0.1)
    print ' ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          '
    time.sleep(0.1)
    print '▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          '
    time.sleep(0.1)
    print '  ███    ███   ███    ███ ███   ███   ███   ███    █▄       '
    time.sleep(0.1)
    print '  ███    ███   ███    ███ ███   ███   ███   ███    ███      '
    time.sleep(0.1)
    print '  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████      '
    time.sleep(0.1)
    print '                                                            '
    time.sleep(0.1)
    print ' ▄██████▄     ▄████████                                     '
    time.sleep(0.1)
    print '███    ███   ███    ███                                     '
    time.sleep(0.1)
    print '███    ███   ███    █▀                                      '
    time.sleep(0.1)
    print '███    ███  ▄███▄▄▄                                         '
    time.sleep(0.1)
    print '███    ███ ▀▀███▀▀▀                                         '
    time.sleep(0.1)
    print '███    ███   ███                                            '
    time.sleep(0.1)
    print '███    ███   ███                                            '
    time.sleep(0.1)
    print ' ▀██████▀    ███                                            '
    time.sleep(0.1)
    print '                                                            '
    time.sleep(0.1)
    print '███▄▄▄▄    ▄█    ▄▄▄▄███▄▄▄▄                                '
    time.sleep(0.1)
    print '███▀▀▀██▄ ███  ▄██▀▀▀███▀▀▀██▄                              '
    time.sleep(0.1)
    print '███   ███ ███▌ ███   ███   ███                              '
    time.sleep(0.1)
    print '███   ███ ███▌ ███   ███   ███                              '
    time.sleep(0.1)
    print '███   ███ ███▌ ███   ███   ███                              '
    time.sleep(0.1)
    print '███   ███ ███  ███   ███   ███                              '
    time.sleep(0.1)
    print '███   ███ ███  ███   ███   ███                              '
    time.sleep(0.1)
    print ' ▀█   █▀  █▀    ▀█   ███   █▀           '
    time.sleep(2)
    print("\nThis is a terrible NIM player\n")
    time.sleep(2)
    print("The objective is to remove the last chip from the board\n")
    time.sleep(2)
    print("Each turn, you may remove as many chips as you want from a single column\n")
    time.sleep(2)
    print("The game ends when all the chips are gone!\n")
    time.sleep(2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)
    print '\n'
    time.sleep(0.2)

def y_n_answer(str):
    valid_yes_ans = ['y','yes','of course!']
    if str.lower() in valid_yes_ans:
        return True
    return False

def r_quit(str):
    valid_q_ans = ['q','quit','exit','stop']
    if str.lower() in valid_q_ans:
        return True
    else:
        return False

def r_quit_routine():
    print "Mid-game quit? Nice."
    for x in range(0,10):
        time.sleep(0.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    print '\nStarting over\n'
    time.sleep(2)
    return True

def print_table(t):
    print "\n#--------------------------#\n"
    for x in range(0,len(t)):
        print 'Column '+str(x)+':','0' * t[x],'('+str(t[x])+')'
    print "\n#--------------------------#"

def calc_table_xor(t):
    b_x = t[0]
    for x in range(1,len(t)):
        b_x = b_x ^ t[x]
    return b_x

def compy_turn(t,b_x):
    mod_temp = -1
    temp = list(set(t))
    for x in temp:
        if t.count(x)%2 == 0:
            temp.remove(x)
    for x in range(0,len(temp)):
        temp_xor = 0
        for y in range(0,len(temp)):
            if temp[x] != temp[y]:
                temp_xor = temp_xor ^ temp[y]
        if temp_xor < temp[x]:
            mod_temp = temp[x]
            temp[x] = temp_xor
            break
    if mod_temp != -1:
        t[t.index(mod_temp)] = temp[x]
    else:
        for x in range(0,len(t)):
            if t[x] != 0:
                t[x] += -1
                temp_xor = t[x]
                break
    return t, x, temp_xor

def play_nim():
    quit, loss = False, False
    cols = random.randint(2,10)
    table = []
    for x in range(0,cols):
        table.append(random.randint(1,15))
    print_table(table)
    while sum(table) > 0:
        bit_xor = calc_table_xor(table)
        print "\nTable XOR Value:",bin(bit_xor),bit_xor
        col = -1
        while int(col) < 0 or len(table) - 1 < int(col):
            col = raw_input("\nWhat column do you want to pick from? ")
            if not col.isdigit():
                if r_quit(str(col)):
                    quit, loss = True, r_quit_routine()
                    break
                else:
                    print '\nplease choose a row digit'
                    col = -1
        if quit:
            break
        count = 0
        while int(count) == 0 or table[int(col)] < int(count):
            count = raw_input("\nHow many ord(48) ASCII characters would you like to remove? ")
            if not count.isdigit():
                if r_quit(str(count)):
                    quit, loss = True, r_quit_routine()
                    break
                else:
                    print '\nplease choose a digit'
                    count = 0
        if quit:
            break
        table[int(col)] += -1 * int(count)
        if sum(table) == 0:
            break
        bit_xor = calc_table_xor(table)
        print "\nTable XOR Value:",bin(bit_xor),bit_xor
        table, rm_column, rm_count = compy_turn(table,bit_xor)
        print "\nThe computer changed column",rm_column,"to",rm_count
        print_table(table)
        if sum(table) == 0:
            loss = True
            break
    if loss:
        print '\nOh no! You lost. There\'s always next time.'
        time.sleep(0.2)
        print '(like you\'ll do better)'
    else:
        print "\nCool, you won!"

print_rules()
desire_to_play = y_n_answer(raw_input("\nWould you like to play? (y = yes) "))
while desire_to_play:
    play_nim()
    desire_to_play = y_n_answer(raw_input("\nWould you like to play again? "))
