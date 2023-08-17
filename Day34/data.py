from typing import List
import requests

BASE_URL = "https://opentdb.com/api.php"
parameters = {"amount": 10, "type": "boolean"}

def retrieve_quiz_questions() -> List[str]:
    try:
        response = requests.get(url=BASE_URL, params=parameters).json()
        if response["response_code"] != 0:
            raise Exception("Something went wrong")
        return response.get("results", [])
    except Exception as e:
        print(e)

question_data = retrieve_quiz_questions()