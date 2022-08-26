import requests, csv
from bs4 import BeautifulSoup

def main():
    
    file = open('data.csv', 'w', newline='')
    writer = csv.writer(file)
    headers = ['name', 'location', 'cuisine', 'ratings']
    writer.writerow(headers)

    for i in range(1, 11):
        URL = "https://www.quandoo.sg/result?destination=singapore&reviewScoreMin=400&bookable=true&page={i}"
        read_page(URL, file)
    
    file.close()

def read_page(URL, file):
    page = requests.get(URL)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")
    restaurant_elements = soup.find_all("div", class_="sc-AxirZ sc-AxiKw sc-1vnptfs-1 iTkAfG")


    for restaurant_element in restaurant_elements:
        title_element = restaurant_element.find("h3", class_="sc-1vnptfs-3 jjhqNf").get_text()
        location_element = restaurant_element.find("span", class_="sc-13j8xb1-0 cFfDvf").get_text()
        cuisine_element = restaurant_element.find("span", class_="sc-1ohzhdx-0 kPKdEs").get_text()
        ratings_element = restaurant_element.find("div", class_="sc-1atis9w-1 bYipHC").get_text()

        file = open('data.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow([title_element, location_element, cuisine_element, ratings_element])
        file.close()

if __name__ == '__main__':
    main()
