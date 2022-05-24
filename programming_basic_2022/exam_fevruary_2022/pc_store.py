price_cpu_usd = float(input())
price_video_card_usd = float(input())
price_ram_usd = float(input())
count_ram = int(input())
discount_percent = float(input())
usd_bgn = 1.57
bill_cpu = (price_cpu_usd * usd_bgn)
bill_cpu -= bill_cpu * discount_percent
bill_video_card = (price_video_card_usd * usd_bgn)
bill_video_card -= bill_video_card * discount_percent
total_bill = (count_ram * (price_ram_usd * usd_bgn)) + bill_cpu + bill_video_card
print(f'Money needed - {total_bill:.2f} leva.')