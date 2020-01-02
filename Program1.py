from bs4 import BeautifulSoup

with open("https://medium.com/better-humans/how-to-set-up-your-iphone-for-productivity-focus-and-your-own-longevity-bb27a68cc3d8") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")