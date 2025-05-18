from requests import get,post, delete, ConnectionError

linkForTest = 'http://jsonplaceholder.typicode.com/posts'

def testGetReq():
      try: getResp = get(linkForTest)
      except ConnectionError: print('errorConnection')
      except Exception as err: print('error', err)
      finally: print(getResp.json)
      # assert getResp.status_code == (200 | 201)

def testPostReq():
      try: postResp = post(linkForTest)
      except ConnectionError: print('errorConnection')
      except Exception as err: print('error', err)
      finally: print(postResp.text)
      #assert postResp.status_code == (200 | 201)


def testDeleteReq():
      try: deleteResp = delete(f'{linkForTest}/1')
      except ConnectionError: print('errorConnection')
      except Exception as err: print('error', err)
      finally: print(deleteResp.text)
      #assert deleteResp.status_code == (200 | 201)
