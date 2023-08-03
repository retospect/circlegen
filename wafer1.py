from yattag import indent
from yattag import Doc

from spiral import spiral

doc, tag, text = Doc().tagtext()

def main():
    with tag('svg', ('width', 80000), ('height', 80000), ('version', '1.1'), ('xmlns', 'http://www.w3.org/2000/svg')):
        with tag('g', ('transform', 'translate(40000 40000)'), ('fill', 'none'), ('stroke-width', 1), ('stroke', 'black')):
            with tag('circle', ('cx', 0), ('cy', 0), ('r', 40000)):
                pass # empty tag

    result = indent(doc.getvalue())
    print(result)

if __name__ == '__main__':
    main()



        
