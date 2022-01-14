from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as NoElement
from selenium.common.exceptions import StaleElementReferenceException as StaleElement
from selenium.common.exceptions import ElementNotVisibleException as NotVisible
from selenium.common.exceptions import ElementNotSelectableException as NotSelectable
from selenium.common.exceptions import ElementNotInteractableException as NotInteractable
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import sys
import os
import pathlib

"""

### THIS IS THE PRODUCT AS DELIVERED, WITH THE EXCEPTION OF COMMENTS AND VARIABLES ADDED OR TRANSLATED TO ENGLISH ###

### PLEASE READ THE README FILE IN ITS ENTIRETY BEFORE FIRST START ###

"""


def initializer():
    try:
        pathname = os.path.dirname(sys.argv[0])
        data_dir = rf'{os.path.abspath(pathname)}\FirefoxProfile\rvzud5ty.whatsweb'
        fp = FirefoxProfile(data_dir)
        options = Options()
        options.headless = False

        print("Starting WebDriver...")
        driver = webdriver.Firefox(executable_path=fr'{pathlib.Path().absolute()}\WebDriver\bin\geckodriver.exe',
                                   options=options, firefox_profile=fp)
        print("WebDriver Successfully Launched.")
        driver.get("https://web.whatsapp.com/")
        return driver
    except (NotVisible, NotSelectable, NotInteractable, NoElement, StaleElement) as error:
        print("WebDriver Failed To Initialize, Error Code: 100")
        print(error)
        pass


def msg_sender(driver, target, message):
    wait = WebDriverWait(driver, 600)  # time.sleep()
    try:
        target_int = int(target) # will throw ValueError if Contact Name was entered
        search_arg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]'
        search_number = wait.until(EC.element_to_be_clickable((By.XPATH, search_arg)))
        search_number.click()
        search_number.send_keys(target_int)
        time.sleep(4)
        search_results_xarg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div'
        clear_results_xarg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/span/button'
        driver.find_element_by_xpath(search_results_xarg + '/div').click()  # click the search result
        clear_results = wait.until(EC.element_to_be_clickable((By.XPATH, clear_results_xarg)))
        clear_results.click()  # clear the search results

        # this part is same for both contact and number
        # find and click the chatbox and type the message
        x_arg_chatbox = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
        # '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]'
        group_title_chatbox = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg_chatbox)))
        time.sleep(0.15)
        group_title_chatbox.click()
        group_title_chatbox.send_keys(message)
        time.sleep(0.1)
        # find and click the send button to send the message
        button_xarg = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[2]/button'
        sendbutton = wait.until(EC.element_to_be_clickable((By.XPATH, button_xarg)))
        time.sleep(0.15)
        sendbutton.click()
        return

    except NoElement:
        print("Coult not find phone number in chat, please make sure the number you have entered is correct.")
        return

    except ValueError:
        try:
            try:
                open_chat_xpath = "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div/div/span"
                open_chat_title = driver.find_element_by_xpath(open_chat_xpath).get_attribute('title')
                if open_chat_title == target:
                    pass
                else:
                    target = '"' + target + '"'
                    # find and click the target to be messaged
                    x_arg = '//span[contains(@title,' + target + ')]'
                    group_title = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))
                    time.sleep(0.2)
                    group_title.click()
            except NoElement:
                target = '"' + target + '"'
                # find and click the target to be messaged
                x_arg = '//span[contains(@title,' + target + ')]'
                group_title = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))
                time.sleep(0.2)
                group_title.click()

            # find and click the chatbox and type the message
            x_arg_chatbox = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/' \
                            'div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
            group_title_chatbox = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg_chatbox)))
            time.sleep(0.15)
            group_title_chatbox.click()
            group_title_chatbox.send_keys(message)
            time.sleep(0.1)

            # find and click the send button to send the message
            button_xarg = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/' \
                          'span[2]/div/div[2]/div[2]/button'
            sendbutton = wait.until(EC.element_to_be_clickable((By.XPATH, button_xarg)))
            time.sleep(0.15)
            sendbutton.click()
            return
        except (NotVisible, NotSelectable, NotInteractable, NoElement, StaleElement) as error:
            print("Message Could Not Be Sent, Error Code: 101")
            print(error)
            return


