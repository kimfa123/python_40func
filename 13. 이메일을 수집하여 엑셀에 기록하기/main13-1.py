import re

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)

print(results)

#이메일 형식을 추출하는 코드