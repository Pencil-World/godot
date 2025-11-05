import brotli

with open("bin/TTTuwu.wasm", "rb") as f:
  data = f.read()

compressed = brotli.compress(data, quality=11)

with open("bin/TTTuwu_br.wasm", "wb") as f:
  f.write(compressed)
