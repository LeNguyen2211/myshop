from flask import request, render_template, redirect, url_for

from ShopApp import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

