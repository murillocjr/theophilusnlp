import json

def wholeChapter(chapter_dict):

    verses_text = [] 

    for content in chapter_dict['data']['content']:
        for item in content['items']:
             verses_text.append(item['text'])

    return ''.join(verses_text)
