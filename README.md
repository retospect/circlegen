# Circlegen

A tool to quickly generate photomasks for repeating patterns. 

This tool writes regular SVG patterns and converts them to EPS files, which can then be made into photomasks by companies like https://artnetpro.com/

## Files

- base.py - utilities.
- spiral.py - a very basic spiral shape generator
- wafer*.py - defines a wafer mask 

## Conversion/steps to use

The tool generates an svg file. The services generally want a dxf or an eps file.

Inkscape (brew install inkscape) can convert to either format. But paths work only in eps. 

```
python mask1.py > mask.svg
inkscape mask.svg
# save as eps from inkscape, using the menu.
```

(There is a way to do this from the commandline, too.)

## Testing individual patterns

Individual patterns like spiral.py can be run directly for development and debugging:
```spiral.py > spiral.svg```
