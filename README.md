# xionic

## 상업적 이용이 가능한 라이센스의 한국어 모델 


질문 :
 
```
각국의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 
하지만 정의란 명확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 
그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라
```

test python openai 

```
from openai import OpenAI

client = OpenAI(
    base_url = "http://sionic.tech:28000/v1/",
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

```

test curl

```
curl --location 'http://sionic.tech:28000/v1/chat/completions' --header 'Content-Type: application/json' --header 'X-SIONIC-API-KEY: 934c4bbc-c384-4bea-af82-1450d7f8128d' --data '{"model": "xionic-1-72b-20240610","messages": [{"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."}, {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라.\\nAnswer:"}]}'
```

예시결과

```

{"id":"cmpl-701fd3382b924bfe99b4161506030f8e","object":"chat.completion","created":1717954469,"model":"xionic-1-72b-20240610","choices":

[{"index":0,"message":{"role":"assistant","content":"
사회 구성원의 대다수가 납득할 수 있는 보편적인 '정의'의 개념을 입증하는 것은 쉽지 않은 과제입니다. 
그러나, 그럼에도 불구하고, 우리는 철학, 법률, 사회학, 심리학, 윤리학 등 다양한 학문 분야를 통해 공통의 원칙과 
가치를 찾고 이를 통해 '정의'를 정의하려는 시도를 해볼 수 있습니다.\n\n

첫째, '정의'의 개념은 '평등'과 '공정'이라는 가치에 기반을 두고 있습니다. 모든 사람, 무론 성별, 인종, 국가, 종교, 성적 지향 등에 관계없이 동등한 권리를 가지는 것이 바로 '평등'의 개념입니다. 
한편, '공정'의 개념은 이 '평등'의 원칙이 실제로 작동하도록 하기 위한 것입니다. 즉, 모든 사람이 동등하게 권리를 누리도록 구조를 공정하게 유지하는 것이 '공정'이라고 할 수 있습니다. \n\n

둘째, '정의'는 '자유'와 '책임'이라는 원칙에 근거합니다. 모든 개인은 자신의 행동에 대한 자유를 가지고 있어야 하며, 그 자유는 다른 사람들의 자유와 충돌하지 않아야 합니다. 
한편, 이 자유는 책임을 수반합니다. 즉, 자유롭게 행동한 결과에 대한 책임을 개인이 지는 것입니다.\n\n

셋째로, '정의'는 '자비'와 '인도'의 개념을 포함합니다. 이는 '정의'가 단지 규칙과 법률에만 의존하지 않고, 인간의 가치와 존엄성을 존중하는 것을 의미합니다. \n\n

마지막으로, '정의'는 사회적 합의의 결과로서 이해될 수 있습니다. 이는 법률과 사회규범이 사회 구성원들의 동의와 합의를 통해 만들어지며, 이들 규범에 대한 준수는 사회 구성원 
모두에게 '정의'로 인식되어야 합니다. \n\n따라서, '정의'는 '평등', '공정', '자유', '책임', '자비', '인도' 등과 같은 가치와 원칙들을 통해 입증될 수 있습니다. 

그러나 이는 사회 구성원 모두가 동의하고 인식하는 폭넓은 합의 과정에 필수적이라는 점을 잊지 말아야 합니다. '정의'는 법과 법률, 또는 도덕과 윤리의 영역에만 한정되지 않고, 
이에 대한 우리의 이해와 인식이 사회 구성원 모두에게 공감되는 가치로 체화되어야 합니다."},

"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":136,"total_tokens":726,"completion_tokens":590}}

```

https://lk.instruct.kr/
