#
import hbmqtt as h
import hbmqtt.mqtt as hm
import hbmqtt.mqtt.packet as hmp


class MqttEncoder(IEncoder):
    TYPES = {
        # Type: Packet, [Variable Header], [Payload]
        hmp.CONNECT: (hm.connect.ConnectPacket, hm.connect.ConnectVariableHeader, hm.connect.ConnectPayload),
        # ...
    }

    # ...

    @staticmethod
    def parse(packetcls, data) -> Tuple[hmp.MQTTPacket, int]:
        buff = h.adapters.BufferReader(data)
        future = packetcls.from_stream(buff)
        packet = asyncw.INSTANCE.runSync(future)
        return (packet, buff._stream.tell())

    def decode(self, msg: Message, context: StateContext) -> Tuple[ProtocolData,  EncodingResult]:
        binSource = cast(BinarySource, msg.latest_data.source)
        data = binSource.blob
        self._data_ += data

        try:
            packet, length = MqttEncoder.parse(
                hbmqtt.mqtt.packet.MQTTPacket, self._data_)
            cls, _, _ = MqttEncoder.TYPES.get(packet.fixed_header.packet_type)
            if not cls:
                raise Exception(
                    f"Unknown packet_type {packet.fixed_header.packet_type}")
            else:
                packet, length = MqttEncoder.parse(cls, self._data_)
            self._data_ = self._data_[length::]

            fields = {
                'fixed_header': packet.fixed_header,
                'variable_header': packet.variable_header,
                'payload': packet.payload
            }
            payload = b''
            pdata = ProtocolData(
                msg.latest_data.direction, fields, BinarySource(payload), 'MQTT')
            return (pdata, EncodingResult.SUCCESS)
        except Exception as e:
            print(e)
            return (None, EncodingResult.INCOMPLETE)
