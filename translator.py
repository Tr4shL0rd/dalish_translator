"""DRAGON AGE ELVISH LANGUAGE TRANSLATOR"""
import csv


def fill_list(file_name:str, index:int=0|1):
    """
    Fills a list

    PARAMS:
    -------
        * file_name `str`: the name of the file containing the translations
        * index `int`: csv index
    
    RETURNS:
    --------
        * the filled list
    """

    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        return [lang[index].replace("\"","") for lang in reader]

def translate(elvish_word:str, display_unknow=True) -> str:
    """
    returns the english translated word

    PARAMS:
    -------
        * elvish_word `str`: The elvish word you want translated

    RETURNS:
    --------
        * the translated word
    """

    file_name = "dictionary.csv"
    english = fill_list(file_name=file_name, index=1)
    elvish = fill_list(file_name=file_name, index=0)
    translator =  {english[i]: elvish[i] for i in range(len(english))}
    error_on_get = "[UNKNOWN]" if display_unknow else elvish_word
    return translator.get(elvish_word.lower(),error_on_get).strip()

sentence = "Emma Solas him var din'an"
for word in sentence.split(" "):
    print(translate(word.lower().strip(), False), end=" ")