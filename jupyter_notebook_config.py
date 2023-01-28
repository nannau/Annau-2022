from notebook.auth import passwd

my_password = "annau2023"
hashed_password = passwd(passphrase=my_password, algorithm='sha256')

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_password_change = True

c.NotebookApp.password = hashed_password
c.NotebookApp.open_browser = False

c.NotebookApp.port = 8888