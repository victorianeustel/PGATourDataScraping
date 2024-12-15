from dotenv import load_dotenv

from classes.tour.year import Year
from classes.players.player import Player
from classes.players.player_profile_career import *
from classes.tournaments.schedule import *

from helpers.file_helper import *
from helpers.json_data_mapping import *
from helpers.csv_helper import *
from helpers.pga_data_calls import *

from tasks.player_tasks.player_career_profile_task import *
from tasks.player_tasks.players_directory_task import *
from tasks.player_tasks.player_stats_task import *
from tasks.tournament_tasks.schedule_task import *
from tasks.merge_stats_task import *

from assets.us_states import *

load_dotenv()
set_api_key(os.environ.get('PGA_TOUR_API_KEY'))

# from tasks.courses_tasks.course_stat_detail_task import *

# df = get_all_tournament_ids()

# print(df)

all_states = get_all_states()

# for state in all_states[0:1]:
#     state = 'US-' + state
#     usga_path = 'https://ncrdb.usga.org/courseTeeInfo?CourseID=2113'
#     response = requests.get(usga_path)
#     print(response.text)
#     # print(usga_path)
    
# "https://ncrdb.usga.org/NCRListing?handler=LoadCourses", {
headers = {
    "requestverificationtoken": "CfDJ8O96VO4SddFMoy-YgviOTdOlA-y5kafjR_cNMW1lg5Vp5OGne-cGn_8Vh9M989NLOlrfGzAfGiL93yi376nfcvmWz0JoNEuQrXnEkGYBaV1zNAtES1WhE6HrT___WO6Ts7xsjeOVWbaZRQzY70p3Tq0",
  }

from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

baseurl = "https://ncrdb.usga.org/"

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

select = Select(mydriver.find_element(By.ID, 'ddlStates'))
select.select_by_value('US-AL')

#Click Login button
# wait = WebDriverWait(mydriver, 20)
# element = wait.until(EC.element_to_be_clickable(ele))
# element.click()
ele = mydriver.find_element(By.ID, 'myButton')
mydriver.execute_script("arguments[0].click();", ele)


# mydriver.find_element(By.ID, 'myButton').click()
        
