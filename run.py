import argparse

from app import create_app

# Create the flask app.
app = create_app()

# Run the app
if __name__ == '__main__':

    app.run()
