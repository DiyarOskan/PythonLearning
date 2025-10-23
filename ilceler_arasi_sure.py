import googlemaps
from datetime import datetime
import time
import csv

gmaps = googlemaps.Client(key='google key')

districts = [
    "Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler",
    "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü",
    "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt",
    "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane",
    "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer",
    "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla", "Ümraniye",
    "Üsküdar", "Zeytinburnu"
]
fixed_time = datetime(2025, 8, 1, 18, 0)

with open('istanbul_traffic_extreme_scenarios.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Origin', 'Destination', 'Duration (Optimistic)', 'Duration (Best Guess)', 'Duration (Pessimistic)', 'Distance (km)'])

    for origin in districts:
        for destination in districts:
            if origin != destination:
                try:
                    # Optimistic (En kısa süre)
                    route_opt = gmaps.directions(
                        origin + ", İstanbul",
                        destination + ", İstanbul",
                        mode="driving",
                        departure_time=fixed_time,
                        traffic_model="optimistic"
                    )
                    duration_opt = route_opt[0]['legs'][0]['duration_in_traffic']['text']

                    # Best Guess (Ortalama süre)
                    route_best = gmaps.directions(
                        origin + ", İstanbul",
                        destination + ", İstanbul",
                        mode="driving",
                        departure_time=fixed_time,
                        traffic_model="best_guess"
                    )
                    duration_best = route_best[0]['legs'][0]['duration_in_traffic']['text']

                    # Pessimistic (En uzun süre)
                    route_pess = gmaps.directions(
                        origin + ", İstanbul",
                        destination + ", İstanbul",
                        mode="driving",
                        departure_time=fixed_time,
                        traffic_model="pessimistic"
                    )
                    duration_pess = route_pess[0]['legs'][0]['duration_in_traffic']['text']

                    # Mesafe (tüm senaryolarda aynı)
                    distance = route_best[0]['legs'][0]['distance']['text']

                    writer.writerow([origin, destination, duration_opt, duration_best, duration_pess, distance])
                    print(f"{origin} → {destination}: Optimistic={duration_opt}, Best={duration_best}, Pessimistic={duration_pess}")

                    time.sleep(1)  # API limiti için bekle

                except Exception as e:
                    print(f"Hata: {origin} → {destination}: {str(e)}")
                    writer.writerow([origin, destination, "ERROR", "ERROR", "ERROR", "ERROR"])

print("Veri toplama tamamlandı. 'istanbul_traffic_extreme_scenarios.csv' dosyası oluşturuldu.")
