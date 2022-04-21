from HW_019_gunicorn.main.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
