price_stats = f"""
    select *, date_trunc('day', recorded_at) as date
    from osmosis.core.dim_prices
    where symbol = 'osmo'
    group by symbol, date, recorded_at, price, total_supply, volume_24h, provider

"""