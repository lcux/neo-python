
from neo.IO.Mixins import SerializableMixin
import sys
from autologging import logged

@logged
class InvPayload(SerializableMixin):

    Type = None
    Hashes = []

    def __init__(self, type=None, hashes=None):
        self.Type = type
        self.Hashes = hashes if hashes else []


    def DistinctHashes(self):
        return set(self.Hashes)

    def Size(self):
        return sys.getsizeof(self.Type) + sys.getsizeof(self.Hashes)


    def Deserialize(self, reader):

        self.Type = reader.ReadByte()

        self.Hashes = reader.ReadHashes()


    def Serialize(self, writer):
        self.__log.debug("Will write hashes: %s " % self.Hashes)
        try:
            writer.WriteByte(self.Type)
            writer.WriteHashes(self.Hashes)
        except Exception as e:
            print("COULD NOT WRITE INVENTORY HASHES %s " % e)
