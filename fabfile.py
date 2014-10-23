from fabric.colors import green, cyan, yellow
from fabric.context_managers import hide, cd, prefix, settings
from fabric.contrib.files import upload_template
from fabric.decorators import task
from fabric.operations import local, run, sudo
from fabric.api import env

env.hosts = ['54.191.105.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/blog_analytics.pem'
env.shell = "/bin/bash -l -i -c"


def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")


templates = {
    "nginx": {
        "local_path": "deploy/nginx.conf",
        "remote_path": "/etc/nginx/sites-enabled/%(proj_name)s.conf",
        "reload_command": "service nginx restart",
    },
    "supervisor": {
        "local_path": "deploy/supervisor.conf",
        "remote_path": "/etc/supervisor/conf.d/%(proj_name)s.conf",
        "reload_command": "supervisorctl reload",
    },
    "gunicorn": {
        "local_path": "deploy/gunicorn.conf.py.template",
        "remote_path": "%(proj_path)s/gunicorn.conf.py",
    },
    "settings": {
        "local_path": "deploy/local_settings.py.template",
        "remote_path": "%(proj_path)s/local_settings.py",
    },
}


@task
def hello():
    print(cyan("I'm ALIVE!!!"))


@task
def create_file(file_name):
    local("touch ~/Desktop/{}.txt".format(file_name))
    print (green("File {} Created").format(file_name))


@task
def create_directory(dir_name):
    local("mkdir ~/Desktop/{}".format(dir_name))
    print (green("Success! Directory {} Created".format(dir_name)))


@task
def new_directory(dir_name, path):
    local("mkdir {}/{}".format(path, dir_name))
    local("cd {}/{}".format(path, dir_name))
    print (green("Success! Current Directory: {}/{}".format(path, dir_name)))


@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))


@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            run("python manage.py migrate")
            run("python manage.py collectstatic --noinput")
    restart_app()


@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))


@task
def setup_nginx(project_name, server_name):
    upload_template(
        "./deploy/nginx.conf",
        "/etc/nginx/sites-enabled/{}.conf".format(project_name),
        {'server_name': server_name},
        use_sudo=True,
        backup=False
    )
    restart_app()


@task
def setup_supervisor(project_name, virtualenv_name):
    upload_template(
        "./deploy/supervisor.conf",
        "/etc/supervisor/conf.d/{}.conf".format(project_name),
        {'virtualenv_name': virtualenv_name, 'project_name': project_name},
        use_sudo=True,
        backup=False
    )
    restart_app()


@task
def setup_gunicorn(project_name, workers):
    upload_template(
        "./deploy/gunicorn.conf.py",
        "/gunicorn.conf.py",
        {'project_name': project_name, 'workers': int(workers)},
        use_sudo=True,
        backup=False
    )
    restart_app()
