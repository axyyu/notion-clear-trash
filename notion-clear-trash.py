from notion.client import NotionClient


def get_trash(client):
    query = {
        'query': '',
        'limit': 1000,
        'spaceId': client.current_space.id
    }
    results = client.post('searchTrashPages', query)
    block_ids = results.json()['results']

    return block_ids


def delete_permanently(client, block_ids):
    for block_id in block_ids:
        client.post("deleteBlocks", {"blockIds": [block_id], "permanentlyDelete": True})


if __name__== "__main__":
    token = input('Please enter your auth token: ')
    client = NotionClient(token_v2=token)

    block_ids = get_trash(client)
    delete_permanently(client, block_ids)
    
    print('Successfully cleared all trash blocks.')