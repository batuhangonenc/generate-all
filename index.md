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
";","<",">","~"]

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
