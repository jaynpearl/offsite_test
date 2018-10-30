import click
from datetime import datetime

@click.command()
@click.option('--file', prompt='Log file', help='Log file location')
@click.option('--start_date', prompt='Start Date in "yyyy-mm-dd"', help='Start Date')
@click.option('--end_date', prompt='End Date inclusive in "yyyy-mm-dd"', help='End Date')
@click.option('--extension', prompt='Extension of the file', help='Extension of File')
def sum_total_data(file, start_date, end_date, extension):
    date_pattern = '%Y-%m-%d'
    from_date = datetime.strptime(start_date, date_pattern)
    to_date = datetime.strptime(end_date, date_pattern)
    count = 0
    with open(file, 'r') as f:
        for line in f:
            cols = line.strip().lower().split('\t')
            date = datetime.strptime(cols[0], date_pattern)
            if(date > to_date):
                break
            if(date >= from_date and cols[3].endswith(extension)):
                count += int(cols[2])
    click.echo(count)

if __name__ == '__main__':
	sum_total_data()
