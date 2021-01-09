from PyPDF2 import PdfFileReader
import pprint
import sys,argparse
import bcolors


def banner():
    print("""
            ██████╗░██████╗░███████╗███╗░░░███╗███████╗████████╗░█████╗░░░░░░░███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗
            ██╔══██╗██╔══██╗██╔════╝████╗░████║██╔════╝╚══██╔══╝██╔══██╗░░░░░░██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
            ██████╔╝██║░░██║█████╗░░██╔████╔██║█████╗░░░░░██║░░░███████║█████╗█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░
            ██╔═══╝░██║░░██║██╔══╝░░██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║╚════╝██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░
            ██║░░░░░██████╔╝██║░░░░░██║░╚═╝░██║███████╗░░░██║░░░██║░░██║░░░░░░███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░
            ╚═╝░░░░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░
                                                                                                                             Code By: NG
              """
          )

if len(sys.argv) > 1:
        banner()
        if (sys.argv[1] != 'p'):
            try:
                input_pdf_location = sys.argv[2]
                parser = argparse.ArgumentParser()
                parser.add_argument("-p", required=True)

                print(bcolors.BITALIC + "Testing for PDF META Data")

                try:
                    input_pdf_read = PdfFileReader(open(input_pdf_location, "rb"))
                    input_pdf_info = input_pdf_read.getDocumentInfo()
                    pp = pprint.PrettyPrinter(indent=10)
                    pp.pprint(input_pdf_info)

                except:
                    print(bcolors.ERRMSG + 'Meta data does not found for this PDF')
            except:
              print(bcolors.OKMSG + 'Please enter python pdfmeta.py -p < Valid pdf location > ')
elif (sys.argv[1] != '-p'):
    print(bcolors.OKMSG + 'Please enter -p < Valid pdf location >')
else:
    banner()
    print(bcolors.ERR + 'Please select  valid option a valid pdf location ')




