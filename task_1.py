from datetime import datetime
def get_days_from_today(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()
    delta = today - date_obj
    return delta.days

date = '2022-02-24'
days_difference = get_days_from_today(date)
print("Кількість днів з {} (почтаку повномаштабного вторгення) і сьогодні: {}".format(date, days_difference))
