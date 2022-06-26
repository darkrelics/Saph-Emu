from struct import Struct

from saphemu.world.opcodes import OpCode
from saphemu.world.world_packet import WorldPacket


class PingHandler:
    """Answer to a ping from client."""

    PACKET_BIN = Struct("<I")

    def __init__(self, connection, packet):
        self.conn = connection
        self.packet = packet

    def process(self):
        pong_packet = WorldPacket(OpCode.SMSG_PONG, self.packet)
        return None, pong_packet
