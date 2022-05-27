def read_file_content(filename):
    # [assignment] Add your code here
    opened_file = open(filename ,  "r")
    read_file = opened_file.read()
    return read_file
    opened_file.close()
    print(opened_file)
print(read_file_content("story.txt") )

def count_words():
    text = read_file_content("story.txt")
    text = text.split()
    count = {}
    for word in text:
        print(word)
        if(word == " " or  word == "\n"):
            continue
        if word in count:
            count[word]+=1
        else:
            count[word] = 1
    print(count )

def  second_count():
        
        main_text = read_file_content("story.txt")
        total={}
        textArr = main_text.split()            
        print(len(textArr) )
        for word in textArr:
           if word in total:
               total[ word ] +=1
            
           else:
                total [ word ]  = 1

        print("all Text :", total)


def key_count():
    text_example =  read_file_content("story.txt")
    main_dict = {}
    main_dict["glass"]= text_example.count("glass")
    main_dict["half"] = text_example.count("half")
    main_dict["of"] =text_example.count("of")
    print(main_dict)
              
count_words()
second_count()
key_count()
