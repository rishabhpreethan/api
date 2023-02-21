# https://www.youtube.com/watch?v=c5sWvP9h3s8


import requests

# url="https://api.spotify.com/v1/search?q=Beyonce"
# api="BQDkg0wrtwqWM39u7FZyxFd8SXxgSLhxJztfeGIOdFHji0Iapi_eQu4ACeHzc4MXS_1hQKZPnbxXM0YXInUVkTuvucSbxH4eksJ_vqgpFKgqnyxFGeqNGDetIIuaV-ZJabup9IFvsyrOh_wxZDfoMb3I18Fa8HntebIRoW6wugq1pyRhsmtw_qJfTXoERalg"
# response=requests.get(url).json
# print(response)

url="https://api.spotify.com/v1/users/8c3sgu4skz19vetw8pz7512r0/playlists"
access_token="BQAwBGVkJlsta_aUyOiMRct29RXMQWEil5poW1iIceMvFA2A_4EpJuvege3LOh4L1CdbjfmrPNHHvNM7hcpVxDAbH39tWNKGngKDdlLf80GyM5ThYmixQP0aFkY19XxIFiQSfgV_OOJ-5Oc2t2bfBxCvg2gGSV9h9MwQWXbKopOoJ0L7jjb4jwP5qOCg_XiO65Er5D5AZ5pK-tiaEzK60aofaGXmv_7ZbeANxIsuxabmLnTD6sKNOUP6iNydpg"

def createplaylist(name):
    response=requests.post(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "name":name
        }
    ).json()
    return response
    
def main():
    n=input("Enter name of the playlist\n")
    playlist=createplaylist(n)
    
    print(playlist)

if __name__=='__main__':
    main()