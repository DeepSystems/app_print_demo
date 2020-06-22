ARG GIT_LOGIN
ARG GIT_PASSWORD

FROM supervisely/base-py:6

RUN python -m pip install 'git+https://${GIT_LOGIN}:${GIT_PASSWORD}@github.com/DeepSystems/supervisely_py.git@import_alpha_images'