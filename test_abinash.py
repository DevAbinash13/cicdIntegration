import requests
import pytest 

class Testendpointcheck:
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
    "title": "My Test Post",
    "body": "This is a test post created via automation.",
    "userId": 1
    }

    @pytest.mark.smoke
    def test_get_top5(self):
        response = requests.get(url= self.url)
        assert response.status_code == 200
        t = response.json()
        for i in range(5):
            print(t[i]['title'])

    @pytest.mark.smoke
    def test_post_new_data(self):
        response = requests.post(url=self.url, json=self.body)
        resp_json = response.json()
        assert response.status_code == 201
        for i in resp_json:
            if i != 'id':
                assert resp_json[i] == self.body[i]
            
class Testnesteddiffcheck:
    url = "https://jsonplaceholder.typicode.com/users"

    @pytest.mark.smoke
    def test_get_fetch_customers(self):
        response = requests.get(url = self.url)
        val = response.json()
        assert response.status_code == 200
        for i in range(len(val)):
            print(val[i]['name'])
            assert "@" and "." in val[0]['email']
            assert len(val[i]['address']['city']) > 0 and len(val[i]['address']['zipcode']) > 0

        
class TestNegativetestingApi:
    url = "https://jsonplaceholder.typicode.com/posts/invalid"

    def test_verify_error_code(self):
        response = requests.get(url = self.url)
        assert response.status_code == 404