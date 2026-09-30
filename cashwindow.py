"""CashWindow: source-linked search evidence for zero-capital opportunities."""
import argparse, datetime as dt, json, os, re, urllib.parse, urllib.request
from pathlib import Path

def screen(item, end):
    text = (item.get('title','')+' '+item.get('snippet','')).lower()
    flags = []
    for label, pattern in [('Possible upfront cost',r'entry fee|registration fee|deposit|paid subscription'),('Possible human attendance',r'in.person|onsite|on.site|live interview'),('Prize, not guaranteed pay',r'prize|hackathon|competition|challenge'),('AI restriction needs review',r'no ai|human.only|ai prohibited')]:
        if re.search(pattern,text): flags.append(label)
    dates=[]
    for match in re.finditer(r'\b(\d{4}-\d{2}-\d{2})\b', text):
        try: dates.append(dt.date.fromisoformat(match.group(1)))
        except ValueError: pass
    return {'title':item.get('title','Untitled'),'url':item.get('link',''), 'evidence':item.get('snippet',''), 'flags':flags,'dates_in_snippet':[d.isoformat() for d in dates], 'window_note':'Snippet mentions date after experiment end' if any(d>end for d in dates) else 'Payment date and eligibility unverified', 'cash_status':'No cleared cash evidenced'}

def search(query):
    key=os.environ.get('SERPAPI_API_KEY')
    if not key: raise ValueError('Set SERPAPI_API_KEY for live search; --fixture runs offline.')
    params=urllib.parse.urlencode({'engine':'google','q':query,'gl':'in','hl':'en','num':10,'api_key':key})
    request=urllib.request.Request('https://serpapi.com/search.json?'+params,headers={'User-Agent':'CashWindow/0.1'})
    # Never print the request URL: it includes a credential.
    try:
        with urllib.request.urlopen(request,timeout=25) as response: data=json.load(response)
    except Exception: raise RuntimeError('Search failed; check connection, account quota and key. Request URL withheld.') from None
    if data.get('error'): raise RuntimeError('Search service returned an error; check account and quota.')
    return data.get('organic_results',[])

def build(results,end,query):
    seen=set(); entries=[]
    for item in results:
        url=item.get('link','')
        if not url.startswith(('https://','http://')) or url in seen: continue
        seen.add(url); entries.append(screen(item,end))
    return {'query':query,'experiment_end':end.isoformat(),'generated_at':dt.datetime.now(dt.timezone.utc).isoformat(),'notice':'Search snippets are discovery evidence, not verified terms or payment guarantees. Open original sources before applying. Dates refer to any snippet event, not necessarily payment.','entries':entries}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--query',default='India online hackathon cash prizes AI allowed October 2026')
    p.add_argument('--end',default='2026-10-29')
    p.add_argument('--fixture',type=Path)
    p.add_argument('--output',type=Path,default=Path('evidence.json'))
    args=p.parse_args()
    try:
        end=dt.date.fromisoformat(args.end)
        results=json.loads(args.fixture.read_text())['organic_results'] if args.fixture else search(args.query)
        report=build(results,end,args.query)
        args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False))
        print(f'Saved {len(report["entries"])} source-linked leads to {args.output}. No revenue is claimed.')
    except (ValueError,RuntimeError,OSError,KeyError) as error: p.exit(1,str(error)+'\n')

if __name__=='__main__': main()
