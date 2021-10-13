import re
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
INVENTARIO="/nombre/servidores.txt"
AD="/lista/dominios.txt"
SALIDA="/inventario/salida_" + timestr


with open(AD, 'r') as f:
  dom_list = [line.strip() for line in f]

with open(INVENTARIO, 'r') as f:
  server_list = [line.strip() for line in f]


def append_new_line(file_name, text_to_append):
  """Append given text as a new line at the end of file"""
  # Abre el fichero en modo adicion y lectura  ('a+')
  with open(file_name, "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0:
      file_object.write("\n")
    # Append text at the end of file
    file_object.write(text_to_append)

# Agrupa los servidores segun los dominios y escribe a fichero
for y in dom_list:
  res = [ x for x in server_list if re.search(y, x)]
  append_new_line(SALIDA, '[' + y + ']')
  for item in res:
    append_new_line(SALIDA, item)

