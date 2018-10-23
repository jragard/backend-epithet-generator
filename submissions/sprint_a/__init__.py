def configure_app():
    import os

    import dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
<<<<<<< HEAD
=======

>>>>>>> 590f2aca4112644ace6203a954dcd293685d8ceb
    app = Flask(__name__)

    return app


app = configure_app()
