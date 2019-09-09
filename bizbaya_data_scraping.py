from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementClickInterceptedException
import pymysql
import time

print("--------------------------------WELCOME TO Bizbaya.com----------------------------------")
print("\n")
print("Connecting to database...")
time.sleep(0.2)
db = pymysql.connect("localhost", "root", "password123", "bizbayadb" )

print("Database connected!")
cursor = db.cursor()
time.sleep(0.5)

print("\nOpening Chrome...")
driver = webdriver.Chrome()

driver.get('https://www.bizbaya.com/sme-india')
state_name = search = driver.find_element_by_xpath('//*[@id="block-system-main"]/div')

state_list = state_name.text.split('\n')
print(state_list)

for state in state_list[28:]:
    print(state)
    count2 = 0
    count = 0
    driver.implicitly_wait(5)

    print("State:-", state)
    state_ = driver.find_element_by_link_text(state)
    state_.click()
    driver.implicitly_wait(5)
    dist_name = 'None'
    dist_name = driver.find_element_by_css_selector('#block-system-main > div > div > div.view-content')

    dist_list = dist_name.text.split('\n')
    print("dist list:-", dist_list)

    for dist in dist_list:
        try:
            director_name = "None"
            mobile_no = 'None'
            telephone = "None"
            fax_no = "None"
            email = "None"
            address = "None"
            pin_code = "None"
            product_and_services = "None"
            count = count+1
            print("state :-", state)
            print("Dist:-", dist)
            dist_length = len(dist_list)
            print(dist_length)
            dist_link = driver.find_element_by_link_text(dist)
            dist_link.click()
            driver.implicitly_wait(5)
            try:
                company = driver.find_element_by_css_selector('#block-system-main > div > div > div.view-content')

                company_list = company.text.split('\n')
                print("Company list :-", company_list)
                driver.implicitly_wait(5)

                for comp in company_list:
                    director_name = "None"
                    mobile_no = 'None'
                    telephone = "None"
                    fax_no = "None"
                    email = "None"
                    address = "None"
                    pin_code = "None"
                    product_and_services = "None"

                    result = comp.split(',')[:-2]
                    print("result : ", result)
                    fullStr = ','.join(result)
                    print("company name :-", fullStr)
                    link = driver.find_element_by_link_text(fullStr)
                    company_name = fullStr
                    link.click()
                    driver.implicitly_wait(5)

                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-directors > span'):
                            director = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-directors > span')
                            print("by classs dirctor name", director.text)
                            director_name = director.text
                        else:
                            director_name = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-mobile > span'):
                            mobile = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-mobile > span')
                            print(mobile.text)
                            mobile_no = mobile.text
                        else:
                            mobile_no = 'None'
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-telephone > span'):
                            tele = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-telephone > span')
                            print(tele.text)
                            telephone = tele.text
                        else:
                            telephone = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-fax > span'):
                            fax = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-fax > span')
                            print(fax.text)
                            fax_no = fax.text
                        else:
                            fax_no = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-email > span'):
                            email_ =driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-email > span')
                            print(email_.text)
                            email = email_.text
                        else:
                            email = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-address > span'):

                            address_ = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-address > span')
                            print(address_.text)
                            address = address_.text
                        else:
                            address = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-pin > span'):

                            pin = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-pin > span')
                            print(pin.text)
                            pin_code = pin.text
                        else:
                            pin_code = "None"
                    except NoSuchElementException:
                        pass
                    try:
                        if driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-products-services > span'):

                            product_services = driver.find_element_by_css_selector('#block-system-main > div > div > div > div > p.views-field.views-field-products-services > span')

                            product_and_services = product_services.text
                            product_and_services = product_and_services[:20]
                            print(product_and_services)
                        else:
                            product_and_services = "None"
                    except NoSuchElementException:
                        pass

                    total = list()

                    record = (state, dist, company_name, director_name, mobile_no, telephone, fax_no, email, address, pin_code, product_and_services)
                    total.append(record)

                    cursor = db.cursor()

                    sql = "INSERT INTO bizbaytable (state, dist, company_name, director_name, mobile_no, telephone, " \
                          "fax_no, email, address, pin_code, product_and_services)" \
                          + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

                    for data in total:
                        cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                                             data[8], data[9], data[10]))
                    db.commit()

                    print("Data Successfully Saved!")
                    count2 = count2 + 1
                    print('Total data retrieved : ', count2, "\n")

                    driver.back()
                    driver.implicitly_wait(2)

                driver.back()
                if count == dist_length:
                    driver.back()

                driver.implicitly_wait(2)

            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass

# disconnect from server
db.close()

driver.close()







