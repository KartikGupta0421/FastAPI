from app.main import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
