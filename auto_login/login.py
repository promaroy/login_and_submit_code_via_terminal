from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path='/home/proma/auto5/geckodriver')

site = input('''Enter the site you wanna login
             1. codeforces
             2. codechef
             3. spoj
             4. stopstalk\n''')

if site == "codeforces":

    driver.get("https://codeforces.com/enter?back=%2F")

    user = input("enter username\n")
    username = driver.find_element_by_id("handleOrEmail")
    username.clear()
    username.send_keys(user)
    passwd = input("Enter password\n")
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(passwd)
    x_arg= '//input[@type="submit"]'
    driver.find_element_by_xpath(x_arg).click()

    ans = input("Wanna submit a code?(yes/no)\n")
    if ans == "yes":
        driver.get("https://codeforces.com/problemset/submit")
        qs = input("Enter problem code\n")
        qsc = driver.find_element_by_name("submittedProblemCode")
        qsc.clear()
        qsc.send_keys(qs)
        ans = input("Enter path to file\n")
        ansc = driver.find_element_by_name("sourceFile")
        ansc.clear()
        ansc.send_keys(ans)
        ask4 = input("Submit??(y/n)")
        if ask4 == "y":

            x_arg2 = '//input[@type="submit"]'
            driver.find_element_by_xpath(x_arg2).click()

elif site == "stopstalk":
    driver.get("https://www.stopstalk.com/default/user/login")

    user = input("enter email\n")
    username = driver.find_element_by_id("auth_user_email")
    username.clear()
    username.send_keys(email)
    passwd = input("Enter password\n")
    password = driver.find_element_by_id("auth_user_password")
    password.clear()
    password.send_keys(passwd)
    x_arg= '//input[@type="submit"]'
    driver.find_element_by_xpath(x_arg).click()

elif site == "codechef":
    driver.get("https://www.codechef.com/")

    user = input("enter username\n")
    username = driver.find_element_by_id("edit-name")
    username.clear()
    username.send_keys(user)
    passwd = input("enter passwd\n")
    password = driver.find_element_by_id("edit-pass")
    password.clear()
    password.send_keys(passwd)
    x_arg= '//input[@type="submit"]'
    driver.find_element_by_xpath(x_arg).click()

    ask = input("Wanna submit a code??(yes/no)\n")
    if ask == "yes":
        qs = input("Enter correct problem code\n")
        driver.get("https://www.codechef.com/submit/{}".format(qs))

        ans = input("Enter path to code\n")
        ansc = driver.find_element_by_id("edit-sourcefile")
        ansc.clear()
        ansc.send_keys(ans)
        x3_arg= '//*[contains(text(),"Submit")]'
        #driver.manage().timeouts().implicitlywait(15 TimeUnit.seconds)
        driver.implicitly_wait(1000)
        driver.find_element_by_id("edit-submit-1").click()


elif site == "spoj":
    driver.get("https://www.spoj.com/")
    Xpath ='//a[@href="/login"]'
    driver.find_element_by_xpath(Xpath).click()
    user = input("enter username\n")
    username = driver.find_element_by_name("login_user")
    username.clear()
    username.send_keys(user)
    passwd = input("enter password\n")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(passwd)
    x_arg= '//*[contains(text(),"sign in")]'
    driver.find_element_by_xpath(x_arg).click()

    ask = input("Wanna submit a code??(yes/no)\n")
    if ask == "yes":
        qs = input("Enter correct problem code\n")
        driver.get("https://www.spoj.com/submit/{}".format(qs))

        ans = input("Enter path to code\n")
        ansc = driver.find_element_by_id("subm_file")
        ansc.clear()
        ansc.send_keys(ans)
        lang = input("enter language\n")
        s3= Select(driver.find_element_by_id("lang"))

        s3.select_by_visible_text(lang)
        ask1 = input("submit??(y/n)\n")
        if ask1 == "y":

        #l.clear()
        #l.send_keys(lang)
        #x3_arg= '//*[contains(text(),"Submit")]'
        #driver.manage().timeouts().implicitlywait(15 TimeUnit.seconds)
            driver.find_element_by_id("submit").click()
else:
    print("Enter a valid name...eg-spoj\n")
