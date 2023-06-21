from requests_html import HTMLSession
import pandas as pd
from tqdm import tqdm

coordinates= [[42.850685, 44.055238],[42.834184, 44.306955],[43.043014,44.721001]]

def distance_km(text):# Просто перебираем текст и оставляем число перед нужным нам словом
    for i , j in tqdm(enumerate(text)):
        if j=='километров':
            distance=float(text[i-1])
        elif j=='метров':
            distance=(float(text[i-1]))/1000
        elif j=='метра':
            distance=(float(text[i-1]))/1000
        elif j=='метр':
            distance=(float(text[i-1]))/1000
        elif j=='километр':
            distance=float(text[i-1])
        elif j=='километра':
            distance=float(text[i-1])
    return distance

def parse_distance(coordinates, last_coordinates):
    dis_km = []
    start_link = "https://2gis.ru/directions/points/"
    for point in range(len(coordinates)):
        mode_part=f'{last_coordinates[1]}%2C{last_coordinates[0]}%7C{coordinates[point][1]}%2C{coordinates[point][0]}%7C'
        link = start_link + mode_part
        session_new = HTMLSession()
        response = session_new.get(link)
        dis_km.append(distance_km(response.html.text.split()))
    return dis_km




if __name__ == "__main__":
    parse_distance(coordinates, [42.720592, 44.621986])

