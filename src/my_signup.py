import base64
import fcntl
import json
import os
import random
import re
import secrets
import string
import time
import traceback
import uuid

import requests
from func_timeout import func_timeout, FunctionTimedOut
from loguru import logger
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import cloudflare_solver
from config import config
import utils
from globals import GlobalState


class Interrupted(Exception):
    pass

class mySign:
    def __init__(self):
        self.driver = utils.get_webdriver()
    def sign_up(self):
        try:
            func_timeout(5 * 60, self._sign_up)
        except Interrupted as e:
            logger.error("error in signup: {}".format(e))
            raise e
        except FunctionTimedOut as e:
            logger.warning("signup timeout")
            pass
        except Exception as e:
            traceback.print_exc()
        finally:
            self.driver.quit()
    
    def _sign_up(self):
        cloudflare_solver.bypass('https://chat.oaifree.com/auth/signup', self.driver)
        email_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email = self._get_email()
        email_input.send_keys(email)
        #print( self.driver.page_source)

        # todo check email
        #submit_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        #submit_btn.click()

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        password = self._get_password()
        password_input.send_keys(password)
        logger.info(f'${email}----${password}')
        submit_btn = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_btn.click()

        time.sleep(5)
        exit(0)
    
    def _get_email(self):
        
        return ''.join(
            [secrets.choice(string.ascii_letters + string.digits) for _ in range(15)]) + "@" + config['domain']

    def _get_password(self):
        return ''.join(
            [secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(15)])

    