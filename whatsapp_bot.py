from selenium import webdriver
from consolemenu import *
from consolemenu.items import *
import random
import string
import time


def create_new_group(name_of_group, contact_name, driver):
    new_chat_btn = driver.find_elements_by_class_name('_3Kxus')
    new_chat_btn[0].click()

    new_group_btn = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]')
    new_group_btn[0].click()

    new_group_participants_txt_box = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
    new_group_participants_txt_box[0].send_keys(contact_name)

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
    time.sleep(1)
    user.click()

    next_btn1 = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span')
    next_btn1[0].click()

    new_group_name_txt_box = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
    new_group_name_txt_box[0].send_keys(name_of_group)

    next_btn2 = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div')
    next_btn2[0].click()

def exit_group(name_of_group, driver):
    group = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name_of_group))
    group.click()

    menu_btn = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[3]/div/span')
    menu_btn.click()
    time.sleep(0.5)

    exit_group_btn = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div')#!!!
    exit_group_btn.click()

    exit_btn = driver.find_element_by_xpath(' //*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
    exit_btn.click()

def delete_group(name_of_group, driver):
    time.sleep(0.5)
    group = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name_of_group))
    group.click()

    menu_btn = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
    menu_btn.click()
    time.sleep(0.5)

    delete_group_btn = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/ul/li[5]/div')
    delete_group_btn.click()
    time.sleep(0.5)

    delete_btn = driver.find_element_by_xpath(' //*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
    delete_btn.click()

def send_messages(name_of_group, count, your_msg, driver):
    group = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name_of_group))
    group.click()
    time.sleep(0.5)

    msg_box = driver.find_element_by_class_name('_2S1VP')
    for message in range(count):
        msg_box.send_keys(your_msg)
        send_button = driver.find_element_by_class_name('_35EW6')
        send_button.click()

def group_spam(driver):
    rnd_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

    name = input('Enter name of contact: ')
    group_name = input('Enter name of group you want to create: ') + "_" + rnd_string
    group_count = int(input('Enter how many times you want to create the group: '))
    your_msg = input('Enter your message: ')
    msg_count = int(input('Enter how many messages you want to send: '))

    input('\nEnter any key after scanning QR code')
    
    print('<-----Creating groups----->')
    for i in range(group_count):
        create_new_group(group_name, name, driver)
        time.sleep(1)

    for i in range(group_count):
        print("\nSending messages {}".format(str(i)))
        send_messages(group_name, msg_count, your_msg, driver)
        time.sleep(0.5)
        print("\nExit group number {}".format(str(i)))
        exit_group(group_name, driver)
        time.sleep(0.5)
        print("\nDeleting group number {}".format(str(i)))
        delete_group(group_name, driver)
        time.sleep(1.5)

def contact_spam(driver):
    name = input('Enter name of group or contact: ')
    your_msg = input('Enter your message: ')
    msg_count = int(input('Enter how many times you want to send your message: '))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    time.sleep(0.5)

    msg_box = driver.find_element_by_class_name('_2S1VP')
    print('<-----Sending messages----->')
    for message in range(msg_count):
        msg_box.send_keys(your_msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

def menu(driver):
    menu = ConsoleMenu("Whatsapp Bot v1.0", "Choose spam method")

    groupSpam = FunctionItem("Group Spam: spam by creating groups", group_spam, [driver])
    contactSpam = FunctionItem("Single Contact Or Group Spam", contact_spam, [driver])

    menu.append_item(groupSpam)
    menu.append_item(contactSpam)

    menu.show()

def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://web.whatsapp.com/')
    menu(driver)

if __name__ == "__main__":
    main()