#!/usr/bin/env python
from teams.wsgi_admin import admin

if __name__ == "__main__":
    admin.run(
        host='0.0.0.0',
        port=9002,
        processes=1,
    )
