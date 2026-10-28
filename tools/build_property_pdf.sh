# Usage (from repo root): bash tools/build_property_pdf.sh research/properties/<name>.md <out>.pdf
# One-page property summaries: A4 portrait, otherwise the report style.
set -e
T=$(cd "$(dirname "$0")" && pwd)
D=$(mktemp -d)
pandoc "$1" -f gfm-tex_math_dollars -t html5 -s --metadata title="Property decision summary" -o $D/page.html
python3 -I - "$D/page.html" "$T/style.css" <<'PY'
import re, sys
p, cssp = sys.argv[1], sys.argv[2]
t=open(p,encoding='utf-8').read()
t=re.sub(r'<header id="title-block-header">.*?</header>','',t,flags=re.S)
t=re.sub(r'<style>.*?</style>','',t,flags=re.S)
css=open(cssp).read().replace('size: A4 landscape','size: A4 portrait')+'@page{margin:8mm 12mm} h1{margin:0 0 1mm} h2{margin:3mm 0 1.5mm} td:nth-child(-n+4){white-space:nowrap} body{line-height:1.25;font-size:8.4pt} p{margin:0 0 1.5mm}'
t=t.replace('</head>','<style>html,body{max-width:none!important;margin:0!important;padding:0!important;}'+css+'</style></head>')
open(p,'w',encoding='utf-8').write(t)
PY
node $T/render.js $D/page.html "$(realpath -m "$2")" $D/shot.png
