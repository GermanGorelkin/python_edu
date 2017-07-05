import requests

path = 'https://stepic.org/media/attachments/course67/3.6.3/'
file_name = '699991.txt'

while True:
    r = requests.get(path+file_name)
    result = r.text
    print(result)
    if result[:2] == 'We':
        break
    else:
        file_name = result
open('', 'w').write(result)
