import json
import os

import requests
from haralyzer import HarPage, HarParser

target_links_file = "links.txt"
har_file = "har.txt"


def form_links_file(har_file):
    with open(har_file, "r") as f:
        har_parser = HarParser(json.loads(f.read()))

    data = har_parser.har_data["entries"]
    image_urls = []

    for entry in data:
        if entry["response"]["content"]["mimeType"].find("image/") == 0:
            image_urls.append(entry["request"]["url"])

    with open(target_links_file, "w") as f:
        for link in image_urls:
            f.write("%s\n" % link)


def download_images(har_file, save_folder):
    os.makedirs(save_folder, exist_ok=True)

    form_links_file(har_file)

    with open(target_links_file, "r") as file:
        for index, url in enumerate(file):
            url = url.strip()
            if not url:
                continue

            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()

                image_name = f"image_{index + 1}.jpg"
                image_path = os.path.join(save_folder, image_name)

                with open(image_path, "wb") as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)

                print(f"Downloaded: {image_name}")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")

    os.remove(target_links_file)


script_directory = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(script_directory, "images")
download_images(har_file, images_folder)
