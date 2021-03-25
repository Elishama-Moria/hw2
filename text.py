def revword(word:str) -> str:
    word=word.lower()[::-1]
    return word

def countword() -> int:
    my_text_opened = open('text.txt', 'r')
    my_text = my_text_opened.read()
    space_text = my_text.replace('\n', ' ')
    text_list = space_text.split(' ')
    word = text_list[0].lower()
    my_word_cnt=0
    for a_word in text_list:
        if my_word_cnt==0:
            my_word_cnt+=1
        else:
            a_word=revword(a_word)
            if a_word==word:
                my_word_cnt+=1
    return my_word_cnt
