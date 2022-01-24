from pathlib import Path
class Site(object):
    """docstring for Site."""

    def __init__(self, source,dest):
        source.Path()
        self.source = source
        dest.Path()
        self.dest =dest

    def create_dir(self,path):
        directory = "C:/Users/melli/Desktop/Python/pluralsight-projects-python-static-site-generator-5215412/ssg/site.py"
        path.directory/relative_to(self.dest)
        path.directory/relative_to(self.source)
        directory.mkdir(parents=True,exist_ok=True)

    def build() :
        self.dest.mkdir()
        mkdir(parents=True,exist_ok=True)
