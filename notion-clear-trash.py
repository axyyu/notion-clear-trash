from notion.client import NotionClient


def get_trash(client):
    query = {
        'query': '',
        'limit': 1000,
        'spaceId': client.current_space.id
    }
    results = client.post('/api/v3/searchTrashPages', query)
    block_ids = results.json()['results']

    return block_ids


def delete_permanently(client, block_ids):
    total = len(block_ids)
    for i in range(total):
        try:
            client.post("deleteBlocks", {"blockIds": [block_ids[i]], "permanentlyDelete": True})
            print(f"Deleted {str(i+1)} / {str(total)}")
        except:
            print("Failed to delete BLOCK_ID:", block_ids[i])


if __name__== "__main__":
    token = input('Please enter your auth token: ')
    client = NotionClient(token_v2=token)

    block_ids = get_trash(client)
    delete_permanently(client, block_ids)
    
    print('Successfully cleared all trash blocks.')