def msg_retriever_all(driver, target_noquotes):
    wait = WebDriverWait(driver, 600)  # time.sleep()

    try:
        target_int = int(target_noquotes)  # will throw ValueError if Contact Name was entered
        search_arg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]'
        search_number = wait.until(EC.element_to_be_clickable((By.XPATH, search_arg)))
        search_number.click()
        search_number.send_keys(target_int)
        time.sleep(4)
        search_results_xarg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div'
        clear_results_xarg = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/span/button'
        driver.find_element_by_xpath(search_results_xarg + '/div').click()  # click the search result
        clear_results = wait.until(EC.element_to_be_clickable((By.XPATH, clear_results_xarg)))
        clear_results.click()  # clear the search results

        # this part is same for both contact and number
        # access the chatbox element
        x_arg_chat = '/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]'
        chatbox = driver.find_elements_by_xpath(x_arg_chat + '/div')
        print(f'length of chatbox is: {len(chatbox)}')

        chatbox.reverse()  # reverse so the messages are in chronological order
        txt_file = open(f'chat_log_{target_noquotes}.txt', 'w+', encoding='utf-16')
        for i in range(len(chatbox) + 1):
            try:
                x_arg_msg = f'/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div[{i}]' \
                            f'/div/div/div/div[1]/div/span[1]/span'
                x_arg_timestamp = f'/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div[{i}]' \
                                  f'/div/div/div/div[1]'
                timestamp = driver.find_element_by_xpath(x_arg_timestamp).get_attribute("data-pre-plain-text")
                message = driver.find_element_by_xpath(x_arg_msg).text
                txt_file.write(f'{timestamp} {message}\n')
            except NoElement:
                pass
        txt_file.close()
        return

    except NoElement:
        print("Coult not find phone number in chat, please make sure the number you have entered is correct.")
        return

    except ValueError:
        try:
            target = '"' + target_noquotes + '"'
            # open the chat screen
            x_arg = '//span[contains(@title,' + target + ')]'
            group_title = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))
            time.sleep(0.2)
            group_title.click()
            time.sleep(1)

            # access the chatbox element
            x_arg_chat = '/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]'
            chatbox = driver.find_elements_by_xpath(x_arg_chat + '/div')
            print(f'length of chatbox is: {len(chatbox)}')

            chatbox.reverse()   # reverse so the messages are in chronological order
            txt_file = open(f'chat_log_{target_noquotes}.txt', 'w+', encoding='utf-16')
            for i in range(len(chatbox)+1):
                try:
                    x_arg_msg = f'/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div[{i}]' \
                                f'/div/div/div/div[1]/div/span[1]/span'
                    x_arg_timestamp = f'/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div[{i}]' \
                                      f'/div/div/div/div[1]'
                    timestamp = driver.find_element_by_xpath(x_arg_timestamp).get_attribute("data-pre-plain-text")
                    message = driver.find_element_by_xpath(x_arg_msg).text
                    txt_file.write(f'{timestamp} {message}\n')
                except NoElement:
                    pass
            txt_file.close()
            return
        except (NotVisible, NotSelectable, NotInteractable):
            print("Failed to retrieve messages, Error Code: 102")
            return


# DELETE OR COMMENT AFTER HERE IF YOU WISH TO IMPORT THE ENTIRE FILE WITHOUT RUNNING THE SCRIPT

drv = initializer()
input_msg = ""
input_msg2 = ""
while input_msg2 != 'exit':
    print("Enter one of the commands below to proceed: \n"
          "    - 'send' to send a message, \n"
          "    - 'chat' to view conversation logs with a contact, \n"
          "    - 'exit' to exit the program. \n")
    input_msg = input('> ')
    if input_msg == "send":
        kisi = input('Enter contact name (preferred) or phone number of the receiver: ')
        print(f'Enter the message you wish to send {kisi}: ')
        mesaj = input('> ')
        msg_sender(drv, kisi, mesaj)
        input_msg = ""
    elif input_msg == "chat":
        kisi = input('Enter contact name (preferred) or phone number to view conversation logs: ')
        msg_retriever_all(drv, kisi)
        input_msg = ""
    elif input_msg == "exit":
        print("Terminating Program.")
        exiter = 1
        time.sleep(2)
        drv.close()
        input_msg2 = input_msg
        break
    else:
        print('\nPlease enter one of the specified commands.\n')
        input_msg = ""
        input_msg2 = ""
        continue
