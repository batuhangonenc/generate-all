## Welcome to GenerateAll Project Website

GenerateAll is a password generator that uses data science to increase security.

### Rating for secure passwords

The rating algorithm that GenerateAll uses is below.
```markdown

def ratePassword(pw):
    basics =  ["1","2","3","4","5","6","7","8","9","0","q","w",
"e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P","a","s","d","f","g","h","j","k",
"l","A","S","D","F","G","H","J","K","L","z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]

    specials =  ["&","$","'","|","=","!","@","#","%","^","*","(",")","+","[","]","{","}","?","/","~",":",
";","~"]

    basicnum = 0
    specnum = 0
    rating = 0

    for i in basics:
        if pw.count(i) > 0:
            basicnum += pw.count(i)

    for i in specials:
        if pw.count(i) > 0:
            specnum += pw.count(i)


    if specnum == 0:
        specnum = 1

    rating = basicnum / specnum
    
    return rating
```

<!--
### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/batuhangonenc/generate-all/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
-->

### an example for save file

```markdown
u%Y&!uCE*nMEYck

Sb1#9PX3$yZrhY/

d#JJaj^ibWM*(ST

@NYeo~Q@*@@o91E

yU>?BAS-7j@uQ5w

3_jl@=2H>iFNpF/

(ecL-%Ew0_a*QRg

|=2*tx+m/g''O56

q]r7C^$>s/~_Q!b

uzn18R<gHI#Zl[0



10 passwords above

most secure passwords

1. q]r7C^$>s/~_Q!b , rating : 0.875

2. |=2*tx+m/g''O56 , rating : 1.1428571428571428

3. @NYeo~Q@*@@o91E , rating : 1.2857142857142858

4. 3_jl@=2H>iFNpF/ , rating : 2.5

5. u%Y&!uCE*nMEYck , rating : 2.75



most used characters

1. @ , used for 6 times

2. * , used for 5 times

3. u , used for 4 times

4. Q , used for 4 times

5. E , used for 4 times

less used characters

1. 4 , used for 0 times

2. ) , used for 0 times

3. { , used for 0 times

4. } , used for 0 times

5. f , used for 0 times



&  , used for 1 times

$  , used for 2 times

'  , used for 2 times

|  , used for 1 times

1  , used for 3 times

2  , used for 2 times

3  , used for 2 times

4  , used for 0 times

5  , used for 2 times

6  , used for 1 times

7  , used for 2 times

8  , used for 1 times

9  , used for 2 times

0  , used for 2 times

-  , used for 2 times

=  , used for 2 times

!  , used for 2 times

@  , used for 6 times

#  , used for 3 times

%  , used for 2 times

^  , used for 2 times

*  , used for 5 times

(  , used for 2 times

)  , used for 0 times

+  , used for 1 times

q  , used for 1 times

w  , used for 2 times

e  , used for 2 times

r  , used for 2 times

t  , used for 1 times

y  , used for 2 times

u  , used for 4 times

i  , used for 2 times

o  , used for 2 times

p  , used for 1 times

[  , used for 1 times

]  , used for 1 times

Q  , used for 4 times

W  , used for 1 times

E  , used for 4 times

R  , used for 2 times

T  , used for 1 times

Y  , used for 4 times

U  , used for 1 times

I  , used for 1 times

O  , used for 1 times

P  , used for 1 times

{  , used for 0 times

}  , used for 0 times

a  , used for 2 times

s  , used for 1 times

d  , used for 1 times

f  , used for 0 times

g  , used for 3 times

h  , used for 1 times

j  , used for 3 times

k  , used for 1 times

l  , used for 2 times

A  , used for 1 times

S  , used for 3 times

D  , used for 0 times

F  , used for 2 times

G  , used for 0 times

H  , used for 2 times

J  , used for 2 times

K  , used for 0 times

L  , used for 1 times

z  , used for 1 times

x  , used for 1 times

c  , used for 2 times

v  , used for 0 times

b  , used for 3 times

n  , used for 2 times

m  , used for 1 times

?  , used for 1 times

/  , used for 4 times

~  , used for 2 times

Z  , used for 2 times

X  , used for 1 times

C  , used for 2 times

V  , used for 0 times

B  , used for 1 times

N  , used for 2 times

M  , used for 2 times

<  , used for 1 times

>  , used for 3 times

it took about 0.00756072998046875 seconds to compute

12/21/20 03:40:02
```
