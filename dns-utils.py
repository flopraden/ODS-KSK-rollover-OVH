import re
import subprocess
import logger


regremovespace=re.compile(' +')

# create logger
logger = logging.getLogger('DNS-UTILS')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def get_ds(domains,servers=['8.8.8.8', '8.8.4.4']):
    ret={}
    for domain in domains:
        for server in servers:
            # Get keys DS from parent DNS server
            logger.debug('Ask DS for %s to %s',domain,server)
            (errno,output)=subprocess.getstatusoutput('dig %s DS @%s' % (domain,server))
            if errno != 0:
                logger.error("DIG ERROR %d: %s",errno,output)
                break
            logger.debug('Server response : %d / %s',errno,output)
            ds=regds.findall(output)
            for (domain,keytag,algorithm,shaid,shasum) in ds:
                iKeyTag=int(keytag)
                ishaid=int(shaid)
                d=ret.get(domain,{})
                k=d.get(iKeyTag,{})
                shaok=regremovespace.sub('',shasum).lower()
                if ishaid in k:
                    if shaok != k[ishaid]:
                        logger.error("Get another DS for the same key domain=%s tag=%d proto=%d ( %s / %s)",domain,iKeyTag,ishaid,k[ishaid],shaok)
                else:
                    k[ishaid]=shaok
                    d[iKeyTag]=k
                    ret[domain]=d
            if len(ds) > 0:
                break
    return ret
