# RedpwnCTF 2019

- [RedpwnCTF 2019](#redpwnctf-2019)
  - [Web](#web)
    - [easycipher](#easycipher)
  - [Cryptography](#cryptography)
    - [Dunce Crypto](#dunce-crypto)
  - [Misc](#misc)
    - [Redpwn Gets Bamboozled](#redpwn-gets-bamboozled)

## Web

### easycipher

Page prompts for login on load. To bypass this and look at the code, i did the following:

- Open Devtools -> Debugger -> {index}

- Extract Javascript from page to editor, format.

- Look at extracted JS, notice `CalcMD5` function. Code seems to be obfuscated version of MD5 calculation. Now, to find out what to decode!

- Notice what seems to be a "password check" function, alerting different values of array `var _0x29a9` on submission.

- in Devtools console, check values of `_0x29a9` - result: `(9) [ "0123456789abcdef", "", "charAt", "length", "charCodeAt", "What is the password", "aa42b234cb05915716c1434058fe1aee16c14340cb059157aa42b234", "submit as redpwnctf{PASSWORD}", ":(" ]`

- Notice value `aa42b234cb05915716c1434058fe1aee16c14340cb059157aa42b234`. check https://md5.gromweb.com/ for reverse value - success! string `shazam` was reversed.

- submit flag as redpwnctf{shazam}

## Cryptography

### Dunce Crypto

Desc: Emperor Caesar encrypted a message with his record-breaking high-performance encryption method. You are his tax collector that he is trying to evade. Fortunately for you, his crown is actually a dunce cap. `mshn{P_k0ua_d4ua_a0_w4f_tf_ahe3z}`

- Flag is formatted caesar cypher. Plug into any caesar cipher decoder with shift -7 - get `flag{I_d0nt_w4nt_t0_p4y_my_tax3s}`

- easy points!

## Misc

### Redpwn Gets Bamboozled

Challenge consists of a txt file containing two lines - line 1 describing dimensions (800 600) of an image, line 2 containing the RGB values of said image in format ((255, 12, 0), (255, 12, 0), ...)

- Download data to local machine.

- Replace all ( with [, and all ) with ] to get text representing Python-style space-seperated lists.
  