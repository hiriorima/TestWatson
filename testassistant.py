# -*- coding: utf-8 -*-
from __future__ import print_function
import json
from watson_developer_cloud import AssistantV1

# If service instance provides API key authentication
# assistant = AssistantV2(
#     version='2018-09-20',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/assistant/api',
#     iam_apikey='iam_apikey')

assistant = AssistantV1(   
        username='username',
        password='password',
        ## url is optional, and defaults to the URL below. Use the correct URL for your region.
        url='https://gateway.watsonplatform.net/assistant/api',
        version='2018-09-20')


response = assistant.message(
        workspace_id='workspace_id',
        input={
            'text': 'hogehoge'
            }    
        ).get_result()
response = json.dumps(response["output"]["text"][0], ensure_ascii=False, indent=2)
print(response)
