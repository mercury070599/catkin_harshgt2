# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ece470_ur3_driver/command.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class command(genpy.Message):
  _md5sum = "2d2c2700daec81019d4338afb533bad6"
  _type = "ece470_ur3_driver/command"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64[] destination
int32 grip
int32 softhome
float64 duration
"""
  __slots__ = ['destination','grip','softhome','duration']
  _slot_types = ['float64[]','int32','int32','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       destination,grip,softhome,duration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(command, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.destination is None:
        self.destination = []
      if self.grip is None:
        self.grip = 0
      if self.softhome is None:
        self.softhome = 0
      if self.duration is None:
        self.duration = 0.
    else:
      self.destination = []
      self.grip = 0
      self.softhome = 0
      self.duration = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.destination)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.destination))
      _x = self
      buff.write(_get_struct_2id().pack(_x.grip, _x.softhome, _x.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.destination = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 16
      (_x.grip, _x.softhome, _x.duration,) = _get_struct_2id().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.destination)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.destination.tostring())
      _x = self
      buff.write(_get_struct_2id().pack(_x.grip, _x.softhome, _x.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.destination = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 16
      (_x.grip, _x.softhome, _x.duration,) = _get_struct_2id().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2id = None
def _get_struct_2id():
    global _struct_2id
    if _struct_2id is None:
        _struct_2id = struct.Struct("<2id")
    return _struct_2id
