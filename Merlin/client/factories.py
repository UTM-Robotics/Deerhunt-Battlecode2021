from Engine.client.client_launcher import DecodeDataFactory, EncodeDataFactory

from .move import MerlinClientMove

class MerlinDecodeDataFactory(DecodeDataFactory):
  def decode(js):
    return ({
      'game_map': Map(js['map']),
      'my_units': Units(js['my_units']),
      'their_units': Units(js['their_units']),
      'my_resources': js['my_resources'],
      'turns_left': js['turns_left'],
      'your_flag': js['your_flag'],
      'their_flag': js['their_flag']
    })

class MerlinEncodeDataFactory(EncodeDataFactory):
  def encode(moves):
      data = []
      for move in moves:
        if isinstance(move, MerlinClientMove):
          data.append(move.to_tuple())
        else:
          print('Expected type Move but got {}'.format(type(move)))
      return data
