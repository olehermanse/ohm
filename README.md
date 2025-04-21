# ohm schematic drawer

A simple tool to draw SVG circuit schematics and similar diagrams in the browser.

The tool is available online:

[ohm.oleherman.com](https://ohm.oleherman.com/)

## Features

- Open source, GPLv3 license.
- Completely client side - no tracking, ads, or saving of your data.
- One single [`index.html`](./index.html) file, no build steps, minification, dependencies, source maps, or similar.
  The file can be edited directly, opened in a browser, etc.

## Tools

In the left bar there are 9 icons representing what is possible:

1. **Pencil:** Create lines / wires.
   In order to finish a drawing, click again on the last point, or close the loop.
2. **Dot:** Create filled in dots, typically used to indicate that crossing wires are connected.
3. **Circle:** Create circles.
   Often used for input / output terminals, or for other decorations.
   Click and drag to create bigger circles.
4. **T:** Create text.
   Click once, start typing, then click again to place.
5. **Arrows in 4 directions:** Move objects.
   Click once to pick something up and again to place.
6. **Two squares:** Copy.
   Click once to select something and again to place a copy.
7. **X:** Delete.
   Hover over objects to see what will be deleted.
8. **Floppy drive:** Save / download / export as SVG.
9. **Up arrow out of a box:** Load / upload / import SVG.

## Tips / keyboard shortcuts

There are some features which are only accessible via keyboard shortcuts:

- **Resize canvas:** Up, down, left, and right arrow keys can be used to increase / decrease the size.
- **Change grid:** 1,2,3, and 4 keys can be used to change the grid size.
  This can help make smaller details / spaces between lines and more specific circle sizes.

## Non-goals

It can be helpful to make a focused and simple tool, thus there are some things we don't want to add:

- Only SVG file format is supported, other tools can be used to convert to other file formats.
- Only SVGs created with ohm are supported, don't expect SVGs from other editors to be working correctly.
- The tool only creates black and white diagrams, which matches the type of circuit schematics we're trying to make.
  You can add colors using other tools or by editing the SVG afterwards.
- Any complex features needed for other types of image editing, but not for black and white circuit schematic diagrams.

## Examples

See the [examples folder](./examples) for some examples of diagrams made in this tool.

Additionally, see this other repo for schematics I made in the same style using Illustrator, before creating this tool:

https://github.com/olehermanse/schem

## Run offline / locally

The entire tool is self contained inside `index.html` - you can download this file and run it in your browser.

When this is deployed, it is running in a minimal nginx Dockerfile (just 2 lines).
You can run this locally as well, with `docker`:

```bash
docker build --tag ohm . && docker run -it -p 8000:80 --name ohm --rm ohm
```

Or with `podman`:

```bash
podman build --tag ohm . && podman run -it -p 8000:80 --name ohm --rm ohm
```

Open in the browser:

http://127.0.0.1:8000

## License

This project is open source and licensed under the GPLv3 license.
See [LICENSE](./LICENSE) for the full license.

Written by [@olehermanse](https://github.com/olehermanse), with design by [@PrebenAas](https://github.com/PrebenAas).
