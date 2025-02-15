import requests
import allure
from config_all import config_app

def attach_bstack_video(session_id):

    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config_app.USER_NAME, config_app.ACCESS_KEY),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']
    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )