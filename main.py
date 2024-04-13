import os
import sys
import time
from pytube import YouTube
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def download_video_from_tiktok():
    tiktok_url = input("Enter the TikTok profile URL: ")

    # Launch Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get(tiktok_url)
    time.sleep(10)

    # Scroll to the bottom of the page
    scroll_to_bottom(driver)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find video elements and extract their URLs
    videos = soup.find_all("div", {"class": "css-1as5cen-DivWrapper"})
    print("Number of videos:", len(videos))

    # Create a folder to save downloaded videos
    output_folder = "videos"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download each video
    for index, video in enumerate(videos):
        video_url = video.a["href"]
        download_video(video_url, output_folder, index)
        time.sleep(10)

    driver.quit()

def download_video_from_youtube():
    url = input("Enter the YouTube video URL: ")
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading...")
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write(f"[{'=' * i}{' ' * (100 - i)}] {i}%")
            sys.stdout.flush()
            time.sleep(0.1)  # Simulating download time
        print("\nDownload successful!")
        stream.download(output_path="output")
    except Exception as e:
        print(f"Error occurred: {e}")


def scroll_to_bottom(driver, scroll_pause_time=3):
    """
    Scroll to the bottom of the page to load all videos
    """
    screen_height = driver.execute_script("return window.screen.height;")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_screen_height = driver.execute_script("return document.body.scrollHeight;")
        if new_screen_height == screen_height:
            break
        screen_height = new_screen_height

def download_video(link, output_folder, id):
    """
    Download video from given link and save it to the output folder
    """
    print("Downloading video", id)
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'content-length': '0',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    params = {
        'v': '2',
        'tid': 'G-ZSF3D6YSLC',
        'gtm': '45je4480v9115464968za200',
        '_p': '1712804213384',
        'gcd': '13l3l3l3l1',
        'npa': '0',
        'dma': '0',
        'tcfd': '10000',
        'cid': '992252036.1712804214',
        'ul': 'en-us',
        'sr': '1536x864',
        'uaa': 'x86',
        'uab': '64',
        'uafvl': 'Google%20Chrome;123.0.6312.106|Not%3AA-Brand;8.0.0.0|Chromium;123.0.6312.106',
        'uamb': '0',
        'uam': '',
        'uap': 'Windows',
        'uapv': '15.0.0',
        'uaw': '0',
        'are': '1',
        'pscdl': 'label_only_5',
        '_eu': 'AEE',
        '_s': '3',
        'sid': '1712804213',
        'sct': '1',
        'seg': '0',
        'dl': 'https://ssstik.io/en',
        'dt': 'TikTok Downloader - Download TikTok Video Without Watermark Online',
        'en': 'form_start',
        'ep.form_id': '_gcaptcha_pt',
        'ep.form_name': '',
        'ep.form_destination': 'https://ssstik.io/en',
        'epn.form_length': '5',
        'ep.first_field_id': 'main_page_text',
        'ep.first_field_name': 'id',
        'ep.first_field_type': 'text',
        'epn.first_field_position': '1',
        '_et': '5953',
        'tfd': '17169',
    }

    response = requests.post('https://www.google-analytics.com/g/collect', params=params, headers=headers)


    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'content-length': '0',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    
    params = {
        'v': '2',
        'tid': 'G-ZSF3D6YSLC',
        'gtm': '45je4480v9115464968z8810593590za200',
        '_p': '1712804213384',
        'gcd': '13l3l3l3l1',
        'npa': '0',
        'dma': '0',
        'tcfd': '10000',
        'cid': '992252036.1712804214',
        'ul': 'en-us',
        'sr': '1536x864',
        'uaa': 'x86',
        'uab': '64',
        'uafvl': 'Google%20Chrome;123.0.6312.106|Not%3AA-Brand;8.0.0.0|Chromium;123.0.6312.106',
        'uamb': '0',
        'uam': '',
        'uap': 'Windows',
        'uapv': '15.0.0',
        'uaw': '0',
        'are': '1',
        'pscdl': 'label_only_5',
        '_s': '4',
        'sid': '1712804213',
        'sct': '1',
        'seg': '0',
        'dl': 'https://ssstik.io/en',
        'dt': 'TikTok Downloader - Download TikTok Video Without Watermark Online',
        'en': 'link-submit_supported-links',
        '_c': '1',
        'ep.insertedLink': 'https://www.tiktok.com/@papayaho.cat/video/7041970214925323525',
        '_et': '68',
        'tfd': '19451',
    }

    response = requests.post('https://www.google-analytics.com/g/collect', params=params, headers=headers)


    cookies = {
        '_ga': 'GA1.1.992252036.1712804214',
        '__gads': 'ID=84e331e72f38de50:T=1712804213:RT=1712804213:S=ALNI_MbUfT9zeV6IYehd3qaD--dT1dQEBA',
        '__gpi': 'UID=00000de830419cf4:T=1712804213:RT=1712804213:S=ALNI_MY_e6TDUAelAY0FBC5QpObXXfprWA',
        '__eoi': 'ID=10eeba9839d222ad:T=1712804213:RT=1712804213:S=AA-Afja16RJPdT1D97nudiLcmoei',
        'FCNEC': '%5B%5B%22AKsRol-Ln1WqMuWd1GJ2GMv7HCGcKL1uNaNjMMIBJEjOlSsBVtR0Zs94q2wN0WgIHNZ2UtnHQ2NXHXEtIAyEDheHTROSP0g6UsfYVozu_5Jl91uH_Depuwc4g1S9HNIzM3i5huCmhYz2EuHN78rFiT9VGCR0S1XqLA%3D%3D%22%5D%5D',
        '_ga_ZSF3D6YSLC': 'GS1.1.1712804213.1.0.1712804232.0.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.992252036.1712804214; __gads=ID=84e331e72f38de50:T=1712804213:RT=1712804213:S=ALNI_MbUfT9zeV6IYehd3qaD--dT1dQEBA; __gpi=UID=00000de830419cf4:T=1712804213:RT=1712804213:S=ALNI_MY_e6TDUAelAY0FBC5QpObXXfprWA; __eoi=ID=10eeba9839d222ad:T=1712804213:RT=1712804213:S=AA-Afja16RJPdT1D97nudiLcmoei; FCNEC=%5B%5B%22AKsRol-Ln1WqMuWd1GJ2GMv7HCGcKL1uNaNjMMIBJEjOlSsBVtR0Zs94q2wN0WgIHNZ2UtnHQ2NXHXEtIAyEDheHTROSP0g6UsfYVozu_5Jl91uH_Depuwc4g1S9HNIzM3i5huCmhYz2EuHN78rFiT9VGCR0S1XqLA%3D%3D%22%5D%5D; _ga_ZSF3D6YSLC=GS1.1.1712804213.1.0.1712804232.0.0.0',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'UGRlUU0_',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    download_soup = BeautifulSoup(response.text, "html.parser")
    download_link = download_soup.a["href"]

    mp4_file = urlopen(download_link)
    with open(os.path.join(output_folder, f"{id}.mp4"), "wb") as output:
        while True:
            data = mp4_file.read(4096)
            if data:
                output.write(data)
            else:
                break

def main():
    while True:
        print("\nWelcome to the Download Dashboard!")
        print("1. Download TikTok Video")
        print("2. Download YouTube Video")
        print("Type 'exit' to quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            download_video_from_tiktok()
        elif choice == '2':
            download_video_from_youtube()
        elif choice.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
