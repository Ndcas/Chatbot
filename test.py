import math

import requests

import re


def generateWord():
    templates = [
        "- Cho tôi thông tin về từ [{}](given_word)",
        "- Bạn có thể dịch từ [{}](given_word) không?",
        "- Làm ơn cho tôi biết nghĩa của từ [{}](given_word)",
        "- Bạn có thể giải thích từ [{}](given_word) không?",
        "- Dịch từ [{}](given_word) sang tiếng Việt giúp tôi",
        "- Bạn có thể cung cấp cho tôi định nghĩa của từ [{}](given_word) không?",
        "- Xin vui lòng cho tôi biết cách sử dụng từ [{}](given_word)",
        "- Bạn có thể dịch từ [{}](given_word) không?",
        "- Làm ơn giải thích từ [{}](given_word) cho tôi",
        "- Bạn có thể cung cấp thông tin về từ [{}](given_word) trong tiếng Anh không?",
        "- Cho tôi biết cách hiểu từ [{}](given_word)",
        "- Làm ơn giải thích nghĩa của từ [{}](given_word)",
        "- Bạn có thể cho tôi thông tin về các định nghĩa của từ [{}](given_word) không?",
        "- Dịch từ [{}](given_word) trong giúp tôi",
        "- Bạn có thể cho tôi biết cách dùng từ [{}](given_word) không?",
        "- Làm ơn cho tôi biết các nghĩa của từ [{}](given_word)",
        "- Bạn có thể giải thích rõ hơn về từ [{}](given_word) không?",
        "- Xin vui lòng dịch từ [{}](given_word)",
        "- Bạn có thể cung cấp cho tôi thông tin về từ [{}](given_word) trong từ điển không?",
        "- Cho tôi một ví dụ về cách dùng từ [{}](given_word)",
        "- Bạn có thể dịch từ [{}](given_word) từ tiếng Anh sang tiếng Việt không?",
        "- Làm ơn cung cấp bản dịch của từ [{}](given_word)",
        "- Cho tôi biết tất cả các nghĩa của từ [{}](given_word)",
        "- Bạn có thể cho tôi thấy cách sử dụng từ [{}](given_word) không?",
        "- Dịch giúp tôi từ [{}](given_word)",
        "- Bạn có thể giải thích rõ ràng về từ [{}](given_word) không?",
        "- Xin vui lòng cung cấp định nghĩa của từ [{}](given_word)",
        "- Bạn có thể cho tôi thông tin chi tiết về từ [{}](given_word) không?",
        "- Dịch từ [{}](given_word) sang tiếng Việt giúp tôi",
        "- Bạn có thể làm rõ nghĩa của từ [{}](given_word) không?"
    ]
    response = requests.get("https://randomwordgenerator.com/json/words_ws.json")
    if (response.status_code != 200):
        return
    response = response.json()["data"]
    for r in range(900):
        print(templates[math.floor(r / 30)].format(response[r % len(response)]["word"]["value"]))


def generateSentence():
    templates = [
        '- Câu "{}" dịch sang tiếng Việt là gì?',
        '- Bạn có thể dịch câu "{}" không?',
        '- "{}" nghĩa là gì trong tiếng Việt?',
        '- Câu "{}" có nghĩa là gì?',
        '- "{}" được dịch thế nào?',
        '- Câu "{}" trong tiếng Anh có thể dịch ra sao?',
        '- "{}" có thể dịch là gì?',
        '- Dịch câu "{}" ra tiếng Việt giúp tôi',
        '- Bạn có thể cho tôi biết "{}" có nghĩa gì không?',
        '- Câu "{}" có thể được hiểu như thế nào?',
        '- Bạn có thể giúp tôi hiểu câu "{}" không?',
        '- Dịch câu "{}" ra tiếng Việt sao cho chính xác?',
        '- Bạn có thể giải thích câu "{}" cho tôi không?',
        '- Dịch câu "{}"',
        '- Câu "{}" dịch sang tiếng Việt như thế nào?',
        '- Câu "{}" có nghĩa là gì trong tiếng Việt?',
        '- Bạn có thể giúp tôi dịch câu "{}" không?',
        '- Dịch câu "{}" sang tiếng Việt giúp tôi.',
        '- Bạn có thể cho tôi biết câu "{}" dịch ra sao không?',
        '- Dịch câu "{}" từ tiếng Anh sang tiếng Việt như thế nào?',
        '- Bạn có thể giải thích câu "{}" bằng tiếng Việt không?',
        '- Dịch câu "{}" giúp tôi với.',
        '- "{}" có thể dịch sang tiếng Việt như thế nào?',
        '- Bạn có thể nói câu "{}" bằng tiếng Việt không?',
        '- Giải thích câu "{}" bằng tiếng Việt giúp tôi',
        '- Dịch câu "{}" sang tiếng Việt đi',
        '- Bạn có thể cho tôi biết cách dịch câu "{}" không?',
        '- Làm ơn dịch câu "{}" sang tiếng Việt.',
        '- Câu "{}" có thể dịch sang tiếng Việt như thế nào?',
        '- Bạn có thể cho tôi một bản dịch của câu "{}" không?'
    ]
    response = requests.get("https://randomwordgenerator.com/json/sentences.json")
    if (response.status_code != 200):
        return
    response = response.json()["data"]
    for r in range(900):
        print(templates[math.floor(r / 30)].format(response[r % len(response)]["sentence"]))

text = 'Đây là một ví dụ: .'

# Sử dụng regex để tìm tất cả các phần giữa dấu ngoặc kép
matches = re.findall(r'"(.*?)"', text)
print(matches)
# In kết quả
for match in matches:
    print(match)
