# PGM-Scripts
Just some useful scripts I've used to treat PGM XML files.
Always recommended to have a backup of your files.

### teleport_regions.py
Allows you to use `point` and `cylinder` regions in `<teleport/>` actions (converts `<teleport region="id"/>` to `<teleport x="" y="" z=""/>` upon execution. Keeps `yaw` and `pitch`).

Warning: will remove your comments unless converted to use `lxml`.
