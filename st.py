import requests

import unittest

class TestStringMethods(unittest.TestCase):
    def test_onliner(self):
  	    r = requests.get("https://petstore.swagger.io/v2/store/inventory") 
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()
 
class TestStringMethods(unittest.TestCase):
    def test_swaggwe(self):
  	    r = requests.post('https://petstore.swagger.io/v2/store/inventory/post', json = {'id':'1'})
  	    r = requests.post('https://petstore.swagger.io/v2/store/inventory/post', json = {'petid':'2'})
  	    r = requests.post('https://petstore.swagger.io/v2/store/inventory/post', json = {'shipDate':'2021-09-05T19:38:52.268'})
  	    r = requests.post('https://petstore.swagger.io/v2/store/inventory/post', json = {'status':'placed'})
  	    r = requests.post('https://petstore.swagger.io/v2/store/inventory/post', json = {'complete': true})
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_onliner(self):
  	    r = requests.get("https://petstore.swagger.io/v2/store/order/1") 
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_swaggwe(self):
  	    r = requests.put('https://petstore.swagger.io/v2/store/inventory/put', json = {'id':'123'})
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_onliner(self):
  	    r = requests.get("https://petstore.swagger.io/v2/store/order/123") 
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_swaggwe(self):
  	    r = requests.delete('https://petstore.swagger.io/v2/store/inventory/delete', json = {'id':'123'})
  	    assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_onliner(self):
  	    r = requests.get("https://petstore.swagger.io/v2/store/order/123") 
  	    assert r.status_code == 404
if __name__ == '__main__':
    unittest.main()
