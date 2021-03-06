
from .MemoryStream import MemoryStream
from .BinaryReader import BinaryReader
import importlib


class Helper(object):

    @staticmethod
    def AsSerializableWithType(buffer, class_name):

        module = '.'.join(class_name.split('.')[:-1])
        klassname = class_name.split('.')[-1]
        klass = getattr(importlib.import_module(module), klassname)
        mstream = MemoryStream(buffer)
        reader = BinaryReader(mstream)

        try:
            serializable = klass()
            serializable.Deserialize(reader)

            return serializable
        except Exception as e:
            print("Colud not deserialize %s %s" % (klassname, e))


        return None