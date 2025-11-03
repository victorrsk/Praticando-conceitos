import requests
import json

url = 'https://jsonplaceholder.typicode.com/'


def get_posts(quantity):
    """
    Retorna multiplos posts
    Args:
        quantity (int): Quantidade de posts a serem retornados
    """
    url_posts = f'{url}posts'
    response = requests.get(url=url_posts)
    posts_data = response.json()

    for i in range(quantity):
        print(f'''ID: {posts_data[i]['id']}\n
        TITLE: {posts_data[i]['title']}\n
        BODY: {posts_data[i]['body']}\n'''
        )


def get_post(post_id):
    """
    Retorna um post
    Args:
        post_id (int): retorna os dados do post com o id especificado
    """
    url_posts = f'{url}posts/{post_id}'
    response = requests.get(url=url_posts)
    post_data = json.dumps(response.json(), indent=4)

    print(post_data)


def post_post():
    """
    Cria um novo post
    Args:
        title (str): titulo do post
        body (str): texto do post
        user_id (int): id do usuario
    """
    title = input('Titulo do post: ')
    body = input('Texto do post: ')
    user_id = int(input('ID do usuario: '))

    url_posts = f'{url}posts'
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(url=url_posts, json=payload)

    print(response.json())
    print(response.status_code, response.reason)


def patch_post_title(post_id):
    """
    Altera o titulo de um post
    Args:
        post_id (int): id do post desejado
    """
    url_posts = f'{url}posts/{post_id}'
    post_title = {"title": input('Novo titulo: ')}
    response = requests.patch(url=url_posts, json=post_title)

    print(response.json())
    print(response.status_code, response.reason)


def delete_post(post_id):
    url_posts = f'{url}posts/{post_id}'
    response = requests.delete(url=url_posts)
    print(response.status_code)


if __name__ == '__main__':
    pass
