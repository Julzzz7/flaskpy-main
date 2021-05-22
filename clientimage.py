import requests

resp = requests.post("https://implementasijulianak.herokuapp.com/predict",
                     files={"file": open('C://olahcitra//kodok1.jpg','rb')})

print(resp.json())
#print(resp)
