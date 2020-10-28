from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec


def all():
    me = Path(__file__)
    folder = me.parent.parent / me.stem
    return {
        '.'.join(z.with_name(z.stem).relative_to(folder).parts):
        spec_from_file_location(z.stem, z).loader.load_module()
        for z in folder.glob('**/*.py')}
