import os
import supervisely_lib as sly

SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))


def generate_random_string(api, task_id, request_msg):
    new_str = sly.rand_str(10)
    api.task.set_data(task_id, new_str, "data.randomString")
    print("!! done")


def main():
    with open(os.path.join(SOURCE_DIR, 'gui.html'), 'r') as file:
        gui_template = file.read()

    # data
    data = {
        "randomString": "initial random value"
    }

    # state
    state = {
    }

    payload = {
        sly.app.TEMPLATE: gui_template,
        sly.app.STATE: state,
        sly.app.DATA: data,
    }

    #@TODO: how to send task_id from agent - env variables

    task_id = os.getenv("TASK_ID")
    agent_token = os.getenv("AGENT_TOKEN")
    api = sly.Api.from_env(retry_count=5)

    # http://78.46.75.100:11111/apps/sessions/20
    jresp = api.task.set_data(task_id, payload)

    app_service = sly.app.AppService(sly.logger, task_id, server_address, agent_token, api_token)
    app_service.add_route("generate_random_string", generate_random_string)
    app_service.run()


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

# exec env
# state всегда передается в callback
# context + state по всем юзерам? + там будет labelerLogin, api_token, и тд
# 