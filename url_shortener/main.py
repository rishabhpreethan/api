import requests

def shorten_link(full_link,link_name):
    base_url="https://cutt.ly/api/api.php"
    api="51de7be2f870ac3d5b7159aaf2707a28e3bf3"
    p = {'key':api,"short":full_link,"name":link_name}
    response=requests.get(base_url,params=p).json()
    # print(response)
    return response['url']['shortLink']

full_link=input("Enter a link that you want to shorten\n")
link_name=input("Enter the name\n")

# shorten_link("https://gogoanime.co.in/","gogo")
# gave an exist status of 3
# which means that the link was already taken

print(shorten_link(full_link,link_name))