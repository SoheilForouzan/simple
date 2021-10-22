import pdfkit

url = input('[?] Enter URL >>>> ')
output = input('[?] Enter output file >>>> ')

pdfkit.from_url(url, output)