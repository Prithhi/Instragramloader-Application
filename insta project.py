import instaloader
profile_name = input("Enter the profile name: ")
print("Downloading the profile picture of " + profile_name)
instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
print("Completed")