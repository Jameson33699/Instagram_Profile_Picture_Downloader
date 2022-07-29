import instaloader

insta = instaloader.Instaloader()
dp = input("Enter Instagram Username: ")

insta.download_profile(dp, profile_pic_only=True)