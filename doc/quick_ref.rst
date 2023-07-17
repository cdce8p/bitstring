.. currentmodule:: bitstring

.. _quick_reference:

******************
Quick Reference
******************
This section lists the bitstring module's classes together with all their methods and attributes. The next section goes into full detail with examples.

The first four classes are bit containers, so that each element is a single bit.
They differ based on whether they can be modified after creation and on whether they have the concept of a current bit position.

.. list-table::
   :widths: 30 15 15 40
   :header-rows: 1

   * - Class
     - Mutable?
     - Streaming methods?
     -
   * - ``Bits``
     - ✘
     - ✘
     - An efficient, immutable container of bits.
   * - ``BitArray``
     - ✔
     - ✘
     - Like ``Bits`` but it can be changed after creation.
   * - ``ConstBitStream``
     - ✘
     - ✔
     - Immutable like ``Bits`` but with a bit position and reading methods.
   * - ``BitStream``
     - ✔
     - ✔
     - Mutable like ``BitArray`` but with a bit position and reading methods.


The final class is a flexible container whose elements are fixed-length bitstrings.

.. list-table::
   :widths: 30 15 15 40

   * - ``Array``
     - ✔
     - ✘
     - An efficient list-like container where each item has a fixed-length binary format.


----

Bits
----

``Bits`` is the most basic class and is just a container of bits. It is immutable, so once created its value cannot change.

Methods
^^^^^^^

* :meth:`~Bits.all` -- Check if all specified bits are set to 1 or 0.
* :meth:`~Bits.any` -- Check if any of specified bits are set to 1 or 0.
* :meth:`~Bits.copy` -- Return a copy of the bitstring.
* :meth:`~Bits.count` -- Count the number of bits set to 1 or 0.
* :meth:`~Bits.cut` -- Create generator of constant sized chunks.
* :meth:`~Bits.endswith` -- Return whether the bitstring ends with a sub-bitstring.
* :meth:`~Bits.find` -- Find a sub-bitstring in the current bitstring.
* :meth:`~Bits.findall` -- Find all occurrences of a sub-bitstring in the current bitstring.
* :meth:`~Bits.join` -- Join bitstrings together using current bitstring.
* :meth:`~Bits.pp` -- Pretty print the bitstring.
* :meth:`~Bits.rfind` -- Seek backwards to find a sub-bitstring.
* :meth:`~Bits.split` -- Create generator of chunks split by a delimiter.
* :meth:`~Bits.startswith` -- Return whether the bitstring starts with a sub-bitstring.
* :meth:`~Bits.tobitarray` -- Return bitstring as a ``bitarray`` object from the `bitarray <https://pypi.org/project/bitarray>`_ package.
* :meth:`~Bits.tobytes` -- Return bitstring as bytes, padding if needed.
* :meth:`~Bits.tofile` -- Write bitstring to file, padding if needed.
* :meth:`~Bits.unpack` -- Interpret bits using format string.


Special methods
^^^^^^^^^^^^^^^

Also available are the operators ``[]``, ``==``, ``!=``, ``+``, ``*``, ``~``, ``<<``, ``>>``, ``&``, ``|`` and ``^``.

Properties
^^^^^^^^^^

* :attr:`~Bits.bin` / ``b`` -- The bitstring as a binary string.
* :attr:`~Bits.bool` -- For single bit bitstrings, interpret as True or False.
* :attr:`~Bits.bytes` -- The bitstring as a bytes object.
* :attr:`~Bits.float` / ``floatbe`` / ``f`` -- Interpret as a big-endian floating point number.
* :attr:`~Bits.floatle` -- Interpret as a little-endian floating point number.
* :attr:`~Bits.floatne` -- Interpret as a native-endian floating point number.
* :attr:`~Bits.float8_143` -- Interpret as an 8 bit float with float8_143 format.
* :attr:`~Bits.float8_152` -- Interpret as an 8 bit float with float8_152 format.
* :attr:`~Bits.bfloat` / ``bfloatbe`` -- Interpret as a big-endian bfloat floating point number.
* :attr:`~Bits.bfloatle` -- Interpret as a little-endian bfloat floating point number.
* :attr:`~Bits.bfloatne` -- Interpret as a native-endian bfloat floating point number.
* :attr:`~Bits.hex` / ``h`` -- The bitstring as a hexadecimal string.
* :attr:`~Bits.int` / ``i`` -- Interpret as a two's complement signed integer.
* :attr:`~Bits.intbe` -- Interpret as a big-endian signed integer.
* :attr:`~Bits.intle` -- Interpret as a little-endian signed integer.
* :attr:`~Bits.intne` -- Interpret as a native-endian signed integer.
* :attr:`~Bits.len` -- Length of the bitstring in bits.
* :attr:`~Bits.oct` / ``o`` -- The bitstring as an octal string.
* :attr:`~Bits.se` -- Interpret as a signed exponential-Golomb code.
* :attr:`~Bits.ue` -- Interpret as an unsigned exponential-Golomb code.
* :attr:`~Bits.sie` -- Interpret as a signed interleaved exponential-Golomb code.
* :attr:`~Bits.uie` -- Interpret as an unsigned interleaved exponential-Golomb code.
* :attr:`~Bits.uint` / ``u`` -- Interpret as a two's complement unsigned integer.
* :attr:`~Bits.uintbe` -- Interpret as a big-endian unsigned integer.
* :attr:`~Bits.uintle` -- Interpret as a little-endian unsigned integer.
* :attr:`~Bits.uintne` -- Interpret as a native-endian unsigned integer.

----


