import  requests,json
def get_QA_answer_test(getanswer_url,body):
    headers={
        'Content-Type':'application/json',
        'Authorization':'f546cb89-0587-48a5-bbf8-8a187b60682b'
    }
    url=getanswer_url
    response=requests.request('POST',url,data=body,headers=headers)
    response_text=json.loads(response.text)
    print(response_text)
    print(response_text['answers'][0]['answer'])
    '''
POST /knowledgebases/b2f91f3d-5c7f-4efc-a927-4820a3fb0b35/generateAnswer
Host: https://ghj1.azurewebsites.net/qnamaker
Authorization: EndpointKey f546cb89-0587-48a5-bbf8-8a187b60682b
Content-Type: application/json
{"question":"<Your question>"}
    '''
getanswer_url='https://ghj1.azurewebsites.net/qnamaker/knowledgebases/b2f91f3d-5c7f-4efc-a927-4820a3fb0b35/generateAnswer'
question_sentence={
    'question':'會員'
}
question_sentence_json=json.dumps((question_sentence))
get_QA_answer_test(getanswer_url,question_sentence_json)
