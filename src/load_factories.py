import inspect
import parsing
from py_linq import Enumerable

factory_types = Enumerable([m for _, m in inspect.getmembers(parsing)])\
    .where(lambda m: inspect.isclass(m) and not inspect.isabstract(m) and parsing.factory.IFactory in inspect.getmro(m))\
    .to_list()

for factory_type in factory_types:
    parsing.SITE.install_factory_type(factory_type)
