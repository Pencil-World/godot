import brotli

with open("bin/web_zip/godot.wasm", "rb") as f:
  data = f.read()

compressed = brotli.compress(data, quality=11)

with open("bin/web_zip/godot.wasm.br", "wb") as f:
  f.write(compressed)
