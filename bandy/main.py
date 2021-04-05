import speedtest

s = speedtest.Speedtest()
s.get_best_server()
download_speed = s.download()
upload_speed = s.upload()

results_dict = s.results.dict()

print(download_speed, upload_speed)
print(results_dict)
