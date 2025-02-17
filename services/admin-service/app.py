from . import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# from . import app  # __init__.py에서 만든 app을 가져옴
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
