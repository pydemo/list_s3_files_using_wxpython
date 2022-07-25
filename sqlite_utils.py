
def drop_table(tname):
    cmd=['DROP TABLE %s;' % tname.strip()]
    exec_sqlite(cmd)

def exec_sqlite(incmd):
    spath = str(Path(SLITE_LOC).resolve())
    dpath = str(Path(DB_NAME).resolve())
    #csv_file = Path('%s_ocean.csv' % REPORT).resolve()
    cmd=[spath, dpath] + incmd
    #pp(cmd)	
    #e()
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell = True)
    retout=[]
    errout = []
    while p.poll() == None: 

        out=p.stdout.readline()
        if out:
            #print('OUTPUT:', out)
            retout.append(out)
        er=p.stderr.readline()
        if er:
            print('ERROR:', er)
            errout.append(er)
    p.wait()

    rcode = p.returncode
    #print('RETCODE: ', rcode)
    return  rcode, retout, errout

def load_table(tname, fname):
    assert isfile(fname), fname
    cmd=[ '.mode csv', ".separator ','", '.import %s %s' % (fname.replace('\\','/'), tname), 'SELECT count(*) from %s;' % tname]
    pp(cmd)
    return exec_sqlite(cmd)

def desribe(tname, fname):
    assert isfile(fname), fname
    cmd=[ '.mode csv', ".separator ','", '.import %s %s' % (fname, tname), 'SELECT count(*) from %s;' % tname]

    return exec_sqlite(cmd)
def describe(tname):
    cur = con.cursor()
    out=con.execute(f"PRAGMA table_info({tname})")
    for x in out.fetchall():
        print(x)
        