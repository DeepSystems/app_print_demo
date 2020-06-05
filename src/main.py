import os
import supervisely_lib as sly

SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))
my_app = sly.AppService(sly.logger)


@my_app.callback("generate")
@sly.timeit
def generate_random_string(api: sly.Api, task_id, context, state):
    new_str = sly.rand_str(10)
    api.app.set_vars(task_id, "data.randomString", new_str)


def main():
    with open(os.path.join(SOURCE_DIR, 'gui.html'), 'r') as file:
        template = file.read()

    # data
    data = {
        "randomString": "initial random value xxx"
    }

    # state
    state = {
    }

    my_app.run(template, data, state)


if __name__ == "__main__":
    main()

#@TODO: config.json
# python -m pip install git+https://github.com/supervisely/supervisely
# python setup.py develop
# корневой уровень переменных (занести все в data)
# уменьшить количество строчек
#@route- > @callback (rename)
# data.set(‘randomString’, sly.rand_str(10))
# data.set({“a”: 111, “b”: 222})
# api.task.state.set()
# context + state по всем юзерам? + там будет labelerLogin, api_token, и тд