import argparse
import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
hdr = { 'User-Agent' : user_agent }
parser = argparse.ArgumentParser(description="Select a file to upload to S3")
parser.add_argument(
    "--url",
    "-u",
    #default='default',
    help="Specifies the url to get ",
    required=True
)

parser.add_argument(
    "--output",
    "-o",
    # default='default',
    help="Specifies the output file ",
    required=True
)
args = parser.parse_args()
filename = args.output
url = args.url

req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
file = response.read()
file = file.decode('UTF8')
playlist = open(filename, "w",encoding='utf-8')
playlist.write(file)

