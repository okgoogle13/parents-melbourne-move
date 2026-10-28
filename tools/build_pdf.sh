# Usage (from repo root): bash tools/build_pdf.sh "Suburb shortlist foundation report.md" "Suburb shortlist foundation report.pdf"
set -e
T=$(cd "$(dirname "$0")" && pwd)
D=$(mktemp -d)
pandoc "$1" -f gfm-tex_math_dollars -t html5 -s --metadata title="Suburb shortlist foundation report" -c style.css -o $D/report.html
python3 -I - "$D/report.html" "$T/style.css" <<'PY'
import re, sys
p, cssp = sys.argv[1], sys.argv[2]
t=open(p,encoding='utf-8').read()
t=re.sub(r'<header id="title-block-header">.*?</header>','',t,flags=re.S)
css=open(cssp).read()
t=t.replace('<link rel="stylesheet" href="style.css" />','<style>html,body{max-width:none!important;margin:0!important;padding:0!important;} table{display:table!important;overflow:visible!important;}'+css+'</style>')
open(p,'w',encoding='utf-8').write(t)
PY
node $T/render.js $D/report.html "$(realpath -m "$2")" $D/shot.png
