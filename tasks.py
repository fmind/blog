from invoke import task
from pathlib import Path


@task
def venv(c, force=False):
    """Create a virtual environment."""
    if Path("venv").exists() and not force:
        return None
    c.run("python3 -m venv venv --clear")
    c.run("venv/bin/pip install --requirement requirements.txt")


@task(venv)
def work(c):
    """Run an instance of Jupyterlab."""
    c.run('venv/bin/jupyter lab')


@task
def plugs(c):
    """Download some external plugins."""
    c.run('git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb')


@task(venv)
def style(c):
    """Create the code style for the site."""
    c.run('venv/bin/pygmentize -f html -a .highlight -S colorful > theme/fmind/static/styles/pygment.css')


@task(venv)
def serve(c):
    """Serve and auto-regenerate the site."""
    c.run('venv/bin/pelican --verbose --listen --autoreload --relative-urls --output local content')


@task(venv)
def build(c):
    """Generate the remote content of the site."""
    c.run('venv/bin/pelican --verbose --ignore-cache --delete-output-directory --output output content')


@task(build)
def deploy(c):
    """Deploy the content on the remote master branch."""
    c.run('git add output; git commit -m "$(shell date +%s)"; git subtree push --prefix output origin master')
