from os.path import basename, exists


def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename


def download_all_prerequisites():
    download('https://github.com/AllenDowney/ThinkPython/raw/v3/thinkpython.py')
    download('https://github.com/AllenDowney/ThinkPython/raw/v3/diagram.py')
    download('https://github.com/ramalho/jupyturtle/releases/download/2024-03/jupyturtle.py')
    download('https://www.gutenberg.org/cache/epub/43/pg43.txt');
