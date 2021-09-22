import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head())

click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source.head(10))

click_source_by_month = user_visits.groupby(
    ['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month.head())

click_source_by_month_pivot = click_source_by_month.pivot(
    index = 'utm_source',
    columns = 'month',
    values = 'id').reset_index()
print(click_source_by_month_pivot)
