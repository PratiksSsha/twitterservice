# app/twitter_api/api/deleteTweet.py
import requests


class deleteTweet:
    @staticmethod
    def delete_tweet(bearer_token,tweetId):
        headers = {
            'Authorization': "Bearer".format(bearer_token)
        }
        response = requests.request(method="DELETE", url="https://api.twitter.com/2/users/{}".format(tweetId),
                                    headers=headers)
        if response.status_code == 401:
            return False
	return {"message": "Delete tweet successfully"}        
