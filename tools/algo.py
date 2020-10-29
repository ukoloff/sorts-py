from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec


def enum():
    me = Path(__file__)
    folder = me.parent.parent / me.stem
    result = {}
    for z in folder.glob('**/*.py'):
      k = '.'.join(z.with_name(z.stem).relative_to(folder).parts)
      result[k] = spec_from_file_location("sorts." + k, z).loader.load_module()
    return result
