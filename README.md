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
    base_url = "http://sionic.chat/v1",
    api_key = "934c4bbc-c384-4bea-af82-1450d7f8128d"
)

response = client.chat.completions.create(
    model="xionic-1-72b-20240404",
    messages=[
        {"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."},
        {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명>확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라."}
    ]
)

print (response)

```

<img width="822" alt="image" src="https://github.com/sionic-ai/xionic/assets/69115576/64f53803-750a-4fc1-8772-186e704c92fd">



test curl

```
curl --location 'http://sionic.chat/v1/chat/completions' --header 'Content-Type: application/json' --header 'X-SIONIC-API-KEY: 934c4bbc-c384-4bea-af82-1450d7f8128d' --data '{"model": "xionic-1-72b-20240404","messages": [{"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."}, {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라.\\nAnswer:"}]}'
```

예시결과

```
{"id":"cmpl-48a28de442714cc69f47013d15fbe75f","object":"chat.completion",
"created":1712684425,"model":"xionic-1-72b-20240404",
"choices":[{"index":0,"message":{"role":"assistant","content":"정의라는 개념은 각 국가와 문화마다 다양한 해석과 이해가 있지만, 
사회 구성원의 대부분이 납득할 수 있는 보편적 정의를 구축하기 위해서는 몇 가지 접근 방식이 있을 수 있습니다. 이를 위해서는 다음과 같은 요소들을 
고려해야 합니다.\n\n1. 공정성과 형평성: 공정한 법과 제도를 통해 모든 구성원에게 동등한 기회와 대우를 보장하는 것이 중요한 작업입니다. 정의는 
개인의 신념과 지위에 상관없이 법과 규칙이 공정하게 적용되는 것을 의미합니다.\n\n2. 공공의 이익: 보편적 정의는 사회 전체의 이익을 고려하는 것으로, 
개인의 이익과 상충되는 경우에도 공공의 이익을 최우선으로 정의를 적용해야 합니다.\n\n3. 인간의 기본권 보장: 모든 인간이 존엄성과 기본권을 소유한다는 
사실을 인정하는 것은 중요합니다. 법과 제도는 이러한 기본권을 침해하지 않도록 설계되어야 하며, 인간의 자유와 안전을 보호하는 것이 정의의 일부입니다.\n\n
4. 역사와 문화의 고려: 사회의 역사와 문화적 배경을 고려하여 정의를 정의하는 것도 중요합니다. 이는 각 지역의 특수성을 인정하고, 이를 바탕으로 공통된 
가치와 원칙을 찾는 과정을 의미합니다.\n\n5. 논리적 일관성: 정의는 논리적으로 일관된 것으로 해석되어야 합니다. 법칙과 규칙이 상호 모순하지 않아야 하며, 
그것이 사회 구성원의 일반적인 인식과 일치해야 합니다.\n\n6. 대화와 참여: 사회 구성원들과의 대화와 의견 수렴은 보편적 정의를 구축하는 데 중요한 역할을 합니다. 
민주적 절차를 통해 다양한 시각을 고려하고, 대중의 의견을 반영하여 정의의 정의를 조정하고 발전시킬 수 있습니다.\n\n7. 교육과 인식 제고: 정의의 개념을 교육과 
정보 제공을 통해 사회 전반에 알리는 것이 중요합니다. 이를 통해 사람들이 정의에 대한 이해를 높이고, 공감대를 형성할 수 있습니다.\n\n이러한 요소들을 기반으로, 
사회 구성원들이 공통적으로 받아들일 수 있는 정의를 구축하는 것은 장기적인 프로세스입니다. 그러나 이러한 노력들을 통해, 각국의 법률과 사회적 체제가 보다 공정하고 
인간다움을 존중하는 방향으로 발전하는 것이 가능할 것입니다."},
"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":136,"total_tokens":728,"completion_tokens":592}}
```

https://lk.instruct.kr/
