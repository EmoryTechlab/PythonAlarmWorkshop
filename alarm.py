from os import listdir
import pygame
import schedule
import time

def job():
	location = 'alarm.mp3'
	#ensure file name is the same
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(location)
	pygame.mixer.music.play(0)
	#loads sound


schedule.every().day.at("15:00").do(job)
#schedule.every(1).minutes.do(job)
#for quick schedule testing

while True:
	schedule.run_pending()
	time.sleep(1)
	#job()
	#for quick sound testing
