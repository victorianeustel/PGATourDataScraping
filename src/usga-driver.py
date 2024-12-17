import time
import pandas as pd

from classes.usga.course_summary import *
from helpers.csv_helper import *

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

create_or_append_csv(path=USGA_CourseSummary.csv_path, 
                    fileName= USGA_CourseSummary.csv_file_name,
                    header=USGA_CourseSummary.header, 
                    fileWritingType='w')

def pull_table_data(rows):
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        facility_name = cols[0].text
        
        course_name = cols[1].text
        a_ele = cols[1].find_element(By.TAG_NAME, "a")
        course_detail_path = a_ele.get_attribute('href')
        
        course_id = int(course_detail_path.split('https://ncrdb.usga.org/courseTeeInfo?CourseID=')[1])
        
        city = cols[2].text
        state = cols[3].text
        
        course = USGA_CourseSummary(course_id, facility_name, course_name, city, state, course_detail_path)
        course.AddToCSV()
            
baseurl = "https://ncrdb.usga.org/"

options = Options()
options.add_experimental_option("detach", True)

mydriver = webdriver.Chrome(options=options)
mydriver.get(baseurl)

# Select state
state_select = Select(mydriver.find_element(By.ID, 'ddlStates'))
state_select_options = [state.get_attribute('value') for state in state_select.options]

print(state_select_options)

for index, state in enumerate(state_select_options[31:len(state_select_options)]):
    print(str(index) + ' - ' + state)
    state_select.select_by_value(state)

    # Click submit form
    ele = mydriver.find_element(By.ID, 'myButton')
    mydriver.execute_script("arguments[0].click();", ele)

    # Wait for datatable result to load 
    time.sleep(2)

    # Updated current selection filter to 100 from 10
    try : 
        filter_len_select = mydriver.find_element(By.XPATH, "//div[@id='resultTable_length']//select[@name='resultTable_length']")
        filter_select = Select(filter_len_select)
        filter_select.select_by_value('100')

        table_next_button = mydriver.find_element(By.ID, 'resultTable_next')

        # Get result table
        while True:
            table = mydriver.find_element(By.ID, 'resultTable')
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            pull_table_data(rows)

            time.sleep(1)
            
            table_next_button = mydriver.find_element(By.ID, 'resultTable_next')
            if ('disabled' in table_next_button.get_attribute('class').split()):
                break
            
            mydriver.execute_script("arguments[0].click();", table_next_button)
    except:
        continue

# Delete null rows 
df = pd.read_csv('data/usga/usga_courses.csv', sep=',')
df = df.dropna()
df.to_csv('data/usga/usga_courses.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
