from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

def main():
    CONFIG_ENV_VAR = 'ONLYATTECH_SETTINGS'
    has_config = app.config.from_envvar(CONFIG_ENV_VAR, silent=True)

    if not has_config:
        print 'Configuration environment variable (%s) was unset, ' \
            'using default config' % CONFIG_ENV_VAR
        app.config.from_object('default_config')

    app.run()

if __name__ == '__main__':
    main()
