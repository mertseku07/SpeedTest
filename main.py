import math
import speedtest

def  bytes_to_mb(size_bytes):
        i = int(math.floor(math.log(size_bytes,1024)))
        power = math.pow(1024,i)
        size = round(size_bytes/power,2)
        return f"{size}Mbps"

wifi = speedtest.Speedtest(secure=True)

print("Getting your download speed...")
download_speed = wifi.download()

print("Getting your upload speed...")
upload_speed = wifi.upload()

print("------------------------------")

print("Your Download Speed: ", bytes_to_mb(download_speed))
print("Your Upload Speed: ", bytes_to_mb(upload_speed))
