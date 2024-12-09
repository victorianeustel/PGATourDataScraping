import json

def LoadJSON():
    f = open('data/detail.json')
    return json.load(f)
    
data = LoadJSON()

def IsMappingJSONLoaded():
    if data:
        return True
    return False


def GetStatCategories():
    
    if IsMappingJSONLoaded() == False:
        LoadJSON()

    categories = data['pageProps']['statDetails']['statCategories']
    
    return categories

def GetYears():
    if IsMappingJSONLoaded() == False:
        LoadJSON()
        
    years = data['pageProps']['statDetails']['yearPills']
    
    return years
