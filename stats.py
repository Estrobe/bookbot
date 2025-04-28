


def get_word_count(text):

    count = 0
    words = []
    
    words = text.split()

    for word in words:
        count += 1

    return count


def get_char_count(text):

    chars = {}

    
    text = text.lower()
    text = list(text)
    
    for l in text:
        if l in chars:
            chars[l] += 1
        else: chars[l] = 1

    return chars


def sortdict(dict):

    sortedDicts = []
    
    keyList = list(dict.keys())
    valueList = list(dict.values())

    for i in range(0,len(keyList)):
        dictEntry = {"name":keyList[i],"num":valueList[i]}
        sortedDicts.append(dictEntry)
   
    def sort_on(dict):
        return dict["num"]

    sortedDicts.sort(reverse=True, key=sort_on)
        
    

    return sortedDicts

def sort_format(dict):
    string = ""
    sortedDicts = sortdict(dict)
    
    
    keyList = list(dict.keys())
    valueList = list(dict.values())


   
    for i in range(0,len(keyList)):
        if (sortedDicts[i]['name'].isalpha()):
            string += f"{sortedDicts[i]['name']}: {sortedDicts[i]['num']}\n"



    return string

    
