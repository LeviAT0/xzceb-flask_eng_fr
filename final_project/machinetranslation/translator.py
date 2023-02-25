"""
To create en-fr  translator import dependencies and load os environment 
"""
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
minimum_version = ssl.PROTOCOL_TLSv1_2
maximum_version = ssl.PROTOCOL_TLSv1_2
TLSVersion = ssl.PROTOCOL_TLSv1_2

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv 
"""
Reference the language translator's apikey and url
"""

load_dotenv()
APIKEY = os.environ['api_key']
URL = os.environ['url']

"""
 setup Language translator service 
"""


VERSION = '2018-05-01'  # service setup and authentication
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=authenticator)
language_translator.set_service_url(URL)


languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    """
    This function returns french translation
    """
    if english_text is None:
        return None
    translation_response = language_translator.translate(
        text=english_text, model_id='en-fr')
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    This function returns english translation
    """
    if french_text is None:
        return None
    translation_new = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = translation_new['translations'][0]['translation']
    return english_text