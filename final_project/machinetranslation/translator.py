''' This module has functions to translate from english to
french and from french to english '''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text = None):
    ''' This function takes english text as input
    and returns french text'''
    #write the code here
    if english_text is None:
        return "You must enter some english text..."

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text = None):
    ''' This function takes french text as input
    and returns english text'''
    #write the code here
    if french_text is None:
        return "You must enter some french text..."

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
