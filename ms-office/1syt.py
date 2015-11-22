__author__ = 'corey'

import sys
import os
from win32com.client import DispatchEx


# # Generate all the support we can.
# def GenerateSupport():
#     # enable python COM support for Word 2007
#     # this is generated by: makepy.py -i "Microsoft Word 12.0 Object Library"
#     gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)

def doc2pdf(input, output):
    w = Dispatch("Word.Application")
    w.Visible = False
    try:
        doc = w.Documents.Open(input, ReadOnly=1)
        doc.ExportAsFixedFormat(output, 17, False, 1)
        return 0
    except Exception as inst:
        print(type(inst), inst.args, inst)
        return 1
    finally:
        w.Quit()


def excel2pdf(input, output):
    w = Dispatch("Excel.Application")
    try:
        doc = w.Workbooks.Open(input, ReadOnly=1)
        doc.ExportAsFixedFormat(0, output)
        return 0
    except Exception as inst:
        print(type(inst), inst.args, inst)
        return 1
    finally:
        w.Quit()


def ppt2pdf(input, output):
    w = Dispatch("PowerPoint.Application", 1)
    try:
        doc = w.Presentations.Open(input, False, False, False)
        doc.ExportAsFixedFormat(output,
                                2,
                                1,
                                PrintRange=None)
        return 0
    except Exception as inst:
        print(type(inst), inst.args, inst)
        return 1
    finally:
        w.Quit()


def vsd2pdf(input, output):
    w = Dispatch("Visio.Application")
    w.Visible = 0
    try:
        doc = w.Documents.Open(input)
        doc.ExportAsFixedFormat(1, output, 1, 0)
        return 0
    except Exception as inst:
        print(type(inst), inst.args, inst)
        return 1
    finally:
        w.Quit()


def DispatchFun(path, out):
    p = path.lower()
    if p.endswith('doc') or p.endswith('docx'):
        return doc2pdf(path, out)
    elif p.endswith('xls') or p.endswith('xlsx'):
        return excel2pdf(path, out)
    elif p.endswith('ppt') or p.endswith('pptx'):
        return ppt2pdf(path, out)
    elif p.endswith('vsd') or p.endswith('vsdx'):
        return vsd2pdf(path, out)
    else:
        print("else...... ")
        return -1


def main():
    if (len(sys.argv) == 2):
        input = sys.argv[1]
        output = os.path.splitext(input)[0] + '.pdf'
    elif (len(sys.argv) == 3):
        input = sys.argv[1]
        output = sys.argv[2]
    else:
        return -1

    if not os.path.exists(input):
        return -1

    if not os.path.isabs(input):
        input = os.path.abspath(input)
    if not os.path.isabs(output):
        output = os.path.abspath(output)
    try:
        rc = DispatchFun(input, output)
        return rc
    except:
        return -1


if __name__ == '__main__':
    # from time import clock

    # start = clock()

    rc = main()

    # finish = clock()
    # print((finish - start))

    if rc:
        sys.exit(rc)
    sys.exit(0)
