import urllib

# path = 'https://www.usga.org/Home/GetClubsActionResult?clubCity=&clubState=&clubName=&assocNum=19'
def get_usga_courses(clubCity: str = "", clubState: str = "", clubName: str = "", assocNum: str = ""):
    # https://ncrdb.usga.org/NCRListing?handler=LoadCourses

    url = 'https://www.usga.org/Home/GetClubsActionResult?'
    params = {
        'clubCity': clubCity, 
        'clubState': clubState, 
        'clubName': clubName, 
        'assocNum': assocNum 
        # 'clubCountry': 
        }
    path = url + urllib.parse.urlencode(params)
    return path
