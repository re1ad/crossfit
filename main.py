import csv
import requests


def write_csv(data):
    with open('data.csv', 'a', encoding='UTF-8') as file:
        fieldnames = ['Name', 'Website', 'Country', 'City', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)


def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def main():
    page = 1
    url = 'https://www.crossfit.com/cf/find-a-box.php?page={}&country=US&state=&city=&type=Commercial'
    while True:
        data = get_data(url.format(page))
        affiliates = data['affiliates']
        if not affiliates:
            return
        for elm in affiliates:
            write_csv(
                {
                    'Name': elm['name'],
                    'Website': elm['website'],
                    'Country': elm['country'],
                    'City': elm['city'],
                    'Address': elm['address']
                }
            )
        page += 1


if __name__ == '__main__':
    main()
