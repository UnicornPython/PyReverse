import requests 


def main():

    imgs = [
        "digital_reform_100000_1000020953_1.jpeg",
        "digital_reform_100000_1000020953_2.jpeg",
        "digital_reform_100000_1000020953_3.jpeg",
        "digital_reform_100001_1000020968_1.jpeg",
        "digital_reform_100001_1000020968_2.jpeg",
        "digital_reform_100001_1000020968_3.jpeg",
        "digital_reform_100002_1000020982_1.jpeg",
        "digital_reform_100002_1000020982_2.jpeg",
        "digital_reform_100002_1000020982_3.jpeg",
        "digital_reform_100003_1000020984_1.jpeg"
    ]
    for img in imgs:
        res = requests.get(f"https://112.15.232.86:38084/networkPhotos/{img}", verify=False)
        with open(f"./image/{img}", mode="wb") as f:
            f.write(res.content)


if __name__ == "__main__":
    
    main()
