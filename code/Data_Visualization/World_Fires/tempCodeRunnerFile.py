    lons, lats, frps, dates = [], [], [], []
    for row in fire_data:
        lons.append(row[header_row.index('longitude')])
        lats.append(row[header_row.index('latitude')])
        frps.append(row[header_row.index('frp')])
        dates.append(row[header_row.index('acq_date')])