BitArray
--------

``BitArray(Bits)``


This class adds mutating methods to ``Bits``.

Additional methods
^^^^^^^^^^^^^^^^^^

* :meth:`~BitArray.append` -- Append a bitstring.
* :meth:`~BitArray.byteswap` -- Change byte endianness in-place.
* :meth:`~BitArray.clear` -- Remove all bits from the bitstring.
* :meth:`~BitArray.insert` -- Insert a bitstring.
* :meth:`~BitArray.invert` -- Flip bit(s) between one and zero.
* :meth:`~BitArray.overwrite` -- Overwrite a section with a new bitstring.
* :meth:`~BitArray.prepend` -- Prepend a bitstring.
* :meth:`~BitArray.replace` -- Replace occurrences of one bitstring with another.
* :meth:`~BitArray.reverse` -- Reverse bits in-place.
* :meth:`~BitArray.rol` -- Rotate bits to the left.
* :meth:`~BitArray.ror` -- Rotate bits to the right.
* :meth:`~BitArray.set` -- Set bit(s) to 1 or 0.

Additional special methods
^^^^^^^^^^^^^^^^^^^^^^^^^^

Mutating operators are available: ``[]``, ``<<=``, ``>>=``, ``*=``, ``&=``, ``|=`` and ``^=``.

Properties
^^^^^^^^^^

The same as ``Bits``, except that they are all (with the exception of ``len``) writable as well as readable.

----

ConstBitStream
--------------

``ConstBitStream(Bits)``

This class adds a bit position and methods to read and navigate in the bitstream.

Additional methods
^^^^^^^^^^^^^^^^^^

* :meth:`~ConstBitStream.bytealign` -- Align to next byte boundary.
* :meth:`~ConstBitStream.peek` -- Peek at and interpret next bits as a single item.
* :meth:`~ConstBitStream.peeklist` -- Peek at and interpret next bits as a list of items.
* :meth:`~ConstBitStream.read` -- Read and interpret next bits as a single item.
* :meth:`~ConstBitStream.readlist` -- Read and interpret next bits as a list of items.
* :meth:`~ConstBitStream.readto` -- Read up to and including next occurrence of a bitstring.

Additional properties
^^^^^^^^^^^^^^^^^^^^^

* :attr:`~ConstBitStream.bytepos` -- The current byte position in the bitstring.
* :attr:`~ConstBitStream.pos` -- The current bit position in the bitstring.

----

BitStream
---------

``BitStream(BitArray, ConstBitStream)``

This class contains all of the 'stream' elements of ``ConstBitStream`` and adds all of the mutating methods of ``BitArray``. It is the most general of the four classes, but it is usually best to choose the simplest class for your use case.

----

Array
-----

The bitstring ``Array`` is similar to the ``array`` type in the ``array`` module, except that it is far more flexible.
The ``fmt`` specifies a fixed-length format for each element of the ``Array``, and it behaves largely like a list.

Both the format and the underlying bit data (stored as a ``BitArray``) can be freely modified after creation, and element-wise operations can be used on the ``Array``.

Methods
^^^^^^^

* :meth:`~Array.append` -- Append a single item to the end of the Array.
* :meth:`~Array.byteswap` -- Change byte endianness of all items.
* :meth:`~Array.count` -- Count the number of occurences of a value.
* :meth:`~Array.extend` -- Append multiple items to the end of the Array from an iterable.
* :meth:`~Array.fromfile` -- Append items read from a file object.
* :meth:`~Array.insert` -- Insert an item at a given position.
* :meth:`~Array.pop` -- Return and remove an item.
* :meth:`~Array.reverse` -- Reverse the order of all items.
* :meth:`~Array.tobytes` -- Return Array data as bytes object, padding with zero bits at end if needed.
* :meth:`~Array.tofile` -- Write Array data to a file, padding with zero bits at end if needed.
* :meth:`~Array.tolist` -- Return Array items as a list.

Special methods
^^^^^^^^^^^^^^^

Also available are the operators ``[]``, ``==``, ``!=``, ``+``, ``*``, ``<<``, ``>>``, ``&``, ``|`` and ``^``.

Mutating operators are available: ``[]``, ``<<=``, ``>>=``, ``*=``, ``&=``, ``|=`` and ``^=``.

Properties
^^^^^^^^^^

* :attr:`~Array.data` -- The complete binary data in a ``BitArray`` object. Can be freely modified.
* :attr:`~Array.fmt` -- The format string or typecode. Can be freely modified.
* :attr:`~Array.itemsize` -- The length *in bits* of a single item. Read only.
* :attr:`~Array.trailing_bits` -- If the data length is not a multiple of the fmt length, this BitArray gives the leftovers at the end of the data.

----

Module level
------------

Functions
^^^^^^^^^
* :func:`~bitstring.pack` -- Create a new ``BitStream`` according to a format string and values.

Exceptions
^^^^^^^^^^
* :class:`~bitstring.Error` -- Base class for module exceptions.
* :class:`~bitstring.ReadError` -- Reading or peeking past the end of a bitstring.
* :class:`~bitstring.InterpretError` -- Inappropriate interpretation of binary data.
* :class:`~bitstring.ByteAlignError` -- Whole-byte position or length needed.
* :class:`~bitstring.CreationError` -- Inappropriate argument during bitstring creation.

Module variables
^^^^^^^^^^^^^^^^
* :data:`~bitstring.bytealigned` -- Determines whether a number of methods default to working only on byte boundaries.
* :data:`~bitstring.lsb0` -- If True, index bits with the least significant bit (the final bit) as bit zero.

