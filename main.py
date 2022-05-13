from fastapi import FastAPI, status, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from typing import Optional

doc_description = """
fast blog api documentation. 🚀
"""


app = FastAPI(title="Fast blog api",
              description=doc_description, version="1.0.1", contact={
                  "name": "Deadpoolio the Amazing",
                  "url": "http://x-force.example.com/contact/",
                  "email": "dp@x-force.example.com",
              })

app.mount('/static', StaticFiles(directory='public'))


@app.get('/')
def root_eendpint():
    return {
        'message': 'Hello World'
    }


articles = [
    {"id": 1, "title": "Post title 1", "published": True},
    {"id": 2, "title": "Post title 2", "published": True},
    {"id": 3, "title": "Post title 3", "published": True},
    {"id": 4, "title": "Post title 4", "published": True},
    {"id": 5, "title": "Post title 5", "published": False},
    {"id": 6, "title": "Post title 6", "published": True},
    {"id": 7, "title": "Post title 7", "published": True},
    {"id": 8, "title": "Post title 8", "published": False},
    {"id": 9, "title": "Post title 9", "published": True},
    {"id": 10, "title": "Post title 10", "published": False},
]


@app.get('/article-list', name="List of all articles", description="List of all articles")
def all_articles(published: bool = True):
    filered = filter(
        lambda article: article['published'] == published, articles)

    return list(filered)
    # return JSONResponse(content=articles, status_code=status.HTTP_200_OK)


@app.get('/get-article/{id}', status_code=status.HTTP_200_OK)
def get_article(id: int):
    filtered_article = filter(lambda article: article['id'] == id, articles)
    filtered_article_list = list(filtered_article)

    if len(filtered_article_list) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")

    return filtered_article_list


class CreateArticlePayload(BaseModel):
    title: str
    body: str
    published: bool


@app.post('/create-article', status_code=status.HTTP_201_CREATED)
def create_article(payload: CreateArticlePayload):
    articles.append({
        'id': len(articles) + 1,
        'title': payload.title,
        "body": payload.body,
    })

    return {
        "message": "Article created",
        "data": articles[-1]
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=5000)
