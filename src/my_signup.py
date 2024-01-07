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
        logger.warning("signup hello")
        

    