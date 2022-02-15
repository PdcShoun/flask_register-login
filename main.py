from website import create_app
# import create_app from __init__.py

# python3 main.py to run server

app = create_app()

if __name__ == '__main__':
    
    # run flask application
    app.run(debug=True) 