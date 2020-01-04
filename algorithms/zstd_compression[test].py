import sys

import zstandard as zstd

nums = [1, 2, 3]
nums_bytes = [bytes([1, 2, 3]), bytes([1, 2, 3]), bytes([1, 2, 3])]
cctx = zstd.ZstdCompressor()
dict = zstd.ZstdCompressionDict
compressed = cctx.compress(bytearray(nums))
print(sys.getsizeof(nums_bytes))
dict_data = zstd.train_dictionary(nums_bytes)
print(compressed)
print(sys.getsizeof(nums))
print(sys.getsizeof(compressed))
dctx = zstd.ZstdDecompressor()
decompressed = dctx.decompress(compressed)
for x in decompressed:
    print(x)
