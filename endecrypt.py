#! /usr/bin/python
import os
import time
import enquiries

import base64


os.system('clear')

print(" ")
print("@@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@@   @@@@@@@  @@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@  ")
print("@@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@  ")
print("@@!       @@!@!@@@  @@!  @@@  @@!       !@@       @@!  @@@  @@! !@@  @@!  @@@    @@!    ")
print("!@!       !@!!@!@!  !@!  @!@  !@!       !@!       !@!  @!@  !@! @!!  !@!  @!@    !@!    ")
print("@!!!:!    @!@ !!@!  @!@  !@!  @!!!:!    !@!       @!@!!@!    !@!@!   @!@@!@!     @!!    ")
print("@!!!:!    @!@ !!@!  @!@  !@!  @!!!:!    !@!       @!@!!@!    !@!@!   @!@@!@!     @!!    ")
print("!!!!!:    !@!  !!!  !@!  !!!  !!!!!:    !!!       !!@!@!      @!!!   !!@!!!      !!!    ")
print("!!:       !!:  !!!  !!:  !!!  !!:       :!!       !!: :!!     !!:    !!:         !!:    ")
print(":!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!    :!:    :!:         :!:    ")
print(" :: ::::   ::   ::   :::: ::   :: ::::   ::: :::  ::   :::     ::     ::          ::    ")
print(": :: ::   ::    :   :: :  :   : :: ::    :: :: :   :   : :     :      :           :     ")

opt = ['Encrypt' , 'Decrypt' , 'Exit']
coi = enquiries.choose ( 'Choose one of the options below: ' , opt )

if coi == ('Encrypt') :
    enopt = ['base64' , 'base32']
    encoi = enquiries.choose ( 'Choose one of the options below: ' , enopt )


    if encoi == ('base64'):
        b64text = input('Enter text for encryption -->')
        b64tbytes = b64text.encode('ascii')
        b64bytes = base64.b64encode(b64tbytes)
        b64enctext = b64bytes.decode('ascii')
        print(' ')
        print('(ignore "░" symbols)')
        print('Encrypted string --> ░' , b64enctext , '░')


    if encoi == ('base32'):
       b32text = input('Enter text for encryption -->')
       b32encutf1 = b32text.encode("UTF-8")
       b32enc = base64.b32encode(b32encutf1)
       b32encres = b32enc.decode("UTF-8")
       print ( ' ' )
       print ( '(ignore "░" symbols)' )
       print ( 'Encrypted string --> ░' , b32encres , '░' )










if coi == ('Decrypt') :
    deopt = ['base64' , 'base32']
    decoi = enquiries.choose ( 'Choose one of the options below: ' , deopt )

    if decoi == ('base64'):
        b64encmsg = input('enter encrypted string -->')
        b64encbytes = b64encmsg.encode('ascii')
        b64msgbytes = base64.b64decode(b64encbytes)
        b64decmsg = b64msgbytes.decode('ascii')
        print(' ')
        print ( '(ignore "░" symbols)' )
        print('Decrypted string --> ░' , b64decmsg , '░')

    if decoi == ('base32'):
        b32encmsg = input('enter encrypted string -->')
        b32encmsgutf1 = b32encmsg.encode('UTF-8')
        b32decode = base64.b32decode(b32encmsgutf1)
        b32decres = b32decode.decode('UTF-8')
        print(' ')
        print ( '(ignore "░" symbols)' )
        print('Decrypted string --> ░' , b32decres , '░')






if coi == ('Exit') :
    print ( ' ' )
    print ( 'Made by github.com/serv3r0' )
    exit ( )
