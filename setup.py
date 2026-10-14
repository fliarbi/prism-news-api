"""Include the canonical plan catalog in installed distributions."""
from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py


class BuildWithPlans(build_py):
    def run(self):
        super().run()
        target = Path(self.build_lib) / 'prism_news_api' / 'data' / 'plans.json'
        target.parent.mkdir(parents=True, exist_ok=True)
        self.copy_file('plans.json', str(target))


setup(cmdclass={'build_py': BuildWithPlans})
