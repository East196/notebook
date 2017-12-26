from fabric.api import local,lcd


def build():
	local("jupyter nbconvert docs/**/*.ipynb --to markdown")
    local("copy README.md docs\index.md")
    local("mkdocs build")
    with lcd("..\East196.github.io"):
        local("rd /s /q notebook")
    local("xcopy site ..\East196.github.io\\notebook\ /s /e")


def serve():
    local("mkdocs serve")
