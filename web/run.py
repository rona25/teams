#!/usr/bin/env python
from teams.wsgi import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=9001,
        processes=1,
    )
