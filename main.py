from imp import reload
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Fast blog api"
)


@app.get('/')
def root_eendpint():
    return {
        'message': 'Hello World'
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=5000)
