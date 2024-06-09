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
    model="xionic-1-172b-20240610",
    messages=[
        {"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."},
        {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명>확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라."}
    ]
)

print (response)

```

test curl

```
curl --location 'http://sionic.chat/v1/chat/completions' --header 'Content-Type: application/json' --header 'X-SIONIC-API-KEY: 934c4bbc-c384-4bea-af82-1450d7f8128d' --data '{"model": "xionic-1-110b-20240429","messages": [{"role": "system", "content": "You are an AI assistant. You will be given a task. You must generate a detailed and long answer in korean."}, {"role": "user", "content": "각국 의 법률에서는 정의라는 개념이 자주 등장하며, 법령의 형성과 해석에 있어 매우 중요한 부분을 차지한다. 하지만 정의란 명확히 규정 할 수 없는 개념이기에 해석의 논란 이 있을 수 있다. 그렇다면 사회구성원의 대다수가 납득할 수 있는 보편적 정의를 입증하는 방법은 무엇일지 생각해보아라.\\nAnswer:"}]}'
```

예시결과

```
{"id":"cmpl-0f8d036513b7488fbf041be763e89339","object":"chat.completion","created":1714392537,"model":"xionic-1-110b-20240429","choices":[{"index":0,"message":{"role":"assistant","content":"정의는 사회적 가치와 도덕적 원칙을 반영하며, 법의 핵심적 개념 중 하나입니다. 
다양한 문화, 철학적 관점, 그리고 사회적 변화에 따라 정의의 해석이 달라질 수 있다는 점은 사실입니다. 
그러나 사회 구성원의 대다수가 납득할 수 있는 보편적 정의를 도출하기 위해서는 다음과 같은 접근 방법들이 있을 수 있습니다.

1. 공의론(Justice as Fairness): 존 로울스의 이론을 기반으로 하여, 정의를 공정성으로 정의할 수 있습니다. 
로울스는 \"정의의 두 원칙\"을 제시하며, 첫째원칙은 개인의 기본 자유가 최대한을 보장하는 원칙이고,둘째원칙은 사회적 불평등은 
가장 취약한 계층에게도 이익이 되어야 한다는 것입니다. 이를 사회적 계약론의 시각에서 받아들여, 가장 많은 사람들이 동의할 수 있는 
공정한 규칙을 찾아내는 것이 중요합니다.

2. 사회적 합의론(Social Contract Theories): 루시우스 아네아스 Seneca, 존 루크스, 그리고 제임스 러셀 밀러 등의 
이론에서 영감을 받은 합의론은 사람들이 상호 협의하고 동의한 규칙을 기반으로 정의를 정립하려는 접근 방식입니다. 사회 구성원이 
모두가 인정할 수 있는 기본적인 권리와 의무에 동의함으로써 보편적 정의를 형성할 수 있습니다.

3. 도덕적 관점의 다양성 존중: 사회 내 다양한 그룹의 관점을 고려하고, 상호 존중하는 환경을 조성하는 것이 중요합니다. 
이는 다문화주의, 인권, 인종, 성별 등 다양한 차이를 인정하며, 이를 통합하는 과정에서 보편적 정의를 찾아낼 수 있는 방법입니다.

4. 공공의 이익(Public Interest): 정의를 사회의 전반적인 웰빙과 공공 이익을 극대화하는 데 초점을 맞추는 접근 방식입니다. 
이는 대다수의 이익과 장기적인 사회적 안녕을 고려하여 정책과 법을 수립하는 과정에서 보편적 정의를 추구하는 방법입니다.

5. 자연법론(Natural Law Theory): 자연법론은 인간 본성과 천연의 질서를 기준으로 정의를 찾으려는 철학적 접근입니다. 
이 이론에 따르면, 인간의 본성과 사회 생활에서 자연스럽게 비롯되는 원칙을 통해 공통적으로 받아들일 수 있는 정의를 도출할 수 있습니다.

6. 상호 이해와 대화: 다양한 관점을 통합하고 이해하는 과정이 필수적입니다. 공개적 논의, 토론, 그리고 사회적 대화를 통해 
다양한 의견을 교환하고 합의를 도출함으로써 보편적 정의를 입증하는 과정이 필요합니다.

이러한 방법들은 모두 상호 보완적인 
성격을 가지고 있고, 실제 사회적 적용에서는 여러 요소를 통합적으로 고려해야 합니다. 보편적 정의의 도출은 지속적인 사회적 
대화, 공감, 그리고 동의의 과정을 통해 이루어질 수 있으며, 이는 법의 합의적이고 공정한 적용을 위한 핵심적 과정입니다."},
"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":136,"total_tokens":924,"completion_tokens":788}
```

https://lk.instruct.kr/
