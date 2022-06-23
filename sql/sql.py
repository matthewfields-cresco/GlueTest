import pandas

def sf(u,pw,acct,wh,db,schema):
    url = URL(
        account = acct,
        user = u,
        database = db,
        schema = schema,
        warehouse = wh,
        password = pw
        )
    sf.eng = create_engine(url)
    sf.conn = sf.eng.connect()
    return
    
