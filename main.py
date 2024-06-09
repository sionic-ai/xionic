from openai import OpenAI

client = OpenAI(
    base_url = "http://sionic.chat/v1",
    api_key = "934c4bbc-c384-4bea-af82-1450d7f8128d"
)

response = client.chat.completions.create(
    model="xionic-1-72b-20240610",
    messages=[
        {"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."},
        {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명>확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라."}
    ]
)

print (response)
