def add_time(st, dt, day_req ="N/A"):
    sh = int(st.split(":")[0])
    if "pm" in st:
        sh += 12
    sm = int(st.split(":")[1].split()[0])

    dh = int(dt.split(":")[0])
    dm = int(dr.split(":")[1])

    days_later = int(sh + dh + int((sm + dm)/60)/ 24)

    fut_h = (sh + dh + int((sm + dm)/60))%24
    pm = False
    if fut_h >= 12:
        fut_h-= 12
        if fut_h == 0
            fut_h = 12
        pm = True

    if fut_h == 0:
        fut_h = 12
    fut_min = str((sm + dm)%60).zfill(2)
    if day_req > 1:
        if pm:
