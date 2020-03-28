from get4W import *
from image_ddgo_5W1h import *
from image_ddgo_who_PERSON import *
#import spacy

#nlp = spacy.load("en_core_web_lg")

#ua = str(UserAgent().random)

def result_links(post_text,post_title,post_Complete_Text,post_Manual_links):
    result =[]
    text_5W=[]
    list_values=[]
        
    post_title=post_title.replace(":",'-')
    result_5W1H = extract_4W(post_Complete_Text)
    
    for v in result_5W1H:
        if v in ['who','what','where']:#,'where'
            if result_5W1H[v]:
                text_5W.append(result_5W1H[v])
    
    text_url=" ".join(text_5W)
    text_url=text_url.replace('..','.')
    
    list_values.append(text_url)
    
    for i in range(len(list_values)):
        result.append(urlfinder(list_values[i]))
                    
    result_links = []
    
    for i in result: 
        if len(i[0]) <= 7:
            result_links.extend(i[0])
        else:
            new_link = i[0]
            new_link = new_link[0:9]
            result_links.extend(new_link)
            new_link = []
        
    result_links=list(set(result_links))  
    
    if len(result_links)==0:
        result_links = []
        list_values  = []
        result       = []
        
        list_values=main_(post_Complete_Text)
        text_url=" ".join(list_values)
        
        for i in range(len(list_values)):
            result.append(urlfinder(list_values[i]))    
            
        for i in result: 
            if len(i[0]) <= 7:
                result_links.extend(i[0])
            else:
                new_link = i[0]
                new_link = new_link[0:9]
                result_links.extend(new_link)
                new_link = []            
       
        result_links=list(set(result_links))  

    return result_links

